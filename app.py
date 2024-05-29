from flask import Flask, render_template, request, send_file
from scraper import scrape_linkedin_profile
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['POST']
    data = scrape_linkedin_profile(url)
    df = pd.DataFrame(data)
    csv_file = 'output.csv'
    df.to_csv(csv_file, index=False)
    return send_file(csv_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)