import plotly.graph_objects as go

# fig = go.Figure(go.Scattermapbox(mode="markers", lon=[-73.605], lat=[45.51]))
                               
# for i, c in enumerate(df.coords):
#     coords = get_close_coords(c)
#     fig.add_trace(go.Scattermapbox(lat=[x[1] for x in coords], 
#                                    lon=[x[0] for x in coords],
#                                    mode="lines",
#                                    marker=go.scattermapbox.Marker(
#                                        color=df.test_type_color[i]
#                                    ),
#                                    fill="toself",
#                                    name="Area %s" % i,
#                                    opacity=0.4
#                                   ))

# fig.update_layout(
#     mapbox = {
#         'style': "stamen-terrain",
#         'center': {'lon': -73.6, 'lat': 45.5},
#         'zoom': 11,
#         #'color': df.test_type,
#     },
#     margin = {'l':0, 'r':0, 'b':0, 't':0})
# fig.show()




# (topleft, bottomleft, bottomright, topright, topleft)

coords = []
for i in range(90, -66, -6):
    for j in range(-180, 180, 6):
        coords.append([(j, j, j+6, j+6, j), (i, i-6, i-6, i, i)])

# for c in coords:
#     print(c)
# coords = [
#     [(-10, -10, 8, 8, -10), (30, 6, 6, 30, 30)],
#     [(30, 30, 50, 50, 30), (20, 30, 30, 20, 20)],
#     [(100, 100, 80, 80, 100), (40, 50, 50, 40, 40)],
# ]

print(len(coords))
fig = go.Figure()

for lon, lat in coords:
    fig.add_trace(go.Scattergeo(
        lon=lon,
        lat=lat,
        mode="lines",
        fill="toself",
        line=dict(
            color="black",
            width=8
        ),
        fillcolor="rgba(255, 255, 255, 0)",
        
        opacity=0.03
    ))

fig.update_geos(
    resolution=50,
    projection=dict(
        type="equirectangular"
    ),
    showland=True,
    showcountries=True,
    showocean=True,
)


# fig = go.Figure(go.Scattermapbox(
#     mode = "lines", fill = "toself",
#     lon = [-10, -10, 8, 8, -10, None, 30, 30, 50, 50, 30, None, 100, 100, 80, 80, 100],
#     lat = [30, 6, 6, 30, 30,    None, 20, 30, 30, 20, 20, None, 40, 50, 50, 40, 40],
#     ))

# fig.update_geos(projection_type="equirectangular")


# fig.update_geos(
#     resolution=50,
#     showcountries=True, countrycolor="Blue"
# )

fig.update_layout(
    title = 'Segmented map',
    margin = {'l':0, 'r':0, 'b':0, 't':0},
    mapbox_bounds=dict(west=-180, east=180, south=-66, north=90),
    showlegend=False
)
# fig.update_layout(
#     mapbox=dict(
#         style="open-street-map",
#         center=dict(lat=0, lon=0),
#         zoom=0.9043657672375094,
#     ),
#     mapbox_bounds=dict(west=-180, east=180, south=-60, north=90),
#     showlegend = False,
#     autosize=False,
#     width=2000,
#     height=1500,
#     margin = {'l':0, 'r':0, 'b':0, 't':0})

fig.show()

# fig = go.Figure(go.Scattergeo())
# fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
# fig.update_layout(height=1000, width=1000, margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

# fig = go.Figure(go.Scattermapbox(
#     mode = "markers",
#     lon = [-73.605], lat = [45.51],
#     marker = {'size': 20, 'color': ["cyan"]}))

