from database.database import get_db
from database.models import AuditLog

def log_action(user_id, action, module, record_id="", old_value="", new_value="", description=""):
    db = get_db()
    try:
        db.add(AuditLog(
            user_id=user_id, action=action, module=module, record_id=str(record_id),
            old_value=str(old_value), new_value=str(new_value), description=description
        ))
        db.commit()
    finally:
        db.close()
