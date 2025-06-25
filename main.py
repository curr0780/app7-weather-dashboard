import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, select box, and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
          "Rain": "images/rain.png", "Snow": "images/snow.png"}

# Get the weather data
if place:
    try:
        filtered_data = get_data(place, days)

        # Create a temperature plot
        if option == "Temperature":
            tempC = [data['main']['temp'] for data in filtered_data]
            tempF = [temp*1.8+32 for temp in tempC]
            dates = [dict['dt_txt'] for dict in filtered_data]
            figure1 = px.line(x=dates, y=tempC, labels={"x": "Date", "y": "Temperature (C)"})
            figure2 = px.line(x=dates, y=tempF, labels={"x": "Date", "y": "Temperature (F)"})
            st.plotly_chart(figure1)
            st.plotly_chart(figure2)

        # Display type fo sky predicted
        if option == "Sky":
            sky_conditions = [data['weather'][0]['main'] for data in filtered_data]
            image_path = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_path, width=115)

    except KeyError:
        st.text("Sorry, I don't know where that place is.")