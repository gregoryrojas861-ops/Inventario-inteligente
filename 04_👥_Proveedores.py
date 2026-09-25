import streamlit as st
from database.database import get_db
from database.models import Supplier
import pandas as pd

st.title("👥 Proveedores")
db = get_db()
with st.form("supplier"):
    code = st.text_input("Código")
    name = st.text_input("Nombre")
    contact = st.text_input("Contacto")
    phone = st.text_input("Teléfono")
    email = st.text_input("Correo")
    submitted = st.form_submit_button("Guardar")
    if submitted:
        if not code or not name:
            st.error("Código y nombre son obligatorios.")
        else:
            try:
                db.add(Supplier(code=code, name=name, contact=contact, phone=phone, email=email))
                db.commit()
                st.success("Proveedor creado.")
            except Exception as e:
                db.rollback()
                st.error(str(e))
rows = [{"Código": x.code, "Nombre": x.name, "Contacto": x.contact, "Teléfono": x.phone, "Correo": x.email}
        for x in db.query(Supplier).all()]
st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
db.close()
