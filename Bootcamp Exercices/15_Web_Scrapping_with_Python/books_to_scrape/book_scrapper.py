import requests
import bs4

# Get title of every book that has a two stars rating.


def get_soup_of_pages():
    """
    Returns a list of the soup of each url in the book store webpage.
    :return: soup_each_page ([]) - List of the soup of each page on book store webpage.
    """
    request_succeed = True
    soup_each_page = []

    while request_succeed:
        for page_number in range(1, 1001):
            res = requests.get(f"https://books.toscrape.com/catalogue/page-{page_number}.html")
            # Check if our status response code is 200.
            if res.status_code == 200:
                # Create our soup of pages an insert each of these in soup_each_page list.
                soup = bs4.BeautifulSoup(res.text, 'lxml')
                soup_each_page.insert(-1, soup)
            else:
                break
        request_succeed = False
    return soup_each_page


def get_all_books(soup_each_page):

    list_of_books = []
    for books_per_page in soup_each_page:
        list_of_books.extend(books_per_page.select(".product_pod"))
    return list_of_books


def get_two_stars_books(list_of_books):
    two_stars_books = [book.select("h3 a")[0]["title"] for book in list_of_books if book.select(".star-rating.Two")]
    return two_stars_books


if __name__ == "__main__":
    soup_of_pages = get_soup_of_pages()
    total_books_on_page = get_all_books(soup_of_pages)
    two_stars_books_list = get_two_stars_books(total_books_on_page)
    print(two_stars_books_list)
    print(len(two_stars_books_list))

