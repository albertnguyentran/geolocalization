'''
Segment the world map into squares.

Using Google Street View API: https://developers.google.com/maps/documentation/streetview/overview

Pull x images for each square, with the square being its label

Train a DNN on this dataset to predict the square the image was taken in.

Run a clustering algorithm to determine the hedge point based on the predicted probabilities
'''
import plotly.graph_objects as go

# Sample data
lats = [40.7128, 34.0522, 41.8781, 29.7604, 47.6062]
lons = [-74.0060, -118.2437, -87.6298, -95.3698, -122.3321]
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Seattle"]

# Create the figure
fig = go.Figure()

# Add the scattergeo trace
fig.add_trace(go.Scattergeo(
    lon = lons,
    lat = lats,
    text = cities,
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'red',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )
))

# Update the layout to use equirectangular projection
fig.update_geos(
    projection_type="equirectangular",
    showland=True,
    showcountries=True,
    showocean=True,
    landcolor='rgb(243, 243, 243)',
    countrycolor='rgb(204, 204, 204)',
    oceancolor='rgb(230, 230, 250)'
)

# Set the figure size and title
fig.update_layout(
    title = 'Cities on Equirectangular Projection',
    height=600,
    width=1000
)

# Show the plot
fig.show()