import requests
import json

url = "http://127.0.0.1:5000/segments/download"
payload = {
    'segments': {
        'width': 6,
        'height': 6,
        'count': 100
    }
}
data = json.dumps(payload)
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=data, headers=headers)
# print(response.text)
# print(response.status_code)
# print(response)

url = "http://127.0.0.1:5000/seasdgments"
params = {
    "id": 123,
    "limit": 10,
    "segment": 4
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
except Exception as err:
    print('YOOO', err)

def download_image(url):
    if not url:
        return "No url provided"

    response = requests.post(url)
    
    if response.ok:
        data = requests.get(response.json()['image'])
        with open('image.jpg', 'wb') as file:
            file.write(data.content)
    else:
        print('Error code: ', response.status_code)
        print('Error: ', response.text)


if response.ok:
    data = response.json()
    print()
    url = data.get("url")
    download_image(url)
else:
    print('Error code: ', response.status_code)
    print('Error: ', response.text)