# Image Geolocalization Prediction Model

"Geolocalization is the process of determining or estimtaing the geographic position of an object. Geopositioning yields a set of geographic coordinates in a given map datum; positions may also be expressed as a bearing and range from a known landmark"

## Objective

The objective of this project to accurately estimate a Static Google Street View Image inside the bounds of the world map.

## Motivation:

To replicate the state of the art model from scratch: https://lukashaas.github.io/PIGEON-CVPR24/. Also to get good at Geo Guessr

## Overview:

### 1) Segmenting

Segment the ecquirectangular projection of the world map into 6x6° geocell segments.

Run `python3 main.py display`

<img width="1422" alt="Screenshot 2024-09-09 at 6 13 32 PM" src="https://github.com/user-attachments/assets/8ad696d1-ba78-4c4d-9f00-31b17bb1aa14">

### 2) Data Collection

For regions covered by Geo Guessr (typiclly regions that have decent street view coverage), pull 100 images for each segment using Street View Static API.

The dataset can be found under `./data` or you can create your own dataset with the script.

### 3) Model Training

Train a deep convulational neural network given each image and its segment (label).

### 4) Inference

Run `python3 main.py predict <image_path>`

Takes the top K predictions and hedges a guess based on a weighted centroid calcultion.

![Screenshot 2024-09-09 at 6 12 41 PM](https://github.com/user-attachments/assets/632d6a62-e40a-4c77-b241-5fedaccd7dc7)

## Future Improvements

Use Ensemble learning by incorporating other base models that can detect certain meta data (Camera generation, cars/street poles, landmarks etc.)

## Benchmarking:

The following are test sets to benchmark geolocalization model. I'm currently aiming to place in the top 25% of Geo Guessr players just using this model.

![image](https://github.com/user-attachments/assets/770c1988-1f53-4839-9325-450f6c5de758)
