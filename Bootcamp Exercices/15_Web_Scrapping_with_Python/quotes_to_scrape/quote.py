import requests
import bs4


class Quote:
    def __init__(self):
        self.url = "https://quotes.toscrape.com/"

    
    def get_main_page_scrapped(self):
        res = requests.get(self.url)
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        return soup

    
    def get_authors_main_page(self):
        soup = self.get_main_page_scrapped()
        raw_authors_list = soup.select(".author")
        enhaced_authors_list = [author.text for author in raw_authors_list]
        return enhaced_authors_list

    def get_main_page_quotes(self):
        soup = self.get_main_page_scrapped()
        raw_quotes_list = soup.select(".text")
        enhaced_quotes_list = [quote.text for quote in raw_quotes_list]
        return enhaced_quotes_list

    def get_top_ten_tags(self):
        soup = self.get_main_page_scrapped()
        tag_box = soup.select("span > a")
        top_ten_tag_list = [tag.text for tag in tag_box if tag.text != "(about)"]
        return top_ten_tag_list