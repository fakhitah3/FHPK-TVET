import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Add a header to the Streamlit app
st.title("Pelancongan")  # This creates a title at the top of the page

try:
  df = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAP.csv')
  print(df.head()) # Print the first few rows to verify
except FileNotFoundError:
  print("Error: File not found. Please upload the file to your current working directory or provide the correct path.")
except Exception as e:
  print(f"An error occurred: {e}")


# Filter data for 2023
df_2023 = df[df['Tahun'] == 2023]

# Grouped bar chart
plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']
subjects = df_2023['Subjek'].unique()

width = 0.15
x = range(len(subjects))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

for i, plo in enumerate(plo_columns):
    ax.bar([val + i * width for val in x], df_2023.groupby('Subjek')[plo].sum(), width, label=plo)

ax.set_xlabel("Subjek")
ax.set_ylabel("Nilai")
ax.set_title("PLO Performance for Subjects in 2023")
ax.set_xticks([val + width for val in x])
ax.set_xticklabels(subjects, rotation=45, ha='right')
# Legend placed outside the chart (top right)
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)

# Use Streamlit's st.pyplot to display the plot
st.pyplot(fig)

# Add a header to the Streamlit app
st.title("Hospitaliti")  # This creates a title at the top of the page

try:
  df = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAH.csv')
  print(df.head()) # Print the first few rows to verify
except FileNotFoundError:
  print("Error: File not found. Please upload the file to your current working directory or provide the correct path.")
except Exception as e:
  print(f"An error occurred: {e}")


# Filter data for 2023
df_2023 = df[df['Tahun'] == 2023]

# Grouped bar chart
plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']
subjects = df_2023['Subjek'].unique()

width = 0.15
x = range(len(subjects))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

for i, plo in enumerate(plo_columns):
    ax.bar([val + i * width for val in x], df_2023.groupby('Subjek')[plo].sum(), width, label=plo)

ax.set_xlabel("Subjek")
ax.set_ylabel("Nilai")
ax.set_title("PLO Performance for Subjects in 2023")
ax.set_xticks([val + width for val in x])
ax.set_xticklabels(subjects, rotation=45, ha='right')
# Legend placed outside the chart (top right)
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)

# Use Streamlit's st.pyplot to display the plot
st.pyplot(fig)

# Add a header to the Streamlit app
st.title("Kesejahteraan")  # This creates a title at the top of the page

try:
  df = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/FHPK-TVET/refs/heads/main/Data/PLO%20Analysis%20SAS.csv')
  print(df.head()) # Print the first few rows to verify
except FileNotFoundError:
  print("Error: File not found. Please upload the file to your current working directory or provide the correct path.")
except Exception as e:
  print(f"An error occurred: {e}")


# Filter data for 2023
df_2023 = df[df['Tahun'] == 2023]

# Grouped bar chart
plo_columns = ['PLO 2', 'PLO 3', 'PLO 4', 'PLO 5']
subjects = df_2023['Subjek'].unique()

width = 0.15
x = range(len(subjects))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

for i, plo in enumerate(plo_columns):
    ax.bar([val + i * width for val in x], df_2023.groupby('Subjek')[plo].sum(), width, label=plo)

ax.set_xlabel("Subjek")
ax.set_ylabel("Nilai")
ax.set_title("PLO Performance for Subjects in 2023")
ax.set_xticks([val + width for val in x])
ax.set_xticklabels(subjects, rotation=45, ha='right')
# Legend placed outside the chart (top right)
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)

# Use Streamlit's st.pyplot to display the plot
st.pyplot(fig)








