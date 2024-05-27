import networkx as nx
import osmnx as ox
import requests
import sys,os,os.path
import matplotlib.cm as cm
import matplotlib.colors as colors
ox.config(use_cache=True, log_console=True)
ox.__version__

place = {'city' : 'Shibuya',
         'state' : 'Tokyo',
         'country' : 'Japan'}
G = ox.graph_from_place(place, network_type='drive')
# fig, ax = ox.plot_graph(G, node_size=0, edge_linewidth=0.5)

import osmnx as ox
import matplotlib.pyplot as plt

# Specify the name that is used to seach for the data
place_name = "Ariake, Tokyo, Japan" 

# Fetch OSM street network from the location
graph = ox.graph_from_place(place_name)

type(graph)

# fig, ax = ox.plot_graph(graph)

area = ox.geocode_to_gdf(place_name)
type(area)

nodes, edges = ox.graph_to_gdfs(graph)
nodes.head()
edges.head()

# building
buildings = ox.geometries_from_place(place_name, tags={'building':True})

len(buildings)

buildings.head(3)

# restautant
restaurants = ox.geometries_from_place(place_name, 
                                  tags={"amenity": "restaurant"}
                                 )

restaurants.columns

fig, ax = plt.subplots(figsize=(12,8))
area.plot(ax=ax, facecolor='black')
edges.plot(ax=ax, linewidth=1, edgecolor='gray')
buildings.plot(ax=ax, facecolor='dimgray', alpha=0.7)
restaurants.plot(ax=ax, color='yellow', alpha=0.7, markersize=10)
plt.tight_layout()