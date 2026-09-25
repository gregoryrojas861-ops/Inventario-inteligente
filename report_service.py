import pandas as pd

def materials_dataframe(materials):
    return pd.DataFrame([{
        "Código": m.code,
        "Nombre": m.name,
        "Categoría": m.category,
        "Stock": m.stock,
        "Costo": m.unit_cost,
        "Valor": m.stock * m.unit_cost
    } for m in materials])
