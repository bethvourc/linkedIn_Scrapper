from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

def scrape_linkedin_profile(url, username, password):
    # Setup Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Login to LinkedIn
    driver.get('https://www.linkedin.com/login')
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')
    username_input.send_keys(username)
    password_input.send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    
    # Wait for login to complete
    time.sleep(5)
    
    # Navigate to the target profile URL
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(5)
    
    # Get the page source and create a BeautifulSoup object
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Extract the required information
    name = soup.select_one('.pv-text-details__left-panel h1').get_text(strip=True)
    title = soup.select_one('.pv-text-details__left-panel .text-body-medium').get_text(strip=True)
    company = soup.select_one('.pv-text-details__left-panel .text-body-small').get_text(strip=True)
    
    # Role(s) they are recruiting for (if available)
    roles_section = soup.find('section', {'id': 'experience-section'})
    roles = ""
    if roles_section:
        roles = roles_section.get_text(strip=True)
    
    # Email is generally not available directly on LinkedIn profiles, you might need additional steps to obtain it
    email = "N/A"

    # Close the browser
    driver.quit()
    
    profile_data = {
        'Name': name,
        'Title': title,
        'Company': company,
        'Roles': roles,
        'Email': email
    }

    return profile_data

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    username = data.get('username')
    password = data.get('password')

    if not url or not username or not password:
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        profile_data = scrape_linkedin_profile(url, username, password)
        return jsonify(profile_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
