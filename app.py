
import ee
import os
import warnings
import datetime
import fiona
import geopandas as gpd
import folium
import streamlit as st
import geemap.colormaps as cm
import geemap.foliumap as geemap
from datetime import date
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
# import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.sidebar.title("About")
service_account =  "ofv-99@ee-ofv.iam.gserviceaccount.com"
private_key = st.secrets["EARTHENGINE_TOKEN"]
credentials = ee.ServiceAccountCredentials(
    service_account, key_data=private_key
)

ee.Initialize(credentials)
Map = geemap.Map(
    basemap="HYBRID",
    plugin_Draw=True,
    Draw_export=True,
    # locate_control=True,
    plugin_LatLngPopup=False, center=(-43.525650, 172.639847), zoom=6.25,
)
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

# st.info("Click on the left sidebar menu to navigate to the different apps.")

st.subheader("Timelapse of Satellite Imagery")
st.markdown(
    """
    The following timelapse animations for three areas.
"""
)
Map.addLayerControl()
Map.to_streamlit(height=600)
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