"""
Interfaz web del Agente de Consultas Internas Empresariales.
Usa la lógica de búsqueda ya implementada en main.py (no la duplica).
"""

import streamlit as st
from src.main import buscar_respuesta, cargar_faq, RUTA_FAQ

# ----- Configuración de página -----
st.set_page_config(
    page_title="Alura Agente - Consultas Internas",
    page_icon="🤖",
    layout="centered",
)

# ----- Carga del FAQ (una sola vez, cacheada) -----
@st.cache_data
def obtener_faq():
    return cargar_faq(RUTA_FAQ)

faq = obtener_faq()

# ----- Encabezado -----
st.title("🤖 Alura Agente")
st.caption("Agente de Consultas Internas Empresariales — Challenge Alura ONE AI for Tech")
st.divider()

# ----- Sidebar -----
with st.sidebar:
    st.header("ℹ️ Sobre este agente")
    st.write(
        "Responde preguntas sobre políticas y procesos internos "
        "usando documentación corporativa como base de conocimiento."
    )
    st.subheader("📂 Temas disponibles")
    st.markdown(
        "- 👋 Onboarding\n"
        "- 🏖️ Vacaciones\n"
        "- 🛒 Compras\n"
        "- 🛠️ Soporte técnico"
    )
    st.divider()
    st.caption("Versión 1 · Búsqueda por palabras clave y sinónimos")
    st.caption("Próximo paso: migrar a RAG con LangChain + Gemini")

# ----- Preguntas de ejemplo (atajos) -----
st.write("**Probá con una pregunta frecuente:**")
col1, col2, col3, col4 = st.columns(4)
ejemplo_clic = None

with col1:
    if st.button("🏖️ Vacaciones"):
        ejemplo_clic = "¿Cómo solicito vacaciones?"
with col2:
    if st.button("🛒 Compras"):
        ejemplo_clic = "¿Quién aprueba una compra?"
with col3:
    if st.button("🛠️ Soporte"):
        ejemplo_clic = "¿Cuánto demora soporte?"
with col4:
    if st.button("👋 Onboarding"):
        ejemplo_clic = "¿Qué hago en mi primera semana?"

# ----- Historial de conversación en memoria de sesión -----
if "historial" not in st.session_state:
    st.session_state.historial = []

# ----- Entrada de consulta (chat) -----
consulta_manual = st.chat_input("Escribí tu consulta acá...")
consulta = ejemplo_clic or consulta_manual

if consulta:
    with st.spinner("Buscando en la documentación interna..."):
        respuesta = buscar_respuesta(consulta, faq)

    encontrada = "No encontré información relacionada" not in respuesta
    st.session_state.historial.append((consulta, respuesta, encontrada))

# ----- Mostrar historial de conversación -----
if st.session_state.historial:
    st.divider()
    for pregunta_usuario, respuesta_agente, encontrada in reversed(st.session_state.historial):
        with st.chat_message("user"):
            st.write(pregunta_usuario)
        with st.chat_message("assistant"):
            if encontrada:
                st.success(respuesta_agente)
            else:
                st.warning(respuesta_agente)
else:
    st.info("Escribí una consulta arriba o probá uno de los botones de ejemplo. 👆")

# ----- Botón para limpiar historial -----
if st.session_state.historial:
    st.divider()
    if st.button("🗑️ Limpiar conversación"):
        st.session_state.historial = []
        st.rerun()

# ----- Footer -----
st.divider()
st.caption("Challenge Alura ONE AI for Tech · Lucía Susana Mendoza León")