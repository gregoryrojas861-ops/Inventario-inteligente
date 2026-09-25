ROLES = {
    "ADMINISTRADOR": {"*"},
    "SUPERVISOR": {"inventory", "movements", "purchases", "reports", "approvals"},
    "ALMACENERO": {"inventory", "movements"},
    "ANALISTA": {"inventory", "reports", "kpis", "ai"},
    "AUDITOR": {"audit", "reports"}
}

def has_permission(role, module):
    permissions = ROLES.get(role, set())
    return "*" in permissions or module in permissions
