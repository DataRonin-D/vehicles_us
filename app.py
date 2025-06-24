from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
user_home = Path.home()
RUTA = 'vehicles_us/vehicles_us.csv'
pathcomplete = user_home / RUTA
car_data = pd.read_csv(pathcomplete)

#histograma
st.sidebar.title('Histograma de Vehículos') #titulo del sidebar
variable = st.sidebar.selectbox('Selecciona una variable', car_data.columns)
st.sidebar.write('Variable seleccionada:', variable)
hist_button = st.button('crear histograma')

if hist_button:
    #histograma de la variable seleccionada
    st.write(f'Histograma de {variable}')
    # Crear histograma usando Plotly Express
    fig = px.histogram(car_data, x=variable, nbins=len(car_data), title=f'Histograma de {variable}')
    # mostrar el histograma
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
st.sidebar.title('Gráfico de Dispersión de Vehículos') #titulo del sidebar
x_variable = st.sidebar.selectbox('Selecciona la variable X', car_data.columns)
y_variable = st.sidebar.selectbox('Selecciona la variable Y', car_data.columns)
st.sidebar.write('Variables seleccionadas:', x_variable, 'y', y_variable) #variables seleccionadas
scatter_button = st.button('crear gráfico de dispersión') #botón para crear el gráfico de dispersión

# Checkbox para invertir ejes
lista_invertida = st.sidebar.checkbox('Invertir Ejes') #checkbox para invertir ejes
if lista_invertida:
    x_variable, y_variable = y_variable, x_variable

# Mostrar las variables seleccionadas
st.sidebar.write('Ejes seleccionados:', x_variable, 'y', y_variable) #variables seleccionadas

if scatter_button:
    #Gráfico de dispersión de las variables seleccionadas
    st.write(f'Gráfico de dispersión de {x_variable} y {y_variable}')
    # Crear gráfico de dispersión usando Plotly Express
    fig = px.scatter(car_data,
                     x=x_variable, y=y_variable,
                     title=f'Gráfico de Dispersión de {x_variable} y {y_variable}')
    # mostrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)

# Reset button
reset_button = st.sidebar.button('Reiniciar')  # Botón para reiniciar la aplicación
if reset_button:
    st.caching.clear_cache() # Limpiar la caché de Streamlit
    st.experimental_rerun() # Reiniciar la aplicación
    st.write("La aplicación ha sido reiniciada.")  # Mensaje de confirmación
