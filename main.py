from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
from constants import map_width, map_height
from streamlit_lottie import st_lottie
import streamlit as st

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
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 5px;">
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





# Map here
with st.container():
    config = {
        "version": "v1",
        "config": {
            "mapState": {
                "bearing": 0,
                "latitude": 50.4501,  # Default latitude (Berlin, for example)
                "longitude":  30.5234,  # Default longitude (Berlin, for example)
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

# -------------------------------------


with st.sidebar:
    city_name = st.text_input(
        label="Search for your location",
        placeholder="City"
    )

    # Create a button to update the map
    if st.button("Update Map"):
        if city_name:
            try:
                location = geolocator.geocode(city_name)
                if location:
                    map_1.config["config"]["mapState"]["latitude"] = location.latitude
                    map_1.config["config"]["mapState"]["longitude"] = location.longitude
                    st.write(f"Map updated for {city_name}: Lat {location.latitude}, Lon {location.longitude}")
                else:
                    st.write("City not found. Please try another city.")
            except Exception as e:
                st.write(f"An error occurred: {e}")

    st_lottie("https://lottie.host/9e9250cc-836c-474e-a4e9-341c417ec652/XJGAWkauNG.json", key="lottie_animation")

#openai.api_key = st.secrets["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"]
