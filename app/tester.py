import requests
import config


json_data = requests.get(config.Config.URL_START + "harry+potter" + config.Config.URL_END).json()
items = json_data['items']
title = items[0]['volumeInfo']['title']
author = items[0]['volumeInfo']['authors'][0]
image_link_small = items[0]['volumeInfo']['imageLinks']['smallThumbnail']
image_link = items[0]['volumeInfo']['imageLinks']['thumbnail']
description = items[0]['volumeInfo']['description']
isbn = items[0]['volumeInfo']['industryIdentifiers'][1]['identifier']
id = items[0]['id']

print('Title: ' + title)
print('Author: ' + author)
print('Id: ' + id)
print('ISBN: ' + isbn)
print('Image link: ' + image_link)
print('Small image link: ' + image_link_small)
print('Description: ' + description)

