import streamlit as st
import pandas as pd
import datetime

# Configuración inicial
st.title("Gestor de Finanzas Personales")
st.write("Registra tus ingresos, gastos y metas de ahorro, y genera reportes para analizar tus finanzas.")

# Función para calcular diferencias
def calcular_diferencias(df):
    df['Diferencia'] = df['Presupuestado'] - df['Real']
    return df

# Datos iniciales
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Fecha", "Categoría", "Presupuestado", "Real", "Tipo"]
    )

# Sección para agregar registros
st.header("Agregar registro")
col1, col2 = st.columns(2)
categoria = col1.selectbox(
    "Selecciona una categoría",
    ["Ingresos", "Gastos", "Ahorro"]
)
tipo = col2.text_input("Descripción (por ejemplo, salario, comida, etc.)")
fecha = st.date_input("Fecha", datetime.date.today())
presupuestado = st.number_input("Cantidad presupuestada:", min_value=0.0, step=0.1)
real = st.number_input("Cantidad real:", min_value=0.0, step=0.1)

if st.button("Agregar"):
    nuevo_registro = pd.DataFrame([{
        "Fecha": pd.to_datetime(fecha),
        "Categoría": categoria,
        "Presupuestado": presupuestado,
        "Real": real,
        "Tipo": tipo
    }])
    st.session_state.data = pd.concat([st.session_state.data, nuevo_registro], ignore_index=True)
    st.success("Registro agregado correctamente.")

# Mostrar los datos actuales
st.header("Registros actuales")
st.dataframe(st.session_state.data)

# Generar reportes
st.header("Reportes financieros")
opcion_reporte = st.selectbox(
    "Selecciona el periodo para el reporte:",
    ["Semanal", "Mensual"]
)

if opcion_reporte == "Semanal":
    inicio_semana = st.date_input("Inicio de la semana", datetime.date.today() - datetime.timedelta(days=7))
    fin_semana = st.date_input("Fin de la semana", datetime.date.today())

    # Asegurar que la columna Fecha sea de tipo datetime
    st.session_state.data['Fecha'] = pd.to_datetime(st.session_state.data['Fecha'])

    filtro = (st.session_state.data["Fecha"] >= pd.Timestamp(inicio_semana)) & \
             (st.session_state.data["Fecha"] <= pd.Timestamp(fin_semana))
    reporte = st.session_state.data.loc[filtro]
    if not reporte.empty:
        reporte = calcular_diferencias(reporte)
        st.subheader("Reporte Semanal")
        st.dataframe(reporte)
    else:
        st.write("No hay registros en el periodo seleccionado.")

elif opcion_reporte == "Mensual":
    mes = st.selectbox("Selecciona el mes", range(1, 13), index=datetime.date.today().month - 1)
    año = st.number_input("Selecciona el año", min_value=2000, max_value=2100, value=datetime.date.today().year)

    # Asegurar que la columna Fecha sea de tipo datetime
    st.session_state.data['Fecha'] = pd.to_datetime(st.session_state.data['Fecha'])

    filtro = (
        (st.session_state.data["Fecha"].dt.month == mes) &
        (st.session_state.data["Fecha"].dt.year == año)
    )
    reporte = st.session_state.data.loc[filtro]
    if not reporte.empty:
        reporte = calcular_diferencias(reporte)
        st.subheader("Reporte Mensual")
        st.dataframe(reporte)
    else:
        st.write("No hay registros en el periodo seleccionado.")

# Análisis general
st.header("Análisis general")
if not st.session_state.data.empty:
    total_presupuestado = st.session_state.data["Presupuestado"].sum()
    total_real = st.session_state.data["Real"].sum()
    diferencia_total = total_presupuestado - total_real

    st.write(f"**Total presupuestado:** {total_presupuestado}")
    st.write(f"**Total real:** {total_real}")
    st.write(f"**Diferencia total:** {diferencia_total}")
else:
    st.write("Aún no hay datos registrados.")
