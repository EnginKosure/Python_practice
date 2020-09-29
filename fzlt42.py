import json
import requests

response_albums = requests.get("https://jsonplaceholder.typicode.com/albums")
albums = json.loads(response_albums.text)

print('\nRESPONSE FOR ALBUMS FROM JSONPLACEHOLDER API CALL')
print(albums[:2])

response_photos = requests.get("https://jsonplaceholder.typicode.com/photos")
photos = json.loads(response_photos.text)

print('\n\nRESPONSE FOR ALBUMS FROM JSONPLACEHOLDER API CALL')
print(photos[:2])
