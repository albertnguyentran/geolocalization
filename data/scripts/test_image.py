from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv('GOOGLE_MAPS_API_KEY')


def get_image():
    '''
    heading: compass heading camera (0, 360)
    - for each image, take 2/4 different headings
    fov: field of view (default of 90)
    pitch: up or down angle (default of 0, 90 is straight up)
    radius: 
    '''

    url = f'https://maps.googleapis.com/maps/api/streetview?size=400x400&location=47.5763831,-122.4211769&fov=90&heading=360&pitch=0&key={api_key}' 
    response = requests.get(url)
    data = response.content

    with open('../images/test_images_heading360.jpg', 'wb') as file:
        file.write(data)

if __name__ == "__main__":
    