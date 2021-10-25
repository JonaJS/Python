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
        authors_list = set()
        soup = self.get_main_page_scrapped()
        raw_authors_list = soup.select(".author")

        for author in raw_authors_list:
            authors_list.add(author.text)
        
        return authors_list


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

    
    def get_all_authors(self):
        page_still_valid = True
        authors_list = set()
        page_number = 1

        while page_still_valid:
            page_url = f"{self.url}page/{page_number}"
            res = requests.get(page_url)
            
            if "No quotes found!" in res.text:
                break
            else:
                soup = bs4.BeautifulSoup(res.text, 'lxml')

                for author in soup.select(".author"):
                    authors_list.add(author.text)
                    
            page_number += 1
        
        return authors_list
