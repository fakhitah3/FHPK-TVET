import streamlit as st

# Set the title of the app
st.title("Streamlit Multi-Page App")

st.set_page_config(
    page_title="Faculty of Hospitality, Tourism and Wellness UMK",
    page_icon="🏨",  # You can choose an appropriate emoji for the icon, like a hotel emoji.
    menu_items={
        'About': "# Made By Faculty of Hospitality, Tourism and Wellness UMK"
    }
)

# Create a sidebar with navigation options
page = st.sidebar.radio("Select Page", ["PLO Sum Visualization", "Overall PLO"])

# Based on the selection, navigate to the corresponding page
if page == "PLO Sum Visualization":
    st.write("### PLO Sum Visualization")
    # Run the code for the first page (PLO Sum Visualization)
    import PLO_sum  # This is the file containing the logic for PLO Sum Visualization
elif page == "Data Table":
    st.write("### Overall PLO")
    # Run the code for the second page (Data Table)
    import Overall_PLO  # This is the file containing the logic for the second page
