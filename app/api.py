import requests
import config


def get_book_data(search):
    try:
        json_data = requests.get(config.Config.URL_START + split_search_term(search) + config.Config.URL_END).json()
        items = json_data['items']
        search_results = []

        if len(items) > 3:
            for i in range(3):
                book_info = {}
                book_info['title'] = items[i]['volumeInfo']['title']
                book_info['author'] = items[i]['volumeInfo']['authors'][0]
                book_info['image_link_small'] = items[i]['volumeInfo']['imageLinks']['smallThumbnail']
                book_info['image_link'] = items[i]['volumeInfo']['imageLinks']['thumbnail']
                book_info['description'] = items[i]['volumeInfo']['description']
                book_info['isbn'] = items[i]['volumeInfo']['industryIdentifiers'][1]['identifier']
                book_info['id'] = items[i]['id']
                search_results.append(book_info)
        else:
            for i in range(len(items)):
                book_info = {}
                book_info['title'] = items[i]['volumeInfo']['title']
                book_info['author'] = items[i]['volumeInfo']['authors'][0]
                book_info['image_link_small'] = items[i]['volumeInfo']['imageLinks']['smallThumbnail']
                book_info['image_link'] = items[i]['volumeInfo']['imageLinks']['thumbnail']
                book_info['description'] = items[i]['volumeInfo']['description']
                book_info['isbn'] = items[i]['volumeInfo']['industryIdentifiers'][1]['identifier']
                book_info['id'] = items[i]['id']
                search_results.append(book_info)

        return search_results
    except Exception:
        print('Something went wrong.')


def split_search_term(search_term):
    terms = search_term.split(' ')
    concat = ''
    for i in range(len(terms)):
        if i == (len(terms) - 1):
            concat += terms[i]
        else:
            concat += terms[i] + '+'
    return concat




    # json_data = requests.get(config.Config.URL_START + "harry+potter" + config.Config.URL_END).json()
    # items = json_data['items']
    # title = items[0]['volumeInfo']['title']
    # author = items[0]['volumeInfo']['authors'][0]
    # image_link_small = items[0]['volumeInfo']['imageLinks']['smallThumbnail']
    # image_link = items[0]['volumeInfo']['imageLinks']['thumbnail']
    # description = items[0]['volumeInfo']['description']
    # isbn = items[0]['volumeInfo']['industryIdentifiers'][1]['identifier']
    # id = items[0]['id']

    # print('Title: ' + title)
    # print('Author: ' + author)
    # print('Id: ' + id)
    # print('ISBN: ' + isbn)
    # print('Image link: ' + image_link)
    # print('Small image link: ' + image_link_small)
    # print('Description: ' + description)


# d = get_book_data('harry potter')
# for i in range(len(d)):
#     print(d[i])