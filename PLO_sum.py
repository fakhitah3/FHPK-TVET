import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# Add a header to the Streamlit app
st.title("Pelancongan")  # This creates a title at the top of the page

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

col1.metric(label="PLO 2", value=f"{plo_sums['PLO 2']:.2f}", help="Total value for PLO 2", border=True)
col2.metric(label="PLO 3", value=f"{plo_sums['PLO 3']:.2f}", help="Total value for PLO 3", border=True)
col3.metric(label="PLO 4", value=f"{plo_sums['PLO 4']:.2f}", help="Total value for PLO 4", border=True)
col4.metric(label="PLO 5", value=f"{plo_sums['PLO 5']:.2f}", help="Total value for PLO 5", border=True)
  
# Create the plot
fig = go.Figure()

# Add each PLO as a separate trace (bar group)
for i, plo in enumerate(plo_columns):
    values = df_filtered.groupby('Subjek')[plo].sum()
    fig.add_trace(go.Bar(
        x=[val + i * width for val in x],
        y=values,
        name=plo,
        # text=values,  # Display the value on hover
        # textposition='outside',  # Position the text outside the bar
        hoverinfo='y',  # Show text on hover
    ))

# Update layout to set axis labels and chart title
fig.update_layout(
    title=f"PLO Performance for Subjects {year_selectionSAP}",
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
st.plotly_chart(fig)

# Add a header to the Streamlit app
st.title("Hospitaliti")  # This creates a title at the top of the page

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

col1.metric(label="PLO 2", value=f"{plo_sums['PLO 2']:.2f}", help="Total value for PLO 2", border=True)
col2.metric(label="PLO 3", value=f"{plo_sums['PLO 3']:.2f}", help="Total value for PLO 3", border=True)
col3.metric(label="PLO 4", value=f"{plo_sums['PLO 4']:.2f}", help="Total value for PLO 4", border=True)
col4.metric(label="PLO 5", value=f"{plo_sums['PLO 5']:.2f}", help="Total value for PLO 5", border=True)


width = 0.15
x = range(len(subjects))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

for i, plo in enumerate(plo_columns):
    ax.bar([val + i * width for val in x], dx_filtered.groupby('Subjek')[plo].sum(), width, label=plo)

ax.set_xlabel("Subjek")
ax.set_ylabel("Nilai")
ax.set_title(f"PLO Performance for Subjects {year_selectionSAH}")
ax.set_xticks([val + width for val in x])
ax.set_xticklabels(subjects, rotation=45, ha='right')
# Legend placed outside the chart (top right)
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)

# Use Streamlit's st.pyplot to display the plot
st.pyplot(fig)

# Add a header to the Streamlit app
st.title("Kesejahteraan")  # This creates a title at the top of the page

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

col1.metric(label="PLO 2", value=f"{plo_sums['PLO 2']:.2f}", help="Total value for PLO 2", border=True)
col2.metric(label="PLO 3", value=f"{plo_sums['PLO 3']:.2f}", help="Total value for PLO 3", border=True)
col3.metric(label="PLO 4", value=f"{plo_sums['PLO 4']:.2f}", help="Total value for PLO 4", border=True)
col4.metric(label="PLO 5", value=f"{plo_sums['PLO 5']:.2f}", help="Total value for PLO 5", border=True)
  

width = 0.15
x = range(len(subjects))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

for i, plo in enumerate(plo_columns):
    ax.bar([val + i * width for val in x], dy_filtered.groupby('Subjek')[plo].sum(), width, label=plo)

ax.set_xlabel("Subjek")
ax.set_ylabel("Nilai")
ax.set_title(f"PLO Performance for Subjects {year_selectionSAS}")
ax.set_xticks([val + width for val in x])
ax.set_xticklabels(subjects, rotation=45, ha='right')
# Legend placed outside the chart (top right)
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0)

# Use Streamlit's st.pyplot to display the plot
st.pyplot(fig)
