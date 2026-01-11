from fastapi import FastAPI
from app.api import vpn
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Blockchain VPN Automation")

app.include_router(vpn.router)

@app.get("/")
def root():
    return {"status": "Backend running"}
