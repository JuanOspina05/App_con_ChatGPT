import streamlit as st
import pandas as pd
import numpy as np

# Título de la app
st.title("Visualizador de Clima Simulado 🌤️")
st.write("¡Simula el clima de ciudades ficticias! Ajusta parámetros para explorar diferentes escenarios climáticos.")

# Sidebar para configuración
st.sidebar.header("Configuración de Simulación")
ciudad = st.sidebar.text_input("Escribe el nombre de una ciudad ficticia:", value="Ciudad Ficticia")
dias_simulacion = st.sidebar.slider("Días de simulación", min_value=7, max_value=30, value=15, step=1)
temp_media = st.sidebar.slider("Temperatura media (°C)", min_value=-10, max_value=40, value=25)
humedad_media = st.sidebar.slider("Humedad media (%)", min_value=10, max_value=100, value=60)
prob_precipitacion = st.sidebar.slider("Probabilidad de precipitación (%)", min_value=0, max_value=100, value=30)

# Generar datos simulados
np.random.seed(42)  # Semilla para reproducibilidad
fechas = pd.date_range(start="2024-01-01", periods=dias_simulacion)
temperaturas = np.random.normal(loc=temp_media, scale=5, size=dias_simulacion).round(1)
humedades = np.random.normal(loc=humedad_media, scale=10, size=dias_simulacion).clip(10, 100).round(1)
precipitaciones = (np.random.rand(dias_simulacion) < (prob_precipitacion / 100)).astype(int) * np.random.uniform(0, 20, size=dias_simulacion).round(1)

# Crear DataFrame
data_clima = pd.DataFrame({
    "Fecha": fechas,
    "Temperatura (°C)": temperaturas,
    "Humedad (%)": humedades,
    "Precipitación (mm)": precipitaciones
})

# Mostrar datos
st.subheader(f"Clima simulado para {ciudad} 🌍")
st.dataframe(data_clima)

# Gráficos dinámicos usando herramientas nativas de Streamlit
st.subheader("Visualización del Clima")

# Gráfico de temperatura
st.line_chart(data=data_clima.set_index("Fecha")["Temperatura (°C)"], use_container_width=True)

# Gráfico de humedad
st.line_chart(data=data_clima.set_index("Fecha")["Humedad (%)"], use_container_width=True)

# Gráfico de precipitación
st.bar_chart(data=data_clima.set_index("Fecha")["Precipitación (mm)"], use_container_width=True)
