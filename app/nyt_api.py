from config import Config
import requests


def get_nyt_bestsellers():
    data = requests.get(Config.NYT_URL).json()
    results = data['results']
    books = []
    for i in range(8):
        book_info = {}
        current_book = results[i]
        book_info['title'] = current_book['book_details'][0]['title']
        book_info['author'] = current_book['book_details'][0]['author']
        book_info['description'] = current_book['book_details'][0]['description']
        book_info['amazon_link'] = current_book['amazon_product_url']
        books.append(book_info)
    return books

# b = get_nyt_bestsellers()
# print(b)