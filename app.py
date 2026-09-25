import streamlit as st
from config import settings
from database.db import init_db
from services.auth_service import authenticate_user, create_default_admin

st.set_page_config(page_title="Inventario Industrial", page_icon="📦", layout="wide")

init_db()
create_default_admin()

if "user" not in st.session_state:
    st.session_state.user = None

def login():
    st.title("📦 Sistema Inteligente de Control de Inventario Industrial")
    st.caption("Acceso seguro al sistema")
    with st.form("login"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        submitted = st.form_submit_button("Iniciar sesión", use_container_width=True)
        if submitted:
            user = authenticate_user(username, password)
            if user:
                st.session_state.user = user
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")

if not st.session_state.user:
    login()
else:
    user = st.session_state.user
    st.sidebar.success(f"👤 {user['full_name']} — {user['role']}")
    if st.sidebar.button("Cerrar sesión"):
        st.session_state.user = None
        st.rerun()

    st.title("📊 Dashboard")
    st.write(f"Bienvenido, **{user['full_name']}**.")
    st.info("Usa el menú lateral para administrar el inventario. Las páginas se encuentran en la carpeta pages/.")
    st.metric("Entorno", settings.APP_ENV)
    st.metric("Base de datos", "SQLite" if settings.DATABASE_URL.startswith("sqlite") else "PostgreSQL")
