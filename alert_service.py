from database.database import get_db
from database.models import Material, Alert

def generate_alerts():
    db = get_db()
    try:
        for material in db.query(Material).all():
            if material.stock <= 0:
                exists = db.query(Alert).filter_by(material_id=material.id, resolved=False, level="CRÍTICA").first()
                if not exists:
                    db.add(Alert(material_id=material.id, level="CRÍTICA",
                                 message=f"{material.name}: inventario agotado."))
            elif material.stock <= material.reorder_point:
                exists = db.query(Alert).filter_by(material_id=material.id, resolved=False, level="ADVERTENCIA").first()
                if not exists:
                    db.add(Alert(material_id=material.id, level="ADVERTENCIA",
                                 message=f"{material.name}: alcanzó el punto de reorden."))
        db.commit()
    finally:
        db.close()
