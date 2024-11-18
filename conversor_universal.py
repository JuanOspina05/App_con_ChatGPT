import streamlit as st

# Título de la app
st.title("Conversor Universal")

# Categorías de conversión
categoria = st.selectbox(
    "Selecciona una categoría de conversión:",
    [
        "Conversiones de temperatura",
        "Conversiones de longitud",
        "Conversiones de peso/masa",
        "Conversiones de volumen",
        "Conversiones de tiempo",
        "Conversiones de velocidad",
        "Conversiones de área",
        "Conversiones de energía",
        "Conversiones de presión",
        "Conversiones de tamaño de datos"
    ]
)

# Funciones de conversión
if categoria == "Conversiones de temperatura":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Celsius a Fahrenheit":
        resultado = (valor * 9/5) + 32
    elif conversion == "Fahrenheit a Celsius":
        resultado = (valor - 32) * 5/9
    elif conversion == "Celsius a Kelvin":
        resultado = valor + 273.15
    elif conversion == "Kelvin a Celsius":
        resultado = valor - 273.15
    st.write(f"Resultado: {resultado}")

elif categoria == "Conversiones de longitud":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Pies a metros":
        resultado = valor * 0.3048
    elif conversion == "Metros a pies":
        resultado = valor / 0.3048
    elif conversion == "Pulgadas a centímetros":
        resultado = valor * 2.54
    elif conversion == "Centímetros a pulgadas":
        resultado = valor / 2.54
    st.write(f"Resultado: {resultado}")

elif categoria == "Conversiones de peso/masa":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Libras a kilogramos":
        resultado = valor * 0.453592
    elif conversion == "Kilogramos a libras":
        resultado = valor / 0.453592
    elif conversion == "Onzas a gramos":
        resultado = valor * 28.3495
    elif conversion == "Gramos a onzas":
        resultado = valor / 28.3495
    st.write(f"Resultado: {resultado}")

elif categoria == "Conversiones de volumen":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Galones a litros":
        resultado = valor * 3.78541
    elif conversion == "Litros a galones":
        resultado = valor / 3.78541
    elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
        resultado = valor * 16.3871
    elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
        resultado = valor / 16.3871
    st.write(f"Resultado: {resultado}")

elif categoria == "Conversiones de tiempo":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Horas a minutos":
        resultado = valor * 60
    elif conversion == "Minutos a segundos":
        resultado = valor * 60
    elif conversion == "Días a horas":
        resultado = valor * 24
    elif conversion == "Semanas a días":
        resultado = valor * 7
    st.write(f"Resultado: {resultado}")

elif categoria == "Conversiones de velocidad":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Millas por hora a kilómetros por hora":
        resultado = valor * 1.60934
    elif conversion == "Kilómetros por hora a metros por segundo":
        resultado = valor / 3.6
    elif conversion == "Nudos a millas por hora":
        resultado = valor * 1.15078
    elif conversion == "Metros por segundo a pies por segundo":
        resultado = valor * 3.28084
    st.write(f"Resultado: {resultado}")

elif categoria == "Conversiones de área":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Metros cuadrados a pies cuadrados":
        resultado = valor * 10.7639
    elif conversion == "Pies cuadrados a metros cuadrados":
        resultado = valor / 10.7639
    elif conversion == "Kilómetros cuadrados a millas cuadradas":
        resultado = valor / 2.58999
    elif conversion == "Millas cuadradas a kilómetros cuadrados":
        resultado = valor * 2.58999
    st.write(f"Resultado: {resultado}")

elif categoria == "Conversiones de energía":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Julios a calorías":
        resultado = valor / 4.184
    elif conversion == "Calorías a kilojulios":
        resultado = valor * 0.004184
    elif conversion == "Kilovatios-hora a megajulios":
        resultado = valor * 3.6
    elif conversion == "Megajulios a kilovatios-hora":
        resultado = valor / 3.6
    st.write(f"Resultado: {resultado}")

elif categoria == "Conversiones de presión":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Pascales a atmósferas":
        resultado = valor / 101325
    elif conversion == "Atmósferas a pascales":
        resultado = valor * 101325
    elif conversion == "Barras a libras por pulgada cuadrada":
        resultado = valor * 14.5038
    elif conversion == "Libras por pulgada cuadrada a bares":
        resultado = valor / 14.5038
    st.write(f"Resultado: {resultado}")

elif categoria == "Conversiones de tamaño de datos":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        ["Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"]
    )
    valor = st.number_input("Ingresa el valor:")
    if conversion == "Megabytes a gigabytes":
        resultado = valor / 1024
    elif conversion == "Gigabytes a Terabytes":
        resultado = valor / 1024
    elif conversion == "Kilobytes a megabytes":
        resultado = valor / 1024
    elif conversion == "Terabytes a petabytes":
        resultado = valor / 1024
    st.write(f"Resultado: {resultado}")
