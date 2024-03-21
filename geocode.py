# Import neccessary libraries
from arcgis.gis import GIS
from arcgis.geocoding import geocode
import streamlit as st

# Establish connection with agol
gis = GIS()

# Submit user request to the agol api
def arcgis_geocode(user_address):
  """
    This function performs geocoding 
    using arcgis api.
  """
  # Handle no user input Error
  if user_address is None:
    st.info(body='Submit Some Address 👻')
  else:
    # Submit the user request
    api_response = geocode(address=user_address)
  # Return the api response
  return api_response

# Extracts relevant information from the api respnse
def extract_api(api_response):
  """
    This function extracts the relevant
    information from the api response.
  """
  # Create empty variables to extract data
  latitude, longitude, addr_type, match, score = '','','','',''
  # Handle no user input related Errors
  try:
    # Extract the latitude, longitude, addr_type, match, and score
    latitude = api_response[0]['attributes']['DisplayY']
    longitude = api_response[0]['attributes']['DisplayX']
    addr_type = api_response[0]['attributes']['Addr_type']
    match = api_response[0]['attributes']['Status']
    score = api_response[0]['attributes']['Score']
  # Gracefully handle Index Error
  except IndexError:
    st.info(body='**👻 Submit Some Address Information**')
  # Return the extract data as tuple
  return (latitude, longitude, addr_type, match, score)