# fig.update_layout(
#     mapbox = {
#         'style': "open-street-map",
#         'center': { 'lon': 0, 'lat': 30},  # Center on prime meridian, slightly north
#         'zoom': 1,  # Zoom out to see the whole world
#         # 'projection': {'type': 'equirectangular'},  # Use equirectangular projection
#         'layers': [{
#             'source': {
#                 'type': "FeatureCollection",
#                 'features': [{
#                     'type': "Feature",
#                     'geometry': {
#                         'type': "MultiPolygon",
#                         'coordinates': [[[
#                             [-73.606352888, 45.507489991], [-73.606133883, 45.50687600],
#                             [-73.605905904, 45.506773980], [-73.603533905, 45.505698946],
#                             [-73.602475870, 45.506856969], [-73.600031904, 45.505696003],
#                             [-73.599379992, 45.505389066], [-73.599119902, 45.505632008],
#                             [-73.598896977, 45.505514039], [-73.598783894, 45.505617001],
#                             [-73.591308727, 45.516246185], [-73.591380782, 45.516280145],
#                             [-73.596778656, 45.518690062], [-73.602796770, 45.521348046],
#                             [-73.612239983, 45.525564037], [-73.612422919, 45.525642061],
#                             [-73.617229085, 45.527751983], [-73.617279234, 45.527774160],
#                             [-73.617304713, 45.527741334], [-73.617492052, 45.527498362],
#                             [-73.617533258, 45.527512253], [-73.618074188, 45.526759105],
#                             [-73.618271651, 45.526500673], [-73.618446320, 45.526287943],
#                             [-73.618968507, 45.525698560], [-73.619388002, 45.525216750],
#                             [-73.619532966, 45.525064183], [-73.619686662, 45.524889290],
#                             [-73.619787038, 45.524770086], [-73.619925742, 45.524584939],
#                             [-73.619954486, 45.524557690], [-73.620122362, 45.524377961],
#                             [-73.620201713, 45.524298907], [-73.620775593, 45.523650879]
#                         ]]]
#                     }
#                 }]
#             },
#             'type': "fill", 'below': "traces", 'color': "royalblue"}]},
#     margin = {'l':0, 'r':0, 'b':0, 't':0})

# fig.update_geos(projection_type="equirectangular")
# fig.update_layout(title="ecquirectangular")
# import plotly.graph_objects as go

# fig = go.Figure(go.Scattermapbox(
#     mode = "markers",
#     lon = [-73.605], lat = [45.51],
#     marker = {'size': 20, 'color': ["cyan"]}))

# fig.update_layout(
#     mapbox = {
#         'style': "white-bg",
#         'center': { 'lon': 0, 'lat': 30},  # Center on prime meridian, slightly north
#         'zoom': 1,  # Zoom out to see the whole world
#         'projection': {'type': 'equirectangular'},  # Use equirectangular projection
#     },
#     mapbox_layers=[
#         {
#             "below": 'traces',
#             "sourcetype": "raster",
#             "sourceattribution": "United States Geological Survey",
#             "source": [
#                 "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
#             ]
#         }
#     ],
#     margin = {'l':0, 'r':0, 'b':0, 't':0}
# )

# fig.show()

# import plotly.express as px
# import geopandas as gpd
# import numpy as np
# import pandas as pd

# df = px.data.election()

# # prep geometry
# gdf = gpd.GeoDataFrame.from_features(px.data.election_geojson())
# gdf = gdf.join(
#     gdf["geometry"].centroid.apply(lambda g: pd.Series({"lon": g.x, "lat": g.y}))
# )

# # plot circles at various lat / lon
# fig = px.scatter_mapbox(
#     df.merge(gdf, on="district"), lat="lat", lon="lon", size="total"
# ).update_layout(mapbox={"style": "carto-positron"})

# # generate a 10000m circle at a random black as geojson
# cgeo = (
#     gdf.set_crs("epsg:4326")
#     .sample(1)
#     .pipe(lambda d: d.to_crs(d.estimate_utm_crs()))["geometry"]
#     .centroid.buffer(10000)
#     .to_crs("epsg:4326")
#     .__geo_interface__
# )
# sqgeo = (
#     gdf.set_crs("epsg:4326")
#     .sample(1)
#     .pipe(lambda d: d.to_crs(d.estimate_utm_crs()))["geometry"]
#     .centroid.buffer(10000, cap_style=3)
#     .to_crs("epsg:4326")
#     .__geo_interface__
# )

# # add circle geometry as layer to mapbox figure
# fig.update_layout(
#     mapbox={
#         "layers": [
#             {"source": cgeo, "color": "PaleTurquoise", "type": "fill", "opacity":.5},
#             {"source": cgeo, "color": "black", "type": "line", "opacity": 0.1},
#             {"source": sqgeo, "color": "PaleTurquoise", "type": "fill", "opacity":.5},
#             {"source": sqgeo, "color": "black", "type": "line", "opacity": 0.1},

#         ]
#     }
# )

# fig.show()