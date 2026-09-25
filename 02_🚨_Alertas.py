import streamlit as st
import pandas as pd
from database.database import get_db
from database.models import Alert
from services.alert_service import generate_alerts

st.title("🚨 Alertas")
generate_alerts()
db = get_db()
alerts = db.query(Alert).filter_by(resolved=False).order_by(Alert.created_at.desc()).all()
df = pd.DataFrame([{
    "ID": a.id, "Nivel": a.level, "Mensaje": a.message,
    "Fecha": a.created_at.strftime("%Y-%m-%d %H:%M")
} for a in alerts])
st.dataframe(df, use_container_width=True, hide_index=True)
db.close()
