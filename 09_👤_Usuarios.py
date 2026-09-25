import streamlit as st
from database.database import get_db
from database.models import User
from services.auth_service import hash_password

st.title("👤 Usuarios")
user = st.session_state.get("user")
if not user or user["role"] != "ADMINISTRADOR":
    st.error("Solo el administrador puede gestionar usuarios.")
    st.stop()

db = get_db()
with st.form("new_user"):
    username = st.text_input("Usuario")
    full_name = st.text_input("Nombre completo")
    password = st.text_input("Contraseña", type="password")
    role = st.selectbox("Rol", ["ADMINISTRADOR", "SUPERVISOR", "ALMACENERO", "ANALISTA", "AUDITOR"])
    if st.form_submit_button("Crear usuario"):
        if not username or not password or not full_name:
            st.error("Completa todos los campos.")
        elif db.query(User).filter_by(username=username).first():
            st.error("El usuario ya existe.")
        else:
            db.add(User(username=username, full_name=full_name,
                        password_hash=hash_password(password), role=role))
            db.commit()
            st.success("Usuario creado.")
st.dataframe([{"Usuario": u.username, "Nombre": u.full_name, "Rol": u.role, "Activo": u.active}
              for u in db.query(User).all()], use_container_width=True, hide_index=True)
db.close()
