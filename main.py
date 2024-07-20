from scraper.amazon_scraper import AmazonScraper
from scraper.utils import save_to_csv

if __name__ == "__main__":
    HEADERS = ({'User-Agent': '', 'Accept-Language': 'en-US, en;q=0.5'})
    URL = "https://www.amazon.com/s?k=light+mouse&crid=I0X206CENT5X&sprefix=light+mous%2Caps%2C234&ref=nb_sb_noss_2"

    scraper = AmazonScraper(URL, HEADERS)
    scraper.scrape()
    data = scraper.get_data()
    amazon_df = save_to_csv(data, "data/amazon_data.csv")
    print(amazon_df)
