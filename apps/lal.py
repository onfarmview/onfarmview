from shapely.geometry import Polygon
import geopandas as gpd
# Load shp files
shp = gpd.read_file("data/nzshp/Canterbury.shp")
gdf = shp.to_crs({'init': 'epsg:4326'}) 
can = []
for index, row in gdf.iterrows():
    for pt in list(row['geometry'].exterior.coords): 
        can.append(list(pt))

shp = gpd.read_file("data/nzshp/Mitimiti.shp")
gdf = shp.to_crs({'init': 'epsg:4326'}) 
Mitimiti = []
for index, row in gdf.iterrows():
    for pt in list(row['geometry'].exterior.coords): 
        Mitimiti.append(list(pt))

shp = gpd.read_file("data/nzshp/Urewera.shp")
gdf = shp.to_crs({'init': 'epsg:4326'}) 
Urewera = []
for index, row in gdf.iterrows():
    for pt in list(row['geometry'].exterior.coords): 
        Urewera.append(list(pt))

nz_rois = {
    "Canterbury":Polygon (can),
    "Mitimiti": Polygon(  Mitimiti  ),
    "Te Urewera": Polygon(  Urewera  ),

}

# Load VN

shp = gpd.read_file("data/vnshp/cantho.shp")
gdf = shp.to_crs({'init': 'epsg:4326'}) 
can = []
for index, row in gdf.iterrows():
    for pt in list(row['geometry'].exterior.coords): 
        can.append(list(pt))

shp = gpd.read_file("data/vnshp/danang.shp")
gdf = shp.to_crs({'init': 'epsg:4326'}) 
danang = []
for index, row in gdf.iterrows():
    for pt in list(row['geometry'].exterior.coords): 
        danang.append(list(pt))

shp = gpd.read_file("data/vnshp/hanoi.shp")
gdf = shp.to_crs({'init': 'epsg:4326'}) 
hanoi = []
for index, row in gdf.iterrows():
    for pt in list(row['geometry'].exterior.coords): 
        hanoi.append(list(pt))
shp = gpd.read_file("data/vnshp/hochiminh.shp")
gdf = shp.to_crs({'init': 'epsg:4326'}) 
hcm = []
for index, row in gdf.iterrows():
    for pt in list(row['geometry'].exterior.coords): 
        hcm.append(list(pt))
shp = gpd.read_file("data/vnshp/hue.shp")
gdf = shp.to_crs({'init': 'epsg:4326'}) 
hue = []
for index, row in gdf.iterrows():
    for pt in list(row['geometry'].exterior.coords): 
        hue.append(list(pt))

vnm_rois = {
    "Can Tho city":Polygon (can),
    "Da Nang city": Polygon(  danang  ),
    "Ha Noi city": Polygon(  hanoi  ),
    "Ho  Chi Minh city": Polygon(  hcm  ),
    "Hue": Polygon(  hue  ),

}