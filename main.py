import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Add a header to the Streamlit app
st.title("Pelancongan")  # This creates a title at the top of the page

# Read data from the given URL
try:
    df = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAP.csv')

    # Filter data for 2023
    df_2023 = df[df['Tahun'] == 2023]

    # Grouped bar chart
    plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']
    subjek_values = df_2023['Subjek'].unique()

    plt.figure(figsize=(12, 6))  # Adjust figure size as needed

    x = range(len(subjek_values))
    width = 0.15

    for i, plo in enumerate(plo_columns):
        plt.bar([val + i * width for val in x], df_2023.groupby('Subjek')[plo].sum(), width, label=plo)

    plt.xlabel("Subjek")
    plt.ylabel("Value")
    plt.title("PLO Analysis for 2023")
    plt.xticks([val + width for val in x], subjek_values, rotation=45, ha='right')  # Rotates labels for better visibility
    plt.legend(loc="upper right", bbox_to_anchor=(1.1, 1))  # Moves legend outside the chart

    # Display the plot using Streamlit
    st.pyplot(plt)

except FileNotFoundError:
    st.error("Error: 'PLO Analysis' not found. Please upload the file to your current working directory or provide the correct path.")
except Exception as e:
    st.error(f"An error occurred: {e}")





