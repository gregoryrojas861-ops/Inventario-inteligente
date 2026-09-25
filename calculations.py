def inventory_value(stock, unit_cost):
    return stock * unit_cost

def reorder_point(average_daily_consumption, lead_time_days, safety_stock=0):
    return average_daily_consumption * lead_time_days + safety_stock

def coverage_days(stock, average_daily_consumption):
    if average_daily_consumption <= 0:
        return None
    return stock / average_daily_consumption

def inventory_turnover(consumption_value, average_inventory_value):
    if average_inventory_value <= 0:
        return 0
    return consumption_value / average_inventory_value
