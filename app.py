
# https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py

import pyam 
import pandas as pd
import streamlit as st

@st.cache(persist=True)
def get_data():
    df = pyam.read_iiasa(
        'iamc15',
        #variable=['Price*','GDP*','Tempera*', 'CO2*'], 
        #region='World',
        #meta=['category', 'carbon price|2030', 'carbon price|2050', 'carbon price|2100']
    )
    return df

df = get_data()

st.title('PyAm NGFS Explorer')

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


ax = d4.plot()
fig = ax.get_figure()
#fig.savefig('fig.png')


st.pyplot(fig)
   
