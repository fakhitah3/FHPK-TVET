import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Set the title of the Streamlit app
st.title("Industri Count by Year")

# Load the CSV file from the provided URL
try:
    df_industri = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/Industri.csv', on_bad_lines='skip')
    
    # Group by 'TAHUN' and count the number of 'INDUSTRI'
    industri_counts = df_industri.groupby('TAHUN')['INDUSTRI'].count()
    # Create the bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(industri_counts.index, industri_counts.values)

    # Set labels and title
    plt.xlabel("Tahun")
    plt.ylabel("Bilangan Industri")
    plt.title("Bilangan Industri Tahunan")

    # Customize x-axis ticks to show only 2022, 2023, 2024
    plt.xticks([2022, 2023, 2024])
    
    # Display the plot using Streamlit
    st.pyplot(plt)
    
    pelajar_counts = df_industri.groupby('TAHUN')['JUMLAH PELAJAR'].count()

    # Create the bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(industri_counts.index, industri_counts.values)

    # Set labels and title
    plt.xlabel("Tahun")
    plt.ylabel("Bilangan Industri")
    plt.title("Bilangan Industri Tahunan")

    # Customize x-axis ticks to show only 2022, 2023, 2024
    plt.xticks([2022, 2023, 2024])
    
    # Display the plot using Streamlit
    st.pyplot(plt)

except FileNotFoundError:
    st.error("Error: 'Industri.csv' file not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")
