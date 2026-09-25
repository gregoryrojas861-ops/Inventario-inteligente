def recommend_purchase(stock, reorder_point_value, average_daily_consumption=0, lead_time_days=0):
    if stock > reorder_point_value:
        return {"recommended": False, "quantity": 0, "reason": "El stock está por encima del punto de reorden."}
    target = max(reorder_point_value, average_daily_consumption * max(lead_time_days, 1))
    quantity = max(0, target - stock)
    return {"recommended": quantity > 0, "quantity": round(quantity, 2), "reason": "Se recomienda reponer inventario."}
