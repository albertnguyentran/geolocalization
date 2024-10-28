import os
import requests
import argparse
from helpers import coloured
from dotenv import load_dotenv




if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')

    parser = argparse.ArgumentParser()
    parser.add_argument('--number', type=int, default=100, help='Number of images per region')
    parser.add_argument('--regions', type=int, default=5, help='Number of regions')
    args = parser.parse_args()

    print(args.number)
    print(args.regions)


