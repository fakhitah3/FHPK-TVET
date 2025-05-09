import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st

# Set the title of the Streamlit app
st.title("Bilangan Industri Terlibat")

# Load the CSV file from the provided URL
try:
    df_industri = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/Industri.csv', on_bad_lines='skip')
    
    # Remove duplicates based on 'INDUSTRI' column and group by 'TAHUN' to count unique 'INDUSTRI'
    unique_industri = df_industri.drop_duplicates(subset=['INDUSTRI'])

    # Group by 'TAHUN' and count the number of unique 'INDUSTRI'
    industri_counts = unique_industri.groupby('TAHUN')['INDUSTRI'].count()
    
    # Create an interactive bar chart using Plotly
    fig_Ind = go.Figure(data=[go.Bar(
        x=industri_counts.index,
        y=industri_counts.values,
        #text=industri_counts.values,  # Hover text
        #textposition='outside',  # Position the text outside the bar
        hoverinfo='y',  # Show text on hover
    )])

    # Set the chart title and axis labels
    fig_Ind.update_layout(
        #title="Bilangan Industri yang Terlibat",
        xaxis_title="Tahun",
        yaxis_title="Bilangan Industri",
        xaxis=dict(tickmode='array', tickvals=[2022, 2023, 2024], ticktext=['2022', '2023', '2024']),
    )

    # Display the Plotly figure in Streamlit
    st.plotly_chart(fig_Ind)

    
    # Calculate the overall number of students per year
    total_students_by_year = df_industri.groupby('TAHUN')['JUMLAH PELAJAR'].sum()

    # Create an interactive bar chart for the overall number of students per year
    fig_Std = go.Figure()

    # Add bar for total students per year
    fig_Std.add_trace(go.Bar(
        x=total_students_by_year.index,
        y=total_students_by_year.values,
        name='Total Students',
        text=total_students_by_year.values,  # Show the number of students on hover
        textposition='outside',
        hoverinfo='text',  # Show text on hover
    ))

    # Set the chart title and axis labels
    fig_Std.update_layout(
        title="Total Number of Students Involved by Year",
        xaxis_title="Year",
        yaxis_title="Number of Students",
        xaxis=dict(tickmode='array', tickvals=[2022, 2023, 2024], ticktext=['2022', '2023', '2024']),
        barmode='group'
    )

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig_Std)

    # Interactive click event handling for viewing distribution by SAH, SAP, SAS
    # Adding a callback for showing distribution when clicking on a bar
    selected_year = st.selectbox("Select a Year to View Distribution", [2022, 2023, 2024])

    # Filter the data based on the selected year
    df_filtered = df_industri[df_industri['TAHUN'] == selected_year]

    # Group by KURSUS (SAH, SAP, SAS) and get the sum of students
    kursus_distribution = df_filtered.groupby('KURSUS')['JUMLAH PELAJAR'].sum()

    # Display the distribution for the selected year
    st.write(f"### Taburan Pelajar pada Tahun {selected_year}")
    st.bar_chart(kursus_distribution)  # Bar chart for SAH, SAP, SAS distribution

except FileNotFoundError:
    st.error("Error: 'Industri.csv' file not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")
