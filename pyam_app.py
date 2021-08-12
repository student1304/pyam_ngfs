
# https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py

import pyam 
import pandas as pd
import streamlit as st

# @st.cache(persist=True)
# def get_data():
#     df = pyam.read_iiasa(
#         'iamc15',
#         #variable=['Price*','GDP*','Tempera*', 'CO2*'], 
#         #region='World',
#         #meta=['category', 'carbon price|2030', 'carbon price|2050', 'carbon price|2100']
#     )
#     return df
# df = get_data()

@st.cache
def get_df():
    df = pyam.read_datapackage('./iamc15_limdata.datapackage')
    return df

df = get_df()

st.title('PyAm NGFS Explorer')
st.subheader('Load data from NGFS and display selected variables')
st.write("<br><hr>", unsafe_allow_html=True)
st.caption("*[Download](./scenarios_overview.pdf) .pdf with scenario overview*")

region = st.sidebar.multiselect(label='Region', options = df.region)
d1 = df.filter(region=region)

model = st.sidebar.multiselect(label='Model', options = d1.model)
d2 = d1.filter(model=model)

scenario = st.sidebar.multiselect(label='Scenario', options = d2.scenario)
d3 = d2.filter(scenario=scenario)

variable = st.sidebar.multiselect(label='Variable', options = d3.variable)
d4 = d3.filter(variable=variable)

#max_year = st.slider(label='Timeframe', value=2050, min_value=2021, max_value=2050, step=1)
#val_cols = [str(i) for i in range(2021, max_year)]

chart = st.empty()
download_link = st.empty()

try:
    ax = d4.plot(color="scenario", fill_between=dict(alpha=0.15), final_ranges=dict(linewidth=3))
    fig = ax.get_figure()
    fig.savefig('img/fig.png')
    
    chart = st.pyplot(fig)
    download_link = st.caption("*Click [here]('img/fig.png') to download this chart as .png*")
except:
    chart=st.write(" :sunglasses: *Make (more) selections in the sidebar to see a chart.*")
    
    

## code to load data
# %%writefile load_and_save_iiasa_data.py
# import pyam
# import os
# path='/home/bjoern/Desktop/data/'
# datafile = 'iamc15_limdata.datapackage'

# my_models= ['MESSAGEix-GLOBIOM 1.0','REMIND-MAgPIE 1.7-3.0','WITCH-GLOBIOM 4.4', 'GCAM 4.2','POLES CD-LINKS']
# my_meta = ['category', 'carbon price|2030', 'carbon price|2050', 'carbon price|2100']
# my_variables = ['Emissions|CO2', 'Discount rate*','GDP*',
#              'Population', 'Price*', 'Temperature|Global Mean', 'Value Added*',
#               'Consumption', 'Policy Cost*' ]
# my_regions = ['World', 'R5ROWO', 'R5OECD90+EU', 'R5REF']

# df = pyam.read_iiasa(
#     'iamc15',
#      model=my_models, 
#     variable= my_variables,
#     region='R50ECD90+EU',
#     meta=my_meta
# )

# df.to_datapackage(os.path.join(path, datafile))

# d2 = pyam.read_datapackage(os.path.join(path, datafile))
    



   
