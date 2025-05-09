import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go

import streamlit as st

# Set the title of the Streamlit app
#st.title("Program Apprentice 3u1i@FHPK")


st.title("Jumlah PLO Keseluruhan")
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

# Combine all dataframes into one DataFrame if they are valid
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Define PLO columns
    plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']

    # Calculate the average value of each PLO across all subjects
    plo_averages = combined_df[plo_columns].mean()  # This calculates the mean of each PLO across all subjects

    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(label="PLO 2", value=f"{plo_averages ['PLO 2']:.2f}", help="PLO 2: Cognitive Skill", border=True)
    col2.metric(label="PLO 3", value=f"{plo_averages ['PLO 3']:.2f}", help="PLO 3: Digital Skill", border=True)
    col3.metric(label="PLO 4", value=f"{plo_averages ['PLO 4']:.2f}", help="PLO 4: Interpersonal Skill", border=True)
    col4.metric(label="PLO 5", value=f"{plo_averages ['PLO 5']:.2f}", help="PLO 5: Communication Skill", border=True)
      

    # Create an interactive bar chart using Plotly
    fig = go.Figure(data=[go.Bar(
        x=plo_averages.index, 
        y=plo_averages.values, 
        hovertemplate='%{y:.2f}',  # Show text on hover
    )])

    # Set labels and title for the chart
    fig.update_layout(
        #title="Average Value for Each PLO across all subjects",
        xaxis_title="PLO",
        yaxis_title="Nilai",
        xaxis=dict(tickmode='array', tickvals=plo_averages.index),
        margin=dict(r=100),  # Add space for the legend
    )

    # Display the Plotly chart using Streamlit
    st.plotly_chart(fig)
else:
    st.error("No valid dataframes to process.")
    

st.subheader("Nama Program:")
st.markdown("""
**PROGRAM PENGAJIAN MOD INDUSTRI**
- Ijazah Sarjana Muda Keusahawanan (Hospitaliti) dengan kepujian (Mod Industri) / MQA/FA4821
- Ijazah Sarjana Muda Keusahawanan (Pelancongan) dengan kepujian (Mod Industri) / MQA/FA4832
- Ijazah Sarjana Muda Keusahawanan (Kesejahteraan) dengan kepujian (Mod Industri) / MQA/FA4822
""")

# Display academic program details
st.subheader("Tahun Pengajian:")
st.write("3 tahun di universiti, 1 tahun di industri (3u1i)")

st.subheader("Tahun Pertama Penawaran Program:")
st.write("2021")


tab1, tab2, tab3 = st.tabs(["Hospitaliti", "Pelancongan", "Kesejahteraan"])


with tab1:
    try:
      dx = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAH.csv')
      print(dx.head()) # Print the first few rows to verify
    except FileNotFoundError:
      print("Error: File not found. Please upload the file to your current working directory or provide the correct path.")
    except Exception as e:
      print(f"An error occurred: {e}")
    
    # Create a dropdown menu for year selection
    year_selectionSAH = st.selectbox("Select Year", ["2022", "2023", "2024"])
    
    # Filter data based on the selected year
    dx_filtered = dx[dx['Tahun'] == int(year_selectionSAH)]
    
    # Grouped bar chart
    plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']
    subjects = dx_filtered['Subjek'].unique()
    
    width = 0.15
    x = range(len(subjects))
    
    # Now, calculate the total sum for each PLO and display them as metrics
    plo_sums = dx_filtered[plo_columns].sum()/4
    
    # Use Streamlit's columns to display metrics in one line
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(label="PLO 2", value=f"{plo_sums['PLO 2']:.2f}", help="PLO 2: Cognitive Skill", border=True)
    col2.metric(label="PLO 3", value=f"{plo_sums['PLO 3']:.2f}", help="PLO 3: Digital Skill", border=True)
    col3.metric(label="PLO 4", value=f"{plo_sums['PLO 4']:.2f}", help="PLO 4: Interpersonal Skill", border=True)
    col4.metric(label="PLO 5", value=f"{plo_sums['PLO 5']:.2f}", help="PLO 5: Communication Skill", border=True)
    
    
    width = 0.15
    x = range(len(subjects))
    
    # Create the plot
    fig_SAH = go.Figure()
    
    # Add each PLO as a separate trace (bar group)
    for i, plo in enumerate(plo_columns):
        values = dx_filtered.groupby('Subjek')[plo].sum()
        fig_SAH.add_trace(go.Bar(
            x=[val + i * width for val in x],
            y=values,
            name=plo,
            # text=values,  # Display the value on hover
            # textposition='outside',  # Position the text outside the bar
            hoverinfo='y',  # Show text on hover
        ))
    
    # Update layout to set axis labels and chart title
    fig_SAH.update_layout(
        title=f"Prestasi PLO bagi Tahun {year_selectionSAH}",
        xaxis_title="Subjek",
        yaxis_title="Nilai",
        xaxis=dict(
            tickmode='array',
            tickvals=[val + width for val in x],
            ticktext=subjects,
        ),
        barmode='group',  # Display the bars in a grouped manner
        legend=dict(x=1.05, y=1),  # Move legend outside the chart
        margin=dict(r=100),  # Add margin for the legend
    )
    
    # Display the Plotly chart using Streamlit
    st.plotly_chart(fig_SAH, use_container_width=True, key="SAH_plot")

