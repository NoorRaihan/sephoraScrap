# Web Scraping for ISP610
# 💄 Sephora Product Review Scraper

This Python script scrapes **product reviews** from [Sephora Malaysia](https://www.sephora.my) using the site's internal API, powered by **Selenium**, **BeautifulSoup**, and **Pandas**.

It collects reviews by rating (1 to 5 stars) and saves the data into CSV files for easy analysis.

---

## 🚀 Features

- 🔎 Scrapes reviews using Sephora’s public API endpoints
- 🧠 Uses headless browser automation with Selenium for bypassing potential bot protections
- 📊 Saves structured review data into CSV files by rating and all combined
- 📁 Output includes:
  - `data_1.csv` to `data_5.csv` — reviews grouped by star rating
  - `data_full.csv` — all reviews merged into one file

---

## ⚙️ Requirements

Make sure you have the following installed:

- Python 3.7+
- Google Chrome
- ChromeDriver (matching your Chrome version)

### 📦 Install Python dependencies:

```bash
pip install selenium beautifulsoup4 pandas
```
⚠️ This script uses ChromeDriver. Make sure it is in your PATH or properly configured.

🧾 Usage
🔧 Edit the product ID
In the script, change the PRODUCT_ID to the one you want to scrape:

```python
PRODUCT_ID = "nudestix-nudies-matte-all-over-face-color-blush"
```
You can get the ID from the product\'s URL on Sephora, like:

```http
https://www.sephora.my/products/nudestix-nudies-matte-all-over-face-color-blush
```

▶️ Run the script:
```bash
python scraper.py
```
It will open a browser window, scrape reviews by rating from 1 to 5, and save the data into CSVs.

🗃 Output Files
- data_1.csv → all 1-star reviews
- data_2.csv → all 2-star reviews
- data_3.csv → all 3-star reviews
- data_4.csv → all 4-star reviews
- data_5.csv → all 5-star reviews
- data_full.csv → all reviews combined

Each CSV includes columns like:
- rating
- title
- text
- reviewer-name
- country-name
- is-staff

🧠 How It Works
1. Initializes a Selenium-controlled Chrome browser.
2. Iterates through review endpoints for ratings 1–5.
3. Parses the JSON responses using BeautifulSoup and stores reviews.
4. Writes review data to separate CSV files by rating and a full merged file.

🔒 Notes
- This script uses Sephora’s public API used by their frontend. It's not an official API.
- Do not abuse or spam requests. Use responsibly for research or academic purposes.
