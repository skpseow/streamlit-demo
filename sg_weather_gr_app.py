import streamlit as st
import requests
from datetime import datetime
import plotly.graph_objects as go

st.title("🇸🇬 Singapore Weather Explorer")
st.write("Choose how you want to view the week's forecast!")

# Sub-goal 1: Capture the user's preferred view
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
                        
            # Sub-goal 3b: Render the Custom Graph View
            elif view_choice == "Temperature Trend Graph":
                st.subheader("Temperature Trend")
                
                # Convert dates and format them strictly as "Month Day" (e.g., "Jul 06")
                # This ensures the graph axis only shows the date, never the time.
                proper_dates = []
                for d in dates_text:
                    real_date = datetime.strptime(d, "%Y-%m-%d")
                    clean_date_string = real_date.strftime("%b %d")
                    proper_dates.append(clean_date_string)
                
                # Sub-goal 4: Build the custom Plotly chart
                fig = go.Figure()
                
                # Add the High temperature line (Red with circle markers)
                fig.add_trace(go.Scatter(
                    x=proper_dates, 
                    y=max_temps, 
                    mode='lines+markers',
                    name='High (°C)',
                    line=dict(color='red'),
                    marker=dict(symbol='circle', size=8)
                ))
                
                # Add the Low temperature line (Dark red with circle markers)
                fig.add_trace(go.Scatter(
                    x=proper_dates, 
                    y=min_temps, 
                    mode='lines+markers',
                    name='Low (°C)',
                    line=dict(color='darkred'),
                    marker=dict(symbol='circle', size=8)
                ))
                
                # Render the chart in Streamlit
                st.plotly_chart(fig)
                
        else:
            st.error("Could not fetch the forecast.")