import streamlit as st
import plotly.express as px
import numpy as np

def hearta(k):
    return 15 * np.sin(k)**3

def heartb(k):
    return 12 * np.cos(k) - 5 * np.cos(2 * k) - 2 * np.cos(3 * k) - np.cos(4 * k)

# Crear datos para el corazón
theta = np.linspace(0, 2 * np.pi, 6000)
x = hearta(theta) * 20
y = heartb(theta) * 20

# Crear figura de Plotly
fig = px.line(x=x, y=y, line_shape="linear", labels={"x": "", "y": ""})

# Estilo de la figura
fig.update_layout(
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
)

# Mostrar la figura en Streamlit
st.plotly_chart(fig)
