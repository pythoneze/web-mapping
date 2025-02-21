import folium
import pandas as pd

data = pd.read_csv('files/world_capitals.txt')

mymap = folium.Map(
    location=[38.58, -99.89], 
    zoom_start=6
)

fgc = folium.FeatureGroup(name="Capitals")

for _, row in data.iterrows():
    folium.Marker(
        location=[row["LAT"], row["LON"]],
        popup=row["NAME"],
        icon=folium.Icon(color='blue')
    ).add_to(fgc)

fgp = folium.FeatureGroup(name="Population")

def get_population_color(population):
    if population < 10000000:
        return 'green'
    elif 10000000 <= population < 50000000:
        return 'yellow'
    elif 50000000 <= population < 100000000:
        return 'orange'
    else:
        return 'red'

with open("files/world.json", "r", encoding="utf-8-sig") as f:
    geojson_data = f.read()

fgp.add_child(folium.GeoJson(
    data=geojson_data,
    style_function=lambda x: {'fillColor': get_population_color(x['properties']['POP2005'])}
))

mymap.add_child(fgc)
mymap.add_child(fgp)
mymap.add_child(folium.LayerControl())


mymap.save("map_1.html")
