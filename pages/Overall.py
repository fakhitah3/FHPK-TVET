import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot_plo_sums(df):
    """Plots the sum of values for each PLO across subjects."""

    plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']  # Define PLO columns
    plo_sums = df.groupby('Subjek')[plo_columns].sum().sum()  # Sum for all subjek

    plt.figure(figsize=(10, 6))
    plt.bar(plo_sums.index, plo_sums.values)
    plt.xlabel("PLO")
    plt.ylabel("Total Value")
    plt.title("Total Value for Each PLO across all subjects")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    st.pyplot(plt)  # Display the plot using Streamlit

# Add a header to the Streamlit app
st.title("PLO Sum Visualization")

# URLs of your CSV files
file_urls = [
    'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAH.csv',
    'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAS.csv',
    'https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAP.csv'
    # Add more file URLs as needed
]

all_data = []

# Reading the data from CSV files
for url in file_urls:
    try:
        df = pd.read_csv(url)
        all_data.append(df)
    except FileNotFoundError:
        st.error(f"Error: File at {url} not found.")
    except Exception as e:
        st.error(f"An error occurred while reading {url}: {e}")

# Concatenate all dataframes if they are valid
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    plot_plo_sums(combined_df)  # Call the function to create the visualization
else:
    st.error("No valid dataframes to process.")
