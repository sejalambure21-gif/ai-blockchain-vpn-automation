from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.vpn_user import VPNUser
from app.schemas.vpn import VPNUserCreate

router = APIRouter(prefix="/vpn", tags=["VPN"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create-user")
def create_user(user: VPNUserCreate, db: Session = Depends(get_db)):
    vpn_user = VPNUser(
        username=user.username,
        role=user.role,
        ip_address="10.0.0.2"  # placeholder
    )
    db.add(vpn_user)
    db.commit()
    db.refresh(vpn_user)
    return vpn_user

@router.get("/generate-config/{user_id}")
def generate_config(user_id: int):
    return {
        "message": "WireGuard config will be generated here"
    }
