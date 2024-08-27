'''
First naively segment the ecquirectangular projection of the world map into squares.

We will run into some issues because not all squares will have street view images in google maps

The world map ranges from latitude: [-90, 90] and longitude [-180, 180]
'''

class Map:
    def __init__(self):
        self.segments = {}
        self.segmentMap()

    def segmentMap(self):
        for i in range(0, 360, 12):
            for j in range(0, 180, 12):
                self.segments[(i, j)] = []

test_map = Map()

for key, _ in test_map.segments.items():
    print(key)