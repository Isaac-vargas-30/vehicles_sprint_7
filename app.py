import pandas as pd
import plotly.express as px
import streamlit as st

#diseño de la app & titulo de la pestaña
st.set_page_config(page_title="Vehículo EEUU",layout="centered")

#titulo de la app
st.header("Análisis interactivo de vehiculos en EEUU")

#leer datos & con el decorador @st.cache_data se evita que se carguen los datos cada vez que se carga la app
@st.cache_data
def cargar_datos():    
    vehicles_df = pd.read_csv("vehicles_us.csv")
    vehicles_df = vehicles_df.dropna(subset=["odometer", "price"])
    return vehicles_df

# de esta forma se cargan los datos cuando inicia la app
datos_vehiculos = cargar_datos() 

# controles y gráficos

histograma = st.checkbox("Mostrar histograma")
scatter = st.checkbox("Mostrar dispersión")

if histograma:
    st.write("## Histograma del odómetro")
    fig = px.histogram(datos_vehiculos, x="odometer", nbins=50)
    st.plotly_chart(fig, use_container_width=True)
    
if scatter:
    st.write("## Dispersión del precio vs odómetro")
    fig = px.scatter(datos_vehiculos, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

    
