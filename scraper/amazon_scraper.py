import requests
from bs4 import BeautifulSoup
from scraper.product import Product

class AmazonScraper:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
        self.products = []

    def get_soup(self, url):
        response = requests.get(url, headers=self.headers)
        print(f"Fetching URL: {url}")
        return BeautifulSoup(response.content, "html.parser")

    def scrape(self):
        soup = self.get_soup(self.url)
        links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})
        links_list = ["https://www.amazon.com" + link.get('href') for link in links]
        print(f"Found {len(links_list)} product links")

        for link in links_list:
            product_soup = self.get_soup(link)
            product = Product.from_soup(product_soup)
            self.products.append(product)
            print(f"Scraped product: {product.title}")

    def get_data(self):
        data = {
            "title": [product.title for product in self.products],
            "specifications": [product.specifications for product in self.products],
            "price": [product.price for product in self.products],
            "rating": [product.rating for product in self.products],
            "reviews": [product.review_count for product in self.products],
            "availability": [product.availability for product in self.products],
        }
        return data
