import streamlit as st
import requests

st.title("🇸🇬 Singapore 7-Day Weather Forecast")
st.write("A simple app to check the week's weather!")

# Open-Meteo API URL for Singapore's 7-day forecast
# We are using coordinates for Singapore (Latitude: 1.3521, Longitude: 103.8198)
url = "https://api.open-meteo.com/v1/forecast?latitude=1.3521&longitude=103.8198&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Asia%2FSingapore"

if st.button("Get Forecast"):
    with st.spinner("Fetching data from the API..."):
        response = requests.get(url)
        data = response.json()
        
        if "daily" in data:
            daily_data = data["daily"]
            dates = daily_data["time"]
            max_temps = daily_data["temperature_2m_max"]
            min_temps = daily_data["temperature_2m_min"]
            precip = daily_data["precipitation_sum"]
            
            st.success("Forecast retrieved successfully!")
            
            # Loop through the days and display the forecast using expanders
            for i in range(len(dates)):
                with st.expander(f"📅 {dates[i]}"):
                    st.write(f"**High:** {max_temps[i]} °C")
                    st.write(f"**Low:** {min_temps[i]} °C")
                    st.write(f"**Precipitation:** {precip[i]} mm")
        else:
            st.error("Could not fetch the forecast.")