from shapely.geometry import Polygon
import geopandas as gpd
# Load shp files
# shp = gpd.read_file("data/nzshp/Canterbury.shp")
# gdf = shp.to_crs({'init': 'epsg:4326'}) 
# can = []
# for index, row in gdf.iterrows():
#     for pt in list(row['geometry'].exterior.coords): 
#         can.append(list(pt))

# shp = gpd.read_file("data/nzshp/Mitimiti.shp")
# gdf = shp.to_crs({'init': 'epsg:4326'}) 
# Mitimiti = []
# for index, row in gdf.iterrows():
#     for pt in list(row['geometry'].exterior.coords): 
#         Mitimiti.append(list(pt))

# shp = gpd.read_file("data/nzshp/Urewera.shp")
# gdf = shp.to_crs({'init': 'epsg:4326'}) 
# Urewera = []
# for index, row in gdf.iterrows():
#     for pt in list(row['geometry'].exterior.coords): 
#         Urewera.append(list(pt))

# nz_rois = {
#     "Canterbury":Polygon (can),
#     "Mitimiti": Polygon(  Mitimiti  ),
#     "Te Urewera": Polygon(  Urewera  ),

# }

# Load VN

# shp = gpd.read_file("data/vnshp/cantho.shp")
# gdf = shp.to_crs({'init': 'epsg:4326'}) 
# can = []
# for index, row in gdf.iterrows():
#     for pt in list(row['geometry'].exterior.coords): 
#         can.append(list(pt))

# shp = gpd.read_file("data/vnshp/danang.shp")
# gdf = shp.to_crs({'init': 'epsg:4326'}) 
# danang = []
# for index, row in gdf.iterrows():
#     for pt in list(row['geometry'].exterior.coords): 
#         danang.append(list(pt))

# shp = gpd.read_file("data/vnshp/hanoi.shp")
# gdf = shp.to_crs({'init': 'epsg:4326'}) 
# hanoi = []
# for index, row in gdf.iterrows():
#     for pt in list(row['geometry'].exterior.coords): 
#         hanoi.append(list(pt))
# shp = gpd.read_file("data/vnshp/hochiminh.shp")
# gdf = shp.to_crs({'init': 'epsg:4326'}) 
# hcm = []
# for index, row in gdf.iterrows():
#     for pt in list(row['geometry'].exterior.coords): 
#         hcm.append(list(pt))
# shp = gpd.read_file("data/vnshp/hue.shp")
# gdf = shp.to_crs({'init': 'epsg:4326'}) 
# hue = []
# for index, row in gdf.iterrows():
#     for pt in list(row['geometry'].exterior.coords): 
#         hue.append(list(pt))

# import geopandas as gpd

def extract_exterior_coords(file_path):
    shp = gpd.read_file(file_path)
    gdf = shp.to_crs('epsg:4326')
    exterior_coords = []
    for index, row in gdf.iterrows():
        if row['geometry'].geom_type == 'Polygon':
            for pt in list(row['geometry'].exterior.coords):
                exterior_coords.append(list(pt))
        elif row['geometry'].geom_type == 'MultiPolygon':
            for polygon in row['geometry'].geoms:
                for pt in list(polygon.exterior.coords):
                    exterior_coords.append(list(pt))
    return exterior_coords

# Vietnam
cantho = extract_exterior_coords("data/vnshp/cantho.shp")
danang = extract_exterior_coords("data/vnshp/danang.shp")
hanoi = extract_exterior_coords("data/vnshp/hanoi.shp")
hcm = extract_exterior_coords("data/vnshp/hochiminh.shp")
hue = extract_exterior_coords("data/vnshp/hue.shp")


vnm_rois = {
    "Can Tho city":Polygon (cantho),
    "Da Nang city": Polygon(  danang  ),
    "Ha Noi city": Polygon(  hanoi  ),
    "Ho  Chi Minh city": Polygon(  hcm  ),
    "Hue": Polygon(  hue  ),

}

# NZ
auck = extract_exterior_coords("data/nzshp/auck.shp")
chch = extract_exterior_coords("data/nzshp/chch.shp")
dun = extract_exterior_coords("data/nzshp/dun.shp")
welly = extract_exterior_coords("data/nzshp/welly.shp")

nz_rois = {
    "Auckland":Polygon (auck),
    "Christchurch": Polygon(  chch  ),
    "Dunedin": Polygon(dun),
    "Wellington": Polygon(welly),

}
