from dotenv import load_dotenv
import os
import requests
import sys

load_dotenv()
api_key = os.getenv('GOOGLE_MAPS_API_KEY')


def get_image(fov, heading, pitch, width, height):
    '''
    size: 400x400 should be fine, you dont get much more information from 800x800. consider geoguessr input though

    # 640x360   (decent size, lower data usage)
    # 854x480   (480p)
    # 1280x720  (720p)
    # 1920x1080 (1080p - note: API might have size limits)

    heading: compass heading camera (0, 360)
    - for each image, take 2/4 different headings
    fov: field of view (default of 90), doesnt change how much you see
    pitch: up or down angle (default of 0, 90 is straight up)
    radius: radius to search for a panorama (valid image), set pretty high?
    source: default (indoors and outdoors), outdoor (only outdoors)
    return error code: set to true to return a 404 instead of a blank image
    '''

    params = {
        'size': f'{width}x{height}',
        'location': '12.5763831,102.4211769',
        'fov': fov,
        'heading': heading,
        'key': api_key,
        'pitch': pitch,
        'radius': 1000,
        'return_error_code': True
    }

    url = 'https://maps.googleapis.com/maps/api/streetview' 
    response = requests.get(url, params=params)
    data = response.content

    if not response.ok:
        print(response)
        return

    with open(f'../images/test_images/test_images_{width}x{height},fov={fov},heading={heading},pitch={pitch}.jpg', 'wb') as file:
        file.write(data)

if __name__ == "__main__":
    arguments = sys.argv
    print(arguments)
    fov = arguments[1]
    heading = arguments[2]
    pitch = arguments[3]
    width = arguments[4] if len(arguments) > 4 else '400'
    height = arguments[5] if len(arguments) > 4 else '400'

    get_image(fov, heading, pitch, width, height)