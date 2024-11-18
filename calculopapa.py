import streamlit as st
import pandas as pd

# Título de la app
st.title("Calculadora de PAPA")
st.write("Calcula tu Promedio Académico Ponderado Acumulado (PAPA) global y por tipología de asignatura.")

# Datos iniciales
if 'materias' not in st.session_state:
    st.session_state.materias = pd.DataFrame(columns=["Asignatura", "Tipología", "Créditos", "Nota"])

# Función para calcular el PAPA
def calcular_papa(df):
    if df.empty:
        return 0
    total_ponderado = (df["Créditos"] * df["Nota"]).sum()
    total_creditos = df["Créditos"].sum()
    return total_ponderado / total_creditos if total_creditos > 0 else 0

# Sección para agregar materias
st.header("Agregar Materias")
asignatura = st.text_input("Nombre de la asignatura")
tipologia = st.selectbox("Tipología de la asignatura", ["Obligatoria", "Electiva", "Otra"])
creditos = st.number_input("Número de créditos", min_value=0, step=1, format="%d")
nota = st.number_input("Calificación", min_value=0.0, max_value=5.0, step=0.1)

if st.button("Agregar Materia"):
    nueva_materia = pd.DataFrame([{
        "Asignatura": asignatura,
        "Tipología": tipologia,
        "Créditos": creditos,
        "Nota": nota
    }])
    st.session_state.materias = pd.concat([st.session_state.materias, nueva_materia], ignore_index=True)
    st.success(f"Materia '{asignatura}' agregada correctamente.")

# Mostrar las materias registradas
st.header("Materias Registradas")
if st.session_state.materias.empty:
    st.write("No hay materias registradas.")
else:
    st.dataframe(st.session_state.materias)

# Cálculo del PAPA global
st.header("PAPA Global")
papa_global = calcular_papa(st.session_state.materias)
st.write(f"Tu PAPA global es: **{papa_global:.2f}**")

# Cálculo del PAPA por tipología
st.header("PAPA por Tipología de Asignatura")
if not st.session_state.materias.empty:
    tipologias = st.session_state.materias["Tipología"].unique()
    for tipo in tipologias:
        df_tipo = st.session_state.materias[st.session_state.materias["Tipología"] == tipo]
        papa_tipo = calcular_papa(df_tipo)
        st.write(f"**{tipo}:** {papa_tipo:.2f}")
