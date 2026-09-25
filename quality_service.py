VALID_STATES = {"APROBADO", "PENDIENTE DE INSPECCIÓN", "RECHAZADO", "CUARENTENA"}

def validate_quality_state(state):
    if state not in VALID_STATES:
        raise ValueError("Estado de calidad inválido.")
    return state
