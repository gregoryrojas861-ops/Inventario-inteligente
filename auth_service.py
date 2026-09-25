import bcrypt
from database.database import get_db
from database.models import User

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def create_default_admin():
    db = get_db()
    try:
        user = db.query(User).filter(User.username.in_(["admin", "Gregory1109"])).first()
        if user:
            user.username = "Gregory1109"
            user.password_hash = hash_password("Yosnier1109")
            if not user.full_name:
                user.full_name = "Administrador"
            if not user.role:
                user.role = "ADMINISTRADOR"
            db.commit()
            return

        db.add(User(
            username="Gregory1109",
            password_hash=hash_password("Yosnier1109"),
            full_name="Administrador",
            role="ADMINISTRADOR"
        ))
        db.commit()
    finally:
        db.close()

def authenticate_user(username, password):
    db = get_db()
    try:
        user = db.query(User).filter_by(username=username, active=True).first()
        if user and verify_password(password, user.password_hash):
            return {"id": user.id, "username": user.username, "full_name": user.full_name, "role": user.role}
        return None
    finally:
        db.close()
