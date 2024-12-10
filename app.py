import os
import streamlit as st
import pandas as pd
from utils.visualization import TransportVisualization

# Dynamically locate the dataset paths
base_path = os.path.dirname(os.path.abspath(__file__))
bus_data_path = os.path.join(base_path, "data", "BUS_Dataset.csv")
dart_data_path = os.path.join(base_path, "data", "DART_Dataset.csv")
luas_data_path = os.path.join(base_path, "data", "LUAS_Dataset.csv")


bus_data = pd.read_csv(bus_data_path, encoding="latin1")
dart_data = pd.read_csv(dart_data_path, encoding="latin1")
luas_data = pd.read_csv(luas_data_path, encoding="latin1")

# Initialize the visualization class
visualization = TransportVisualization(bus_data, dart_data, luas_data)

# Streamlit App UI
st.title("Irish Transport System - Data Visualization")

# Sidebar Options
st.sidebar.header("Transport Selection")
transport_option = st.sidebar.selectbox(
    "Select a Transport Type",
    ["DART", "LUAS", "BUS"]
)

# Display graphs for the selected transport type
if transport_option == "BUS":
    st.subheader("BUS Dataset Visualizations")
    visualization.plot_frequency_vs_duration()
    visualization.plot_top_routes_by_landmarks()

elif transport_option == "DART":
    st.subheader("DART Dataset Visualizations")
    visualization.plot_facilities_availability()
    visualization.plot_weekend_operational_stations()
    visualization.plot_routes_serviced_per_station()

elif transport_option == "LUAS":
    st.subheader("LUAS Dataset Visualizations")
    visualization.plot_footfall_by_line()
    visualization.plot_parking_availability()
    visualization.plot_accessibility_comparison()
    visualization.plot_nearby_landmarks()
    visualization.plot_station_zone_relationship()