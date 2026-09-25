from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from database.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=False)
    role = Column(String(30), nullable=False, default="ALMACENERO")
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True)
    code = Column(String(80), unique=True, nullable=False, index=True)
    barcode = Column(String(120), unique=True, nullable=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, default="")
    category = Column(String(100), default="General")
    unit = Column(String(30), default="unidad")
    supplier = Column(String(150), default="")
    unit_cost = Column(Float, default=0)
    stock = Column(Float, default=0)
    min_stock = Column(Float, default=0)
    max_stock = Column(Float, default=0)
    safety_stock = Column(Float, default=0)
    reorder_point = Column(Float, default=0)
    location = Column(String(100), default="")
    warehouse = Column(String(100), default="Principal")
    criticality = Column(String(30), default="MEDIA")
    status = Column(String(30), default="ACTIVO")
    expiration_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Movement(Base):
    __tablename__ = "movements"
    id = Column(Integer, primary_key=True)
    material_id = Column(Integer, ForeignKey("materials.id"), nullable=False)
    movement_type = Column(String(30), nullable=False)
    quantity = Column(Float, nullable=False)
    reason = Column(String(150), default="")
    previous_stock = Column(Float, nullable=False)
    resulting_stock = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    lot = Column(String(100), default="")
    serial_number = Column(String(100), default="")
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    material = relationship("Material")
    user = relationship("User")

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    action = Column(String(100), nullable=False)
    module = Column(String(100), nullable=False)
    record_id = Column(String(100), default="")
    old_value = Column(Text, default="")
    new_value = Column(Text, default="")
    description = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    code = Column(String(80), unique=True, nullable=False)
    contact = Column(String(150), default="")
    phone = Column(String(50), default="")
    email = Column(String(150), default="")
    address = Column(Text, default="")

class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    material_id = Column(Integer, ForeignKey("materials.id"), nullable=False)
    quantity = Column(Float, nullable=False)
    status = Column(String(40), default="BORRADOR")
    unit_cost = Column(Float, default=0)
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    material_id = Column(Integer, ForeignKey("materials.id"), nullable=True)
    level = Column(String(30), nullable=False)
    message = Column(Text, nullable=False)
    resolved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class PhysicalInventory(Base):
    __tablename__ = "physical_inventory"
    id = Column(Integer, primary_key=True)
    material_id = Column(Integer, ForeignKey("materials.id"), nullable=False)
    system_quantity = Column(Float, nullable=False)
    physical_quantity = Column(Float, nullable=False)
    difference = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(30), default="PENDIENTE")
    created_at = Column(DateTime, default=datetime.utcnow)
