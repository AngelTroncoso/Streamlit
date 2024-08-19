import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Título de la aplicación
st.title('Análisis de Datos con Streamlit')

# Subtítulo
st.subheader('Carga y análisis de datos')

# Cargar datos
uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Datos cargados:")
    st.write(df.head())

    # Mostrar estadísticas descriptivas
    st.subheader('Estadísticas Descriptivas')
    st.write(df.describe())

    # Selección de columnas para gráfico
    st.subheader('Visualización')
    columns = df.columns.tolist()
    x_axis = st.selectbox('Selecciona la columna para el eje X:', columns)
    y_axis = st.selectbox('Selecciona la columna para el eje Y:', columns)

    # Crear gráfico
    if x_axis and y_axis:
        st.write(f'Gráfico de {y_axis} vs {x_axis}')
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)
else:
    st.write("Por favor, carga un archivo CSV para comenzar.")
