from database.database import get_db
from database.models import Material
from services.audit_service import log_action

def create_material(data, user_id):
    db = get_db()
    try:
        material = Material(**data)
        db.add(material)
        db.commit()
        db.refresh(material)
        log_action(user_id, "CREAR", "MATERIALES", material.id, "", data, f"Material {material.code} creado")
        return material
    finally:
        db.close()

def update_stock(material_id, quantity, movement_type, user_id, reason=""):
    db = get_db()
    try:
        material = db.get(Material, material_id)
        if not material:
            raise ValueError("Material no encontrado.")
        previous = material.stock
        if movement_type == "ENTRADA":
            material.stock += quantity
        elif movement_type == "SALIDA":
            if material.stock - quantity < 0:
                raise ValueError("El inventario no puede quedar negativo.")
            material.stock -= quantity
        else:
            raise ValueError("Tipo de movimiento inválido.")
        db.commit()
        from database.models import Movement
        movement = Movement(
            material_id=material.id, movement_type=movement_type, quantity=quantity,
            reason=reason, previous_stock=previous, resulting_stock=material.stock,
            user_id=user_id
        )
        db.add(movement)
        db.commit()
        log_action(user_id, movement_type, "INVENTARIO", material.id, previous, material.stock, reason)
        return material.stock
    finally:
        db.close()
