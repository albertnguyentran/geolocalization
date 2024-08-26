'''
Segment the world map into squares.

Using Google Street View API: https://developers.google.com/maps/documentation/streetview/overview

Pull x images for each square, with the square being its label

Train a DNN on this dataset to predict the square the image was taken in.

Run a clustering algorithm to determine the hedge point based on the predicted probabilities
'''