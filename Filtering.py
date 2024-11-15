#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
import streamlit_pandas as sp
import google.cloud


# In[4]:


# Main app function
def app():
    # Display header
    colored_header(
        label = 'You are in Data :blue[Filtering] page',
        color_name = 'blue-70',
        description = ''
    )
    
    # Cache data loading function
    @st.cache_data
    def data():
        return pd.read_csv('Cleaned_Car_Dheko.csv')
    
    df = data()
    
    # Convert columns to string
    df['Car_Produced_Year'] = df['Car_Produced_Year'].astype('str')
    df['Registration_Year'] = df['Registration_Year'].astype('str')

    # Sidebar select box
    choice = st.sidebar.selectbox(
        '*Select a column to know unique values :*', ['Car_Model', 'Manufactured_By']
    )

    # Show unique values in sidebar
    if choice == 'Car_Model':
        unique_values = pd.DataFrame({'Car_Models': df['Car_Model'].unique()})
    else:
        unique_values = pd.DataFrame({'Car_Companies': df['Manufactured_By'].unique()})
    st.sidebar.dataframe(unique_values, use_container_width=True)

    # Dataframe explorer
    filter = dataframe_explorer(df)

    # Submit button
    if st.button('**SUBMIT**', use_container_width=True):
        st.dataframe(filter, use_container_width=True, hide_index=True)


# Version: 0.0.9

# In[ ]:




