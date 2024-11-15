#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
from streamlit_option_menu import option_menu
import Home, Filtering, Analysis, Prediction # Import individual app modules


# In[4]:


# Set Streamlit page configuration
st.set_page_config(
    page_title='Cardekho Resale Price Prediction',
    layout='wide'
)

# Define a class to manage multiple apps
class multiapp:
    def __init__(self):
        self.apps = []  # Store app title and function pairs

    def add_app(self, title, function):
        # Add app to the list
        self.apps.append({'title': title, 'function': function})

    def run(self):
        # Sidebar navigation
        with st.sidebar:
            app = option_menu(
                'Car Resale Price Prediction',  # Sidebar title
                ["Home", "Data Filtering", "Data Analysis", "Data Prediction"],  # Options
                icons=['house', 'search', "reception-4", "dice-5-fill"],  # Option icons
                menu_icon='cash-coin',  # Menu icon
                default_index=0,  # Default selected option
                orientation="vertical",  # Layout orientation
                styles={  # Styling the sidebar menu
                    "container": {"padding": "0!important", "background-color": "#A95C68"},
                    "icon": {"color": "violet", "font-size": "20px"},
                    "nav-link": {"font-size": "18px", "text-align": "left", "margin": "0px", "--hover-color": "#C4A484"},
                    "nav-link-selected": {"background-color": "#C04000"},
                }
            )

        # Determine which app to run based on the selected option
        if app == 'Home':
            Home.app()
        elif app == 'Data Filtering':
            Filtering.app()
        elif app == 'Data Analysis':
            Analysis.app()
        elif app == 'Data Prediction':
            Prediction.app()

# Create an instance of the multiapp class
app = multiapp()

# Add your apps to the multiapp instance
app.add_app("Home", Home.app)  # Home page
app.add_app("Data Filtering", Filtering.app)  # Filtering page
app.add_app("Data Analysis", Analysis.app)  # Analysis page
app.add_app("Data Prediction", Prediction.app)  # Prediction page

# Run the multiapp
app.run()


# In[ ]:




