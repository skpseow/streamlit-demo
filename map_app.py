import streamlit as st

st.title("🌍 Exploring Cities on a Map")
st.write("Select a city to see it on the map!")

# Dictionary of cities containing coordinate dictionaries
city_data = {
    "New York": {"lat": 40.7128, "lon": -74.0060},
    "London": {"lat": 51.5074, "lon": -0.1278},
    "Tokyo": {"lat": 35.6895, "lon": 139.6917},
    "Sydney": {"lat": -33.8688, "lon": 151.2093},
    "Singapore": {"lat": 1.3521, "lon": 103.8198},
    "Bangkok": {"lat": 13.7563, "lon": 100.5018},
    "Hanoi": {"lat": 21.0285, "lon": 105.8542}
}

# User selects a city from a dropdown
selected_city = st.selectbox("Choose a city:", list(city_data.keys()))

# Retrieve the dictionary for the chosen city
coords = city_data[selected_city]

# st.map expects a list containing dictionary items with 'lat' and 'lon' keys
map_data = [coords]

st.write(f"### Currently viewing: {selected_city}")

# Display the map
st.map(map_data, zoom=10)
