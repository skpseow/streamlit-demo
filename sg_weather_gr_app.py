import streamlit as st
import requests
from datetime import datetime

st.title("🇸🇬 Singapore Weather Explorer")
st.write("Choose how you want to view the week's forecast!")

# Sub-goal 1: Capture the user's preferred view
# The radio button returns the exact string the user selects
view_choice = st.radio(
    "Select a view:", 
    ["Daily Details", "Temperature Trend Graph"]
)

url = "https://api.open-meteo.com/v1/forecast?latitude=1.3521&longitude=103.8198&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Asia%2FSingapore"

if st.button("Fetch Weather"):
    with st.spinner("Fetching data from the clouds..."):
        response = requests.get(url)
        data = response.json()
        
        if "daily" in data:
            # Sub-goal 2: Extract the raw data from the JSON
            daily_data = data["daily"]
            dates_text = daily_data["time"]
            max_temps = daily_data["temperature_2m_max"]
            min_temps = daily_data["temperature_2m_min"]
            precip = daily_data["precipitation_sum"]
            
            # Sub-goal 3a: Render the Expander View
            if view_choice == "Daily Details":
                st.subheader("Daily Forecast Details")
                for i in range(len(dates_text)):
                    with st.expander(f"📅 {dates_text[i]}"):
                        st.write(f"**High:** {max_temps[i]} °C")
                        st.write(f"**Low:** {min_temps[i]} °C")
                        st.write(f"**Precipitation:** {precip[i]} mm")
                        
            # Sub-goal 3b: Render the Graph View
            elif view_choice == "Temperature Trend Graph":
                st.subheader("Temperature Trend")
                
                # Convert text dates to real dates for the X-axis
                proper_dates = []
                for d in dates_text:
                    real_date = datetime.strptime(d, "%Y-%m-%d").date()
                    proper_dates.append(real_date)
                
                # Structure the dictionary and plot
                chart_data = {
                    "Date": proper_dates,
                    "High (°C)": max_temps,
                    "Low (°C)": min_temps
                }
                
                st.line_chart(
                    chart_data,
                    x="Date",
                    y=["High (°C)", "Low (°C)"]
                )
                
        else:
            st.error("Could not fetch the forecast.")