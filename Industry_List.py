import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/Industri.csv')
    
# Set the title for the app
st.title("Industri and Student Cohort Analysis")

# Visualize the number of unique INDUSTRI
industries_count = df['INDUSTRI'].value_counts()  # Count occurrences of each INDUSTRI
st.write("### Number of Unique INDUSTRI")
st.bar_chart(industries_count)  # Display a bar chart for INDUSTRI counts

# Visualize the number of students by KOHORT 1, KOHORT 2, KOHORT 3
kohort_counts = df[['KOHORT 1', 'KOHORT 2', 'KOHORT 3']].sum()  # Sum of students per KOHORT
st.write("### Number of Students by KOHORT")
st.bar_chart(kohort_counts)  # Display a bar chart for KOHORT student counts

