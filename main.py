import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from constants import map_width, map_height
from streamlit_lottie import st_lottie

st.set_page_config(
    page_title="Concast",
    page_icon="💖",
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


# Read the content of the HTML file
#with open("./components/navbar.html", "r") as f:
#    navbar_content = f.read()

# Render the HTML content using components.html
#components.html(navbar_content)

# Map here
with st.container():
    config = {
        "version": "v1",
        "config": {
            "mapState": {
                "bearing": 0,
                "latitude": 50.450001,
                "longitude": 30.523333,
                "pitch": 0,
                "zoom": 12,
            }
        },
    }
    map_1 = KeplerGl(
        height=map_height,
        width=map_width)
    map_1.config = config
    keplergl_static(map_1)

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

with st.sidebar:

    st.text_input(
        label="Search for your location",
        placeholder="City"
    )
    st_lottie("https://lottie.host/9e9250cc-836c-474e-a4e9-341c417ec652/XJGAWkauNG.json")

