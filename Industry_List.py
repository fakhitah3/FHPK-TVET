import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st

# Set the title of the Streamlit app
st.title("Industri Count by Year")

# Load the CSV file from the provided URL
try:
    df_industri = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/Industri.csv', on_bad_lines='skip')
    
    # Group by 'TAHUN' and count the number of 'INDUSTRI'
    industri_counts = df_industri.groupby('TAHUN')['INDUSTRI'].count()
    
    # Create an interactive bar chart using Plotly
    fig = go.Figure(data=[go.Bar(
        x=industri_counts.index,
        y=industri_counts.values,
        text=industri_counts.values,  # Hover text
        textposition='outside',  # Position the text outside the bar
        hoverinfo='text',  # Show text on hover
    )])

    # Set the chart title and axis labels
    fig.update_layout(
        title="Bilangan Industri yang Terlibat",
        xaxis_title="Tahun",
        yaxis_title="Bilangan Industri",
        xaxis=dict(tickmode='array', tickvals=[2022, 2023, 2024], ticktext=['2022', '2023', '2024']),
    )

    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig)

    
    pelajar_counts = df_industri.groupby('TAHUN')['JUMLAH PELAJAR'].count()

    # Create an interactive bar chart using Plotly
    fig = go.Figure(data=[go.Bar(
        x=pelajar_counts.index,
        y=pelajar_counts.values,
        text=pelajar_counts.values,  # Hover text
        textposition='outside',  # Position the text outside the bar
        hoverinfo='text',  # Show text on hover
    )])

    # Set the chart title and axis labels
    fig.update_layout(
        title="Bilangan Pelajar yang Terlibat",
        xaxis_title="Tahun",
        yaxis_title="Bilangan Pelajar",
        xaxis=dict(tickmode='array', tickvals=[2022, 2023, 2024], ticktext=['2022', '2023', '2024']),
    )

    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig)


except FileNotFoundError:
    st.error("Error: 'Industri.csv' file not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")
