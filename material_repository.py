from database.database import get_db
from database.models import Material

def list_materials():
    db = get_db()
    try:
        return db.query(Material).all()
    finally:
        db.close()

def get_material(material_id):
    db = get_db()
    try:
        return db.get(Material, material_id)
    finally:
        db.close()
