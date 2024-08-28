'''
First naively segment the ecquirectangular projection of the world map into squares.

We will run into some issues because not all squares will have street view images in google maps

The world map ranges from latitude: [-90, 90] and longitude [-180, 180]
'''

import plotly.graph_objects as go

class Map:
    def __init__(self):
        self.prediction = {}
        self.segment_count = 0
        self.fig = go.Figure()
        self.fig_coords = []
        self.segmentMap()
        self.configureMap()
    
    @staticmethod
    def get_segment(lon, lat):
        lat_segment = 90 - (lat + 90) // 6 * 6
        lon_segment = -180 + (lon + 180) // 6 * 6
        return (lon_segment, lat_segment)
    
    def segmentMap(self):
        for i in range(90, -66, -6):
            for j in range(-180, 180, 6):
                self.prediction[self.get_segment(j, i)] = 0
                lon, lat = (j, j, j+6, j+6, j), (i, i-6, i-6, i, i)
                self.fig_coords.append([lon, lat])

                if sum(self.get_segment(j, i)):
                    print('here')
                    p = f"rgba(255, 0, 0, 0.1)"
                else:
                    print('-')
                    p = f"rgba(0, 0, 255, 0)"

                self.fig.add_trace(go.Scattergeo(
                    lon=lon,
                    lat=lat,
                    mode="lines+markers+text",
                    fill="toself",
                    line=dict(
                        color="black",
                        width=8
                    ),
                    marker=go.scattergeo.Marker(
                        color=p
                    ),
                    fillcolor=p,
                    opacity=0.03
                ))
                self.segment_count += 1
    
    def configureMap(self):
        self.fig.update_geos(
            resolution=50,
            projection=dict(
                type="equirectangular"
            ),
            showland=True,
            showcountries=True,
            showocean=True,
        )

        self.fig.update_layout(
            title = 'Segmented map',
            margin = {'l':0, 'r':0, 'b':0, 't':0},
            mapbox_bounds=dict(west=-180, east=180, south=-66, north=90),
            showlegend=False
        )
    
    def displayMap(self):
        self.fig.show()

def main():
    test_map = Map()

    test_map.displayMap()

    # print(test_map.segment_count)
    # for lat, lon in test_map.fig_coords:
    #     print(lat, lon)
    # print(len(test_map.prediction.keys()))

if __name__ == "__main__":
    main()