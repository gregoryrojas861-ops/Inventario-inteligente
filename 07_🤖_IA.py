import streamlit as st
from database.database import get_db
from database.models import Material
from ai.analysis import analyze_inventory
from ai.recommendation import recommend_purchase

st.title("🤖 Análisis inteligente")
db = get_db()
materials = db.query(Material).all()
analysis = analyze_inventory(materials)

c1, c2, c3 = st.columns(3)
c1.metric("Valor total", f"${analysis['total_value']:,.2f}")
c2.metric("Materiales", analysis["total_materials"])
c3.metric("Bajo reorden", analysis["low_stock"])

st.subheader("Recomendaciones")
for m in materials:
    rec = recommend_purchase(m.stock, m.reorder_point)
    if rec["recommended"]:
        st.warning(f"**{m.name}** → comprar aproximadamente **{rec['quantity']} {m.unit}**. {rec['reason']}")
db.close()
