from config import Config
import requests
import app.api as google_api


def get_nyt_bestsellers(): # FICTION !!!
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
        book_info['cover_image'] = get_google_cover_image(title=current_book['book_details'][0]['title'])
        books.append(book_info)
    return books


def get_nyt_bestsellers_nonfiction():
    data = requests.get(Config.NYT_URL_NONFICTION).json()
    results = data['results']
    books = []
    for i in range(8):
        book_info = {}
        current_book = results[i]
        book_info['title'] = current_book['book_details'][0]['title']
        book_info['author'] = current_book['book_details'][0]['author']
        book_info['description'] = current_book['book_details'][0]['description']
        book_info['amazon_link'] = current_book['amazon_product_url']
        book_info['cover_image'] = get_google_cover_image(title=current_book['book_details'][0]['title'])
        books.append(book_info)
    return books


def get_google_cover_image(title):
    return google_api.get_one_book_image_link(title)


# b = get_nyt_bestsellers_nonfiction()
# print(b)