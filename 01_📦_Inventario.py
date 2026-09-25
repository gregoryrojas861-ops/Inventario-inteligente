import streamlit as st
import pandas as pd
from database.database import get_db
from database.models import Material
from services.inventory_service import create_material, update_stock
from services.alert_service import generate_alerts

st.title("📦 Inventario")
user = st.session_state.get("user")
if not user:
    st.stop()

generate_alerts()
db = get_db()
materials = db.query(Material).order_by(Material.name).all()

tab1, tab2 = st.tabs(["Inventario", "Nuevo material"])

with tab1:
    rows = [{
        "ID": m.id, "Código": m.code, "Nombre": m.name, "Categoría": m.category,
        "Stock": m.stock, "Mínimo": m.min_stock, "Reorden": m.reorder_point,
        "Costo": m.unit_cost, "Almacén": m.warehouse, "Estado": m.status
    } for m in materials]
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    if materials:
        selected = st.selectbox("Material", materials, format_func=lambda x: f"{x.code} — {x.name}")
        c1, c2 = st.columns(2)
        with c1:
            qty = st.number_input("Cantidad", min_value=0.01, value=1.0)
            reason = st.text_input("Motivo", "Movimiento manual")
        with c2:
            if st.button("Registrar entrada"):
                update_stock(selected.id, qty, "ENTRADA", user["id"], reason)
                st.success("Entrada registrada.")
                st.rerun()
            if st.button("Registrar salida"):
                try:
                    update_stock(selected.id, qty, "SALIDA", user["id"], reason)
                    st.success("Salida registrada.")
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
db.close()

with tab2:
    with st.form("material_form"):
        code = st.text_input("Código *")
        name = st.text_input("Nombre *")
        category = st.text_input("Categoría", "General")
        unit = st.text_input("Unidad", "unidad")
        cost = st.number_input("Costo unitario", min_value=0.0)
        stock = st.number_input("Stock inicial", min_value=0.0)
        minimum = st.number_input("Stock mínimo", min_value=0.0)
        maximum = st.number_input("Stock máximo", min_value=0.0)
        reorder = st.number_input("Punto de reorden", min_value=0.0)
        warehouse = st.text_input("Almacén", "Principal")
        submitted = st.form_submit_button("Crear material")
        if submitted:
            if not code or not name:
                st.error("Código y nombre son obligatorios.")
            else:
                try:
                    create_material({
                        "code": code, "name": name, "category": category, "unit": unit,
                        "unit_cost": cost, "stock": stock, "min_stock": minimum,
                        "max_stock": maximum, "reorder_point": reorder, "warehouse": warehouse
                    }, user["id"])
                    st.success("Material creado.")
                    st.rerun()
                except Exception as e:
                    st.error(f"No se pudo crear: {e}")
