from database.database import get_db
from database.models import Material, Supplier

def seed():
    db = get_db()
    try:
        if not db.query(Material).first():
            materials = [
                Material(code="MAT-001", name="Papel industrial", category="Materia prima",
                         unit="kg", unit_cost=2.5, stock=500, min_stock=100, max_stock=1000, reorder_point=200),
                Material(code="REP-001", name="Rodamiento", category="Repuesto",
                         unit="unidad", unit_cost=18, stock=12, min_stock=10, max_stock=50, reorder_point=15,
                         criticality="ALTA"),
                Material(code="INS-001", name="Guantes", category="Insumo",
                         unit="par", unit_cost=3.2, stock=80, min_stock=20, max_stock=200, reorder_point=40),
            ]
            db.add_all(materials)
        if not db.query(Supplier).first():
            db.add_all([
                Supplier(code="PROV-001", name="Proveedor Industrial A"),
                Supplier(code="PROV-002", name="Proveedor Industrial B")
            ])
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    seed()
    print("Datos de prueba creados.")
