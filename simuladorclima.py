import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Gráficos dinámicos
st.subheader("Visualización del Clima")

# Gráfico de temperatura
fig_temp, ax_temp = plt.subplots()
ax_temp.plot(data_clima["Fecha"], data_clima["Temperatura (°C)"], marker="o", label="Temperatura (°C)")
ax_temp.set_title(f"Temperatura Diaria en {ciudad}")
ax_temp.set_xlabel("Fecha")
ax_temp.set_ylabel("Temperatura (°C)")
ax_temp.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig_temp)

# Gráfico de humedad
fig_humedad, ax_humedad = plt.subplots()
ax_humedad.plot(data_clima["Fecha"], data_clima["Humedad (%)"], marker="o", color="green", label="Humedad (%)")
ax_humedad.set_title(f"Humedad Diaria en {ciudad}")
ax_humedad.set_xlabel("Fecha")
ax_humedad.set_ylabel("Humedad (%)")
ax_humedad.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig_humedad)

# Gráfico de precipitación
fig_prec, ax_prec = plt.subplots()
ax_prec.bar(data_clima["Fecha"], data_clima["Precipitación (mm)"], color="blue", label="Precipitación (mm)")
ax_prec.set_title(f"Precipitación Diaria en {ciudad}")
ax_prec.set_xlabel("Fecha")
ax_prec.set_ylabel("Precipitación (mm)")
ax_prec.grid(True)
plt.xticks(rotation=45)
st.pyplot(fig_prec)
