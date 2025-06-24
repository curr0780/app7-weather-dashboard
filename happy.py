import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")

st.title("In Search of Happiness")

x_data_label = st.selectbox("Select the data for the x-axis",
                            ("GDP", "Happiness", "Generosity"))
y_data_label = st.selectbox("Select the data for the y-axis",
                      ("GDP", "Happiness", "Generosity"))

print(f"x_data_label, type = {x_data_label}, {type(x_data_label)}")
print(f"y_data_label, type = {y_data_label}, {type(y_data_label)}")

st.subheader(f"{x_data_label} and {y_data_label}")

# def get_data(x, y):
#     x_data_loc = df[x]
#     y_data_loc = df[y]
#     return x_data_loc, y_data_loc

x_data, y_data = df[x_data_label.lower()], df[y_data_label.lower()]

figure = px.scatter(x=x_data, y=y_data, labels={"x": x_data_label, "y": y_data_label})
st.plotly_chart(figure)