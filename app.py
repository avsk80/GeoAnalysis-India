import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("./india.csv")

st.set_page_config(page_title="India Geo Analytics", page_icon=":1234:", layout="wide")
st.title("India Geo Analytics")

# State,District,Latitude,Longitude,District code,Population,Households_with_Internet,sex_ratio,literacy_rate

list_of_states = df["State"].unique().tolist()
list_of_states.insert(0, "All")

state = st.sidebar.selectbox("Select State", list_of_states)
primary = st.sidebar.selectbox("Select Primary parameter", sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary parameter", sorted(df.columns[5:].to_list()))

plot = st.sidebar.button("Plot")

if plot is not None:
    st.write("You selected:", state, primary, secondary)
    st.write("primary represents color, and secondary represents size of the bubble")
    if state == "All":
        #pass
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color=primary, size=secondary,
                                zoom=4, hover_data='District', height=500, width=1000, color_continuous_scale='Viridis')
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig, use_container_width=True)
    else:
        #pass 
        fig = px.scatter_mapbox(df[df["State"] == state], lat="Latitude", lon="Longitude", color=primary, size=secondary,
                                zoom=4, hover_data='District', height=500, width=1000, color_continuous_scale='Viridis')
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig, use_container_width=True)
        
