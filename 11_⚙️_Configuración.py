import streamlit as st
from config import settings

st.title("⚙️ Configuración")
st.write("Entorno:", settings.APP_ENV)
st.write("Base de datos:", "SQLite" if settings.DATABASE_URL.startswith("sqlite") else "PostgreSQL")
st.caption("Las credenciales y secretos deben permanecer en .env y nunca publicarse en el repositorio.")
