import streamlit as st
from database.database import get_db
from database.models import Material, PhysicalInventory
from services.audit_service import log_action

st.title("📦 Inventario físico")
user = st.session_state.get("user")
if not user:
    st.stop()

db = get_db()
materials = db.query(Material).all()
if materials:
    material = st.selectbox("Material", materials, format_func=lambda x: f"{x.code} — {x.name}")
    physical = st.number_input("Cantidad física", min_value=0.0)
    if st.button("Registrar conteo"):
        diff = physical - material.stock
        db.add(PhysicalInventory(material_id=material.id, system_quantity=material.stock,
                                  physical_quantity=physical, difference=diff, user_id=user["id"]))
        db.commit()
        log_action(user["id"], "CONTEO", "INVENTARIO_FISICO", material.id,
                   material.stock, physical, f"Diferencia: {diff}")
        st.success(f"Diferencia registrada: {diff}")
else:
    st.info("No existen materiales.")
db.close()
