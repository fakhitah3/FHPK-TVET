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
    # Display the data in a table format
    st.write("### Senarai Industri")
    st.dataframe(unique_industri['INDUSTRI'])  # This displays the dataframe in a table format
    
    # Optional: Provide some explanation for the table
    st.write("""
    You can click on the column headers to sort the data.
    """)
    
    # Set the title of the Streamlit app
    st.title("Jumlah Pelajar Terlibat")
    
    # Calculate the overall number of students per year
    total_students_by_year = df_industri.groupby('TAHUN')['JUMLAH PELAJAR'].sum()

    # Create an interactive bar chart for the overall number of students per year
    fig_Std = go.Figure()

    # Add bar for total students per year
    fig_Std.add_trace(go.Bar(
        x=total_students_by_year.index,
        y=total_students_by_year.values,
        name='Total Students',
        #text=total_students_by_year.values,  # Show the number of students on hover
        #textposition='outside',
        hoverinfo='y',  # Show text on hover
    ))

    # Set the chart title and axis labels
    fig_Std.update_layout(
        #title="Jumlah Pelajar Terlibat",
        xaxis_title="Year",
        yaxis_title="Number of Students",
        xaxis=dict(tickmode='array', tickvals=[2022, 2023, 2024], ticktext=['2022', '2023', '2024']),
        barmode='group'
    )

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig_Std)

    # Set the title of the Streamlit app
    st.title("Jumlah Pelajar Terlibat per Tahun")
    
    # Load the data
    df_industri = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/Industri.csv', on_bad_lines='skip')
    
    # Group by 'TAHUN' and 'KURSUS' and calculate the sum of 'JUMLAH PELAJAR'
    student_counts = df_industri.groupby(['TAHUN', 'KURSUS'])['JUMLAH PELAJAR'].sum().unstack()
    
    # Create an interactive grouped bar chart for the number of students per year and course
    fig_Course = go.Figure()

    # Map the KURSUS to their respective names
    kursus_mapping = {
        'SAP': 'Pelancongan',
        'SAH': 'Hospitaliti',
        'SAS': 'Kesejahteraan'
    }

    # Rename columns using the mapping
    student_counts = student_counts.rename(columns=kursus_mapping)

    # Add a trace for each KURSUS (SAS, SAH, SAP)
    for kursus in student_counts.columns:
        fig_Course.add_trace(go.Bar(
            x=student_counts.index,
            y=student_counts[kursus],
            name=kursus,
            hoverinfo='y',  # Show the number of students on hover
        ))
    
    # Set the chart title and axis labels
    fig_Course.update_layout(
        #title="Jumlah Pelajar Terlibat per Tahun dan Kursus",
        xaxis_title="Tahun",
        yaxis_title="Number of Students",
        barmode='group',  # Group the bars for each year
        xaxis=dict(tickmode='array', tickvals=student_counts.index, ticktext=student_counts.index),
        legend_title="Kursus"
    )
    
    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig_Course)


except FileNotFoundError:
    st.error("Error: 'Industri.csv' file not found.")
except Exception as e:
    st.error(f"An error occurred: {e}")
