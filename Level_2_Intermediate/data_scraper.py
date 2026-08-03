import requests
from bs4 import BeautifulSoup
import csv


def scrape_quotes():
    """Scrapes quotes and authors from quotes.toscrape.com and saves to CSV."""
    url = "http://quotes.toscrape.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 1. Fetch the web page content
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # 2. Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # 3. Extract specific data (Quotes and Authors)
        quotes = []
        quote_divs = soup.find_all('div', class_='quote')

        for div in quote_divs:
            text = div.find('span', class_='text').get_text()
            author = div.find('small', class_='author').get_text()
            quotes.append({'Quote': text, 'Author': author})

        if not quotes:
            print(" No quotes found. The website structure might have changed.")
            return

        # 4. Save data to CSV
        filename = "scraped_quotes.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Quote', 'Author']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for quote in quotes:
                writer.writerow(quote)

        print(f" Successfully scraped {len(quotes)} quotes!")
        print(f" Data saved to '{filename}'")

    except requests.exceptions.ConnectionError:
        print(" Error: Could not connect to the website.")
    except Exception as e:
        print(f" An error occurred: {e}")


if __name__ == "__main__":
    print("--- Codveda Level 2: Data Scraper ---")
    scrape_quotes()
