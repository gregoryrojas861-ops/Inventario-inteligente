import streamlit as st
import pandas as pd
from database.database import get_db
from database.models import AuditLog, User

st.title("🔍 Auditoría")
user = st.session_state.get("user")
if not user or user["role"] not in ("ADMINISTRADOR", "AUDITOR"):
    st.error("No tienes permisos para consultar auditoría.")
    st.stop()

db = get_db()
rows = []
for log in db.query(AuditLog).order_by(AuditLog.created_at.desc()).all():
    u = db.get(User, log.user_id)
    rows.append({
        "Fecha": log.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "Usuario": u.username if u else "Desconocido",
        "Acción": log.action, "Módulo": log.module,
        "Registro": log.record_id, "Descripción": log.description
    })
st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
db.close()
