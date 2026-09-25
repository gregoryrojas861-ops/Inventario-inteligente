import streamlit as st
import pandas as pd
from database.database import get_db
from database.models import Movement, Material

st.title("📋 Movimientos")
db = get_db()
rows = []
for m in db.query(Movement).order_by(Movement.created_at.desc()).all():
    material = db.get(Material, m.material_id)
    rows.append({
        "Fecha": m.created_at.strftime("%Y-%m-%d %H:%M"),
        "Material": material.name if material else "Eliminado",
        "Tipo": m.movement_type, "Cantidad": m.quantity,
        "Anterior": m.previous_stock, "Resultado": m.resulting_stock,
        "Motivo": m.reason
    })
st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
db.close()
