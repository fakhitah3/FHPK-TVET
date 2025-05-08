import streamlit as st

st.set_page_config(
    page_title="Faculty of Hospitality, Tourism and Wellness UMK",
    page_icon="🏨",  # You can choose an appropriate emoji for the icon, like a hotel emoji.
    menu_items={
        'About': "# Made By Faculty of Hospitality, Tourism and Wellness UMK"
    }
)

analysis = st.Page('PLO_sum.py', title='PLO by Course', icon=":material/school:")
overall = st.Page('Overall_PLO.py', title="Overall PLO")
industri = st.Page('Industry_List.py', title='Industry List', icon=":material/business:")
home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, analysis, overall, industri]
        }
    )

pg.run()
