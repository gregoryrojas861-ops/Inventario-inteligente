import streamlit as st
from database.database import get_db
from database.models import Material
from utils.calculations import inventory_value

st.title("📊 KPI")
db = get_db()
materials = db.query(Material).all()
total_value = sum(inventory_value(m.stock, m.unit_cost) for m in materials)
total_stock = sum(m.stock for m in materials)
low = sum(1 for m in materials if m.stock <= m.reorder_point)
critical = sum(1 for m in materials if m.criticality == "ALTA")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Valor inventario", f"${total_value:,.2f}")
c2.metric("Unidades", f"{total_stock:,.2f}")
c3.metric("Bajo reorden", low)
c4.metric("Críticos", critical)
db.close()
