from pydantic import BaseModel

class VPNUserCreate(BaseModel):
    username: str
    role: str

class VPNUserResponse(BaseModel):
    id: int
    username: str
    ip_address: str
    role: str
    status: str
