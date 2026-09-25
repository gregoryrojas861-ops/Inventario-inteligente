def analyze_inventory(materials):
    total_value = sum(m.stock * m.unit_cost for m in materials)
    low_stock = [m for m in materials if m.stock <= m.reorder_point]
    return {
        "total_value": total_value,
        "total_materials": len(materials),
        "low_stock": len(low_stock),
        "critical": len([m for m in materials if m.criticality == "ALTA"])
    }