with tab2:
    try:
      df = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAP.csv')
      print(df.head()) # Print the first few rows to verify
    except FileNotFoundError:
      print("Error: File not found. Please upload the file to your current working directory or provide the correct path.")
    except Exception as e:
      print(f"An error occurred: {e}")
    
    # Create a dropdown menu for year selection
    year_selectionSAP = st.selectbox("Select Year", ["2023", "2024"])
    
    # Filter data based on the selected year
    df_filtered = df[df['Tahun'] == int(year_selectionSAP)]
    
    # Grouped bar chart
    plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']
    subjects = df_filtered['Subjek'].unique()
    
    width = 0.15
    x = range(len(subjects))
    
    # Now, calculate the total sum for each PLO and display them as metrics
    plo_sums = df_filtered[plo_columns].sum()/4
    
    # Use Streamlit's columns to display metrics in one line
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(label="PLO 2", value=f"{plo_sums['PLO 2']:.2f}", help="PLO 2: Cognitive Skill", border=True)
    col2.metric(label="PLO 3", value=f"{plo_sums['PLO 3']:.2f}", help="PLO 3: Digital Skill", border=True)
    col3.metric(label="PLO 4", value=f"{plo_sums['PLO 4']:.2f}", help="PLO 4: Interpersonal Skill", border=True)
    col4.metric(label="PLO 5", value=f"{plo_sums['PLO 5']:.2f}", help="PLO 5: Communication Skill", border=True)
      
    # Create the plot
    fig_SAP = go.Figure()
    
    # Add each PLO as a separate trace (bar group)
    for i, plo in enumerate(plo_columns):
        values = df_filtered.groupby('Subjek')[plo].sum()
        fig_SAP.add_trace(go.Bar(
            x=[val + i * width for val in x],
            y=values,
            name=plo,
            # text=values,  # Display the value on hover
            # textposition='outside',  # Position the text outside the bar
            hoverinfo='y',  # Show text on hover
        ))
    
    # Update layout to set axis labels and chart title
    fig_SAP.update_layout(
        title=f"Prestasi PLO bagi Tahun {year_selectionSAP}",
        xaxis_title="Subjek",
        yaxis_title="Nilai",
        xaxis=dict(
            tickmode='array',
            tickvals=[val + width for val in x],
            ticktext=subjects,
        ),
        barmode='group',  # Display the bars in a grouped manner
        legend=dict(x=1.05, y=1),  # Move legend outside the chart
        margin=dict(r=100),  # Add margin for the legend
    )
    
    # Display the Plotly chart using Streamlit
    st.plotly_chart(fig_SAP, use_container_width=True, key="SAP_plot")

with tab3:
    try:
      dy = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAS.csv')
      print(dy.head()) # Print the first few rows to verify
    except FileNotFoundError:
      print("Error: File not found. Please upload the file to your current working directory or provide the correct path.")
    except Exception as e:
      print(f"An error occurred: {e}")
    
    
    # Create a dropdown menu for year selection
    year_selectionSAS = st.selectbox("Select Year", ["2023", "2024"], key="year_dropdown")
    
    # Filter data based on the selected year
    dy_filtered = dy[dy['Tahun'] == int(year_selectionSAS)]
    
    # Grouped bar chart
    plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']
    subjects = dy_filtered['Subjek'].unique()
    
    
    width = 0.15
    x = range(len(subjects))
    
    # Now, calculate the total sum for each PLO and display them as metrics
    plo_sums = dy_filtered[plo_columns].sum()/4
    
    # Use Streamlit's columns to display metrics in one line
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(label="PLO 2", value=f"{plo_sums['PLO 2']:.2f}", help="PLO 2: Cognitive Skill", border=True)
    col2.metric(label="PLO 3", value=f"{plo_sums['PLO 3']:.2f}", help="PLO 3: Digital Skill", border=True)
    col3.metric(label="PLO 4", value=f"{plo_sums['PLO 4']:.2f}", help="PLO 4: Interpersonal Skill", border=True)
    col4.metric(label="PLO 5", value=f"{plo_sums['PLO 5']:.2f}", help="PLO 5: Communication Skill", border=True)
      
      
    width = 0.15
    x = range(len(subjects))
    
    # Create the plot
    fig_SAS = go.Figure()
    
    # Add each PLO as a separate trace (bar group)
    for i, plo in enumerate(plo_columns):
        values = dy_filtered.groupby('Subjek')[plo].sum()
        fig_SAS.add_trace(go.Bar(
            x=[val + i * width for val in x],
            y=values,
            name=plo,
            # text=values,  # Display the value on hover
            # textposition='outside',  # Position the text outside the bar
            hoverinfo='y',  # Show text on hover
        ))
    
    # Update layout to set axis labels and chart title
    fig_SAS.update_layout(
        title=f"Prestasi PLO bagi Tahun {year_selectionSAS}",
        xaxis_title="Subjek",
        yaxis_title="Nilai",
        xaxis=dict(
            tickmode='array',
            tickvals=[val + width for val in x],
            ticktext=subjects,
        ),
        barmode='group',  # Display the bars in a grouped manner
        legend=dict(x=1.05, y=1),  # Move legend outside the chart
        margin=dict(r=100),  # Add margin for the legend
    )
    
    # Display the Plotly chart using Streamlit
    st.plotly_chart(fig_SAS, use_container_width=True, key="SAS_plot")
