import streamlit as st
import pandas as pd
from database.database import get_db
from database.models import Purchase, Supplier, Material

st.title("🛒 Compras")
db = get_db()
suppliers = db.query(Supplier).all()
materials = db.query(Material).all()

if suppliers and materials:
    with st.form("purchase"):
        supplier = st.selectbox("Proveedor", suppliers, format_func=lambda x: x.name)
        material = st.selectbox("Material", materials, format_func=lambda x: x.name)
        quantity = st.number_input("Cantidad", min_value=0.01)
        cost = st.number_input("Costo unitario", min_value=0.0)
        status = st.selectbox("Estado", ["BORRADOR", "PENDIENTE", "APROBADA", "EN TRÁNSITO", "RECIBIDA", "CANCELADA"])
        if st.form_submit_button("Crear orden"):
            db.add(Purchase(supplier_id=supplier.id, material_id=material.id,
                            quantity=quantity, unit_cost=cost, status=status))
            db.commit()
            st.success("Orden creada.")
else:
    st.info("Primero crea proveedores y materiales.")

rows = []
for p in db.query(Purchase).order_by(Purchase.created_at.desc()).all():
    s, m = db.get(Supplier, p.supplier_id), db.get(Material, p.material_id)
    rows.append({"ID": p.id, "Proveedor": s.name, "Material": m.name, "Cantidad": p.quantity,
                 "Estado": p.status, "Costo": p.unit_cost})
st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
db.close()
