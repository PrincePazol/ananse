# Import the neccessary libraries for the project
import streamlit as st
from arcgis.gis import GIS
from arcgis.geocoding import geocode
import folium
from streamlit_folium import st_folium
from streamlit_lottie import st_lottie
from geocode import arcgis_geocode, extract_api

# Initialize the App
st.set_page_config(page_title='Ananse', page_icon='🕸️')

# Establish connection with ArcGIS Online
gis = GIS()

# Remove whitespace from the top of the page and sidebar
st.markdown(body="""
              <style>
                    .ea3mdgi5 {
                          padding-top: 1rem;
                          padding-bottom: 10rem;
                          padding-left: 5rem;
                          padding-right: 5rem;
                      }
                    .e1nzilvr4 svg {
                          padding-left: 5rem;
                    }
              </style>
            """, 
        unsafe_allow_html=True)


# Add a Title
st.title(body='🕸️ Kwaku Ananse')

# Add a GIF in the Header
lottie_link = 'https://lottie.host/03c48fea-5c66-4e28-8f0e-92c2e6d14e46/LLUhbU88b3.json'
st_lottie(lottie_link, height=300)

# Add a divider
st.divider()

# Add User Input
user_input = str(st.text_input(label='**🔍 Address Here**', 
                               placeholder='Type Something Here...'
                              )
                )

# Submit API request
api_response = arcgis_geocode(user_address=user_input)

# Extract relevant information from API response
extract_data = extract_api(api_response=api_response)

# Output the result
st.write('Your Address Coordinates')

# Lats and Long values
latitude = extract_data[0]
longitude = extract_data[1]
score = extract_data[-1]

# Create the container
with st.container(border=True):
  # Create three(3) columns
  col1, col2, col3 = st.columns(3)
  # Insert contents in col1, col2, col3
  with col1:
    st.text(body='Latitude')
    # Handle ValueError
    try:
      st.write(f'{latitude:.6f}')
    except ValueError:
      st.info(body='To be Displayed', icon='👻')
  
  with col2:
    st.text(body='Longitude')
    # handle ValueError
    try:
      st.write(f'{longitude:.6f}')
    except ValueError:
      st.info(body='To be Displayed', icon='👻')
    
  with col3:
    st.text(body='Score(1-100)')
    # Handle ValueError
    try:
      st.write(f'{score}')
    except ValueError:
      st.info(body='To be Displayed', icon='👻')
    
# Add a divider
st.divider()

# Add a map
# Handle ValueError
try:
  m = folium.Map(location=[latitude, longitude],
                zoom_start=16
                )
except ValueError:
    st.info(body='Map Display Here', icon='👻')

# Handle Value Error
try:
  # Show the point on the map
  folium.Marker(
                [latitude, longitude],
                popup=user_input,
                tooltip=api_response[0]['address']
               ).add_to(m)
except ValueError:
  pass

# Handle NameError
try:  
  # Display the map
  st_data = st_folium(m, width=600)
except NameError:
  pass
