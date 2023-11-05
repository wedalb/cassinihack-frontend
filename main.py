from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from constants import map_width, map_height
from streamlit_lottie import st_lottie
import streamlit as st
import streamlit.components.v1 as components
from keplergl import KeplerGl
import pandas as pd
import numpy as np
import pydeck as pdk

import pandas as pd
import pydeck as pdk


st.set_page_config(
    page_title="Concast",
    page_icon="❇️",
    layout="wide"
)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
# Add a smaller header with a wider shape, smaller "Concast" text, and smaller overlapping rectangular shape with 50% opacity
header_html = """
    <style>
        .cool-shape {
            width: 40px;
            height: 30px;
            background: linear-gradient(45deg, #1B8A62, #2FB384);
            border-radius: 0 0 50% 50%;
            clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
        }
        .profile-menu {
            position: absolute;
            top: 30px;
            left: -60px;
            opacity: 0;
            visibility: hidden;
            background: white;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
            border-radius: 5px;
            padding: 10px;
            transition: opacity 0.2s, visibility 0.2s;
        }
        .profile-menu:hover {
            opacity: 1;
            visibility: visible;
        }
        .menu-item {
            cursor: pointer;
            padding: 5px;
        }
        .menu-item.logout {
            color: red;
        }
    </style>
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 5px 5px;">
        <div style="display: flex; align-items: center; position: relative;">
            <div class="cool-shape"></div>
            <div class="overlay-shape"></div>
            <h2 style="margin-left: 10px; font-size: 20px; display: inline-block; vertical-align: middle;">ConCast</h2>
        </div>
        <div style="width: 30px; height: 30px; border-radius: 50%; background: linear-gradient(45deg, #1B8A62, #2FB384); display: flex; justify-content: center; align-items: center;">
        </div>
    </div>
"""

st.markdown(header_html, unsafe_allow_html=True)



#------------------------------------------------------------------------------------------------------------------------
chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [50.4501, 30.5234],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=50.4501,
        longitude=30.5234,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

#------------------------------------------------------------------------------------------------------------------------


# Map here
#with st.container():
#    config = {
#       "version": "v1",
#        "config": {
#           "mapState": {
#               "bearing": 0,
#               "latitude": 50.4501,  # Default latitude (Berlin, for example)
#               "longitude":  30.5234,  # Default longitude (Berlin, for example)
#               "pitch": 0,
#               "zoom": 12,
##           }
#      },
#   }
#   map_1 = KeplerGl(
#       height=map_height,
#       width=map_width)
#   map_1.config = config
#   keplergl_static(map_1)

#SLIDER
st.markdown("""
<style>
    .stSlider {
        padding-top: 0px; 
        padding-bottom: 0px; 
        padding-right: 30px; 
        padding-left: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Select year here:
selected_year = st.slider(
    label="Please choose a year",
    value=2023,
    min_value=2019,
    max_value=2050,
    step=1,
    label_visibility="collapsed")

# ---------------------------------------------------------------------------------------------------------------
button_style = """
<style>
    .custom-button {
        color: white; /* Change font color to black */
        font-size: 16px; /* Change font size to 16px */
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s, transform 0.1s;
        border-radius: 10px;
        font-family: 'Montserrat', sans-serif; /* Change font family to Montserrat */
    }
    .custom-button.war {
        background-color: #256345;

    }
    .custom-button.disaster {
        background-color: #3b6b5d;
    }
    .custom-button.drought {
        background-color: #225c49;
    }
    .custom-button:hover {
        background-color: #26926B;
    }
    .custom-button:active {
        transform: scale(0.95);
    }
</style>
"""




with st.sidebar:
    city_name = st.text_input(
        label="Search for your location",
        placeholder="City"
    )
    col1, col2 = st.columns(2)
    with col2:
        # Create a button to update the map
        st.button("Update Map")


    st_lottie("https://lottie.host/7ca66b6f-e37e-43bd-b6f9-a559c7beef10/LI5QEy8pgB.json")

    # Inject button styles to Streamlit
    st.markdown(button_style, unsafe_allow_html=True)

    st.caption("Make predictions about the future population under different scenarios")

    # Create buttons
    st.markdown('<button class="custom-button war">What happens in an event of war?</button>', unsafe_allow_html=True)
    st.markdown('<button class="custom-button disaster">What happens during natural disaster?</button>', unsafe_allow_html=True)
    st.markdown('<button class="custom-button drought">What effects does climate change have?</button>', unsafe_allow_html=True)

#openai.api_key = st.secrets["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"]
