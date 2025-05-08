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

PLO = st.Page('PLO_sum.py', title='PLO by Course')
overall = st.Page('Overall_PLO.py', title="DOverall PLO")
home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home,PLO,overall]
        }
    )

pg.run()
