# LinkedIn Scraper

## Overview

LinkedIn Scraper is a web application designed to scrape LinkedIn profiles and download the resulting data as a CSV file. This tool can be used for various purposes, such as research, data analysis, and networking.

## Features

- **Scrape LinkedIn Profiles:** Extract specific data from LinkedIn profiles.
- **Download as CSV:** Download the scraped data in a CSV file format.
- **User-Friendly Interface:** Easy-to-use interface for entering LinkedIn URLs and scraping data.

## Prerequisites

- Python 3.x
- Flask
- BeautifulSoup4
- Requests
- Pandas

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/linkedin-scraper.git
    cd linkedin-scraper
    ```

2. **Set up a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Activate the virtual environment:**

    ```bash
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

2. **Run the application:**

    ```bash
    flask run
    ```

3. **Open your web browser and navigate to:**

    ```text
    http://127.0.0.1:5000/
    ```

4. **Enter the LinkedIn URL you want to scrape and click "Scrape" to download the CSV file.**

## Note

Pleae ensure that you comply with LinkedIn’s terms of service when scraping data from their platform.

---