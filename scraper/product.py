class Product:
    def __init__(self, title, specifications, price, rating, review_count, availability):
        self.title = title
        self.specifications = specifications
        self.price = price
        self.rating = rating
        self.review_count = review_count
        self.availability = availability

    @classmethod
    def from_soup(cls, soup):
        title, specifications = cls.get_title_and_specifications(soup)
        price = cls.get_price(soup)
        rating = cls.get_rating(soup)
        review_count = cls.get_review_count(soup)
        availability = cls.get_availability(soup)
        return cls(title, specifications, price, rating, review_count, availability)

    @staticmethod
    def get_title_and_specifications(soup):
        try:
            title = soup.find("span", attrs={"id": 'productTitle'}).text.strip()
            if ":" in title:
                title, specifications = title.split(":", 1)
            elif "-" in title:
                title, specifications = title.split("-", 1)
            else:
                specifications = ""
        except AttributeError:
            title = ""
            specifications = ""
        return title.strip(), specifications.strip()

    @staticmethod
    def get_price(soup):
        try:
            price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).text.strip()
        except AttributeError:
            try:
                price = soup.find("span", attrs={'id': 'priceblock_dealprice'}).text.strip()
            except AttributeError:
                try:
                    price = soup.find("span", attrs={'class': 'a-price-whole'}).text.strip() + \
                            soup.find("span", attrs={'class': 'a-price-fraction'}).text.strip()
                except AttributeError:
                    price = ""
        return price

    @staticmethod
    def get_rating(soup):
        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).text.strip()
        except AttributeError:
            rating = ""
        return rating

    @staticmethod
    def get_review_count(soup):
        try:
            review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).text.strip()
        except AttributeError:
            review_count = ""
        return review_count

    @staticmethod
    def get_availability(soup):
        try:
            available = soup.find("div", attrs={'id': 'availability'}).find("span").text.strip()
        except AttributeError:
            available = "Not Available"
        return available
