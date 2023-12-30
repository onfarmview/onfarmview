
import ee
import geopandas as gpd
import streamlit as st
import geemap.colormaps as cm
import geemap.foliumap as geemap
from datetime import date, timedelta, datetime

st.set_page_config(layout="wide")
st.sidebar.title("About")
st.sidebar.info(
    """
    - Web App URL: https://onfarmview.com/
   
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    admin@onfarmview.com
    """
)

st.title("OnFarmView - Farm Monitoring Tools")

st.markdown(
    """
    An online interactive mapping tool to display basic vegetative metrics available over New Zealand.
    """
)

def maskCloudAndShadows(image):
  cloudProb = image.select('MSK_CLDPRB')
  snowProb = image.select('MSK_SNWPRB')
  cloud = cloudProb.lt(5)
  snow = snowProb.lt(5)
  scl = image.select('SCL')
  shadow = scl.eq(3); # 3 = cloud shadow
  cirrus = scl.eq(10); # 10 = cirrus
  # Cloud probability less than 5% or cloud shadow classification
  mask = (cloud.And(snow)).And(cirrus.neq(1)).And(shadow.neq(1))
  return image.updateMask(mask)
def getNDVI(image): 
    ndvi = image.normalizedDifference(['B8','B4']).rename("NDVI")
    image = image.addBands(ndvi)
    return(image)

def addDate(image):
    img_date = ee.Date(image.date())
    img_date = ee.Number.parse(img_date.format('YYYYMMdd'))
    return image.addBands(ee.Image(img_date).rename('date').toInt())


service_account =  "ofv-99@ee-ofv.iam.gserviceaccount.com"
private_key = st.secrets["EARTHENGINE_TOKEN"]
credentials = ee.ServiceAccountCredentials(
    service_account, key_data=private_key
)
ee.Initialize(credentials)
today = date.today()
default_date_yesterday = today - timedelta(days=1)
sd = st.date_input(
    "Start date", date(2023, 10, 1), min_value= date(2015, 6, 23),
    max_value= today,
    )

ed = st.date_input(
    "End date",
    default_date_yesterday,
    min_value= date(2023, 12, 31),max_value= today)      

start_date = sd.strftime("%Y-%m-%d") + "T" 
end_date = ed.strftime("%Y-%m-%d") + "T" 


Map = geemap.Map(
    basemap="HYBRID",
    plugin_Draw=True,
    Draw_export=True,
    # locate_control=True,
    plugin_LatLngPopup=False, center=(-43.525650, 172.639847), zoom=6.25,
)

filename = "data.geojson"
file = open(filename)
gdf = gpd.read_file(file)
palette = ['FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718', '74A901', '66A000', '529400', '3E8601', '207401', '056201', '004C00', '023B01', '012E01', '011D01', '011301']
vis_params = {
  'min': 0,
  'max': 1,
  'palette': palette}
aoi= geemap.gdf_to_ee(gdf, geodesic=False)    
Map.centerObject(aoi)
NDVI_data = ee.ImageCollection('COPERNICUS/S2_SR').filterDate(start_date, end_date).filterBounds(aoi).filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE",90)).map(maskCloudAndShadows).map(getNDVI).map(addDate).median()
Map.addLayer(NDVI_data.clip(aoi).select('NDVI'), vis_params, "Median of NDVI")    

Map.addLayerControl()
Map.to_streamlit(height=600)

# st.info("Click on the left sidebar menu to navigate to the different apps.")

# st.subheader("Timelapse of Satellite Imagery")
# st.markdown(
#     """
#     The following timelapse animations for three areas.
# """
# )

# row1_col1, row1_col2, row1_col3 = st.columns(3)
# with row1_col1:
#     st.image("data/can.gif")
#     st.markdown("""Canterbury Region""")
    
# with row1_col2:
#     st.image("data/urewera.gif")
#     st.markdown("""Urewera""")
# with row1_col3:
#     st.image("data/mitimiti.gif")
#     st.markdown("""Mitimiti""")