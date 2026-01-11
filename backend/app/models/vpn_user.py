from sqlalchemy import Column, Integer, String
from app.core.database import Base

class VPNUser(Base):
    __tablename__ = "vpn_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    public_key = Column(String)
    private_key = Column(String)
    ip_address = Column(String)
    role = Column(String)
    status = Column(String, default="active")
