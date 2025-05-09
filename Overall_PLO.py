import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Set the title of the Streamlit app
st.title("PLO Average Performance for Subjects")

# Example: Assuming you have your dataframe `df` already loaded
# Replace this with actual data loading code if necessary, e.g., from a CSV or database
# df = pd.read_csv('your_data.csv') 

# Define PLO columns
plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']

# Calculate the average value of each PLO across all subjects
plo_averages = df[plo_columns].mean()  # This calculates the mean of each PLO across all subjects

# Create an interactive bar chart using Plotly
fig = go.Figure(data=[go.Bar(
    x=plo_averages.index, 
    y=plo_averages.values, 
    text=plo_averages.values,  # Display the value on hover
    textposition='outside',  # Position the text outside the bar
    hoverinfo='text',  # Show text on hover
)])

# Set labels and title for the chart
fig.update_layout(
    title="Average Value for Each PLO across all subjects",
    xaxis_title="PLO",
    yaxis_title="Average Value",
    xaxis=dict(tickmode='array', tickvals=plo_averages.index),
    margin=dict(r=100),  # Add space for the legend
)

# Display the Plotly chart using Streamlit
st.plotly_chart(fig)

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
