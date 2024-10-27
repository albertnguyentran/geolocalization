import requests
import json

test = requests.get('https://jsonplaceholder.typicode.com/posts')
data = json.loads(test.text)
print(json.dumps(data, indent=4))
# print(test.json)
