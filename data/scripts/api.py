import requests
import json

# test = requests.get('https://jsonplaceholder.typicode.com/posts')
# data = test.json()

url = 'http://randomfox.ca/floof'
response = requests.get(url)

data = response.json()
image_url = data['image']

image = requests.get(image_url)

# print(dir(image))
print(image.content)

sg