def positive_number(value, field_name="valor"):
    if value < 0:
        raise ValueError(f"{field_name} no puede ser negativo.")
    return value
