import streamlit as st
import pandas as pd
import numpy as np
import requests

# API key for OpenWeatherMap
API_KEY = '8JCD3BEXPXXSN9AYRB6JDS3KG'

# Function to fetch weather data
def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and 'main' in data:
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure']
        }
    else:
        return None

# Set page title and layout
st.set_page_config(page_title="Health Tracker App", layout="wide")

# Title and introduction
st.title("Health Tracker App")
st.write("Track your daily health metrics and monitor your progress.")

# Sidebar content
st.sidebar.subheader("Daily Health Tips")
tips = [
    "Drink at least 8 glasses of water a day.",
    "Exercise for at least 30 minutes.",
    "Get 7-9 hours of sleep."
]
st.sidebar.write(np.random.choice(tips))

st.sidebar.subheader("User Feedback")
feedback = st.sidebar.text_area("Share your feedback or suggestions:")
if st.sidebar.button("Submit Feedback"):
    st.sidebar.write("Thank you for your feedback!")

# User input for city
city = st.text_input("Enter your city:", "London")

# Fetch weather data
weather_data = get_weather_data(city)

if weather_data:
    # Display weather data
    st.subheader(f"Weather in {city}")
    st.write(f"Temperature: {weather_data['temperature']} °C")
    st.write(f"Humidity: {weather_data['humidity']} %")
    st.write(f"Pressure: {weather_data['pressure']} hPa")
else:
    st.error("Could not fetch weather data. Please check the city name or try again later.")

# Mock health data representing API response
data = {
    "date": pd.date_range(start="2023-01-01", periods=10),
    "water_intake": np.random.randint(1, 4, size=10),
    "calories_burned": np.random.randint(1500, 2500, size=10),
    "hours_slept": np.random.uniform(6, 9, size=10)
}
df = pd.DataFrame(data)

# Interactive table
st.subheader("Daily Health Metrics")
st.dataframe(df)

# Chart elements
st.subheader("Water Intake Over Time")
st.line_chart(df.set_index("date")["water_intake"])

st.subheader("Calories Burned Over Time")
st.area_chart(df.set_index("date")["calories_burned"])

st.subheader("Hours Slept Over Time")
st.bar_chart(df.set_index("date")["hours_slept"])

# Map with points (mock data)
st.subheader("Health Activity Locations")
map_data = pd.DataFrame({
    'lat': np.random.uniform(-90, 90, size=10),
    'lon': np.random.uniform(-180, 180, size=10)
})
st.map(map_data)

# Button widget
if st.button("Refresh Data"):
    st.write("Data refreshed!")

# Checkbox widget
if st.checkbox("Show Raw Data"):
    st.write(df)

# Feedback and messages boxes
st.success("Data loaded successfully!")
st.info("This app helps you track your health metrics.")
st.warning("Make sure to input accurate data.")
st.error("An error occurred while loading data.")

# Additional widgets
st.radio("Choose a metric to display:", ["Water Intake", "Calories Burned", "Hours Slept"])
st.selectbox("Select a date range:", df["date"].astype(str))
st.multiselect("Select metrics to compare:", df.columns[1:])
st.slider("Select a value range for water intake:", 1, 4)
st.text_input("Enter a comment:")
