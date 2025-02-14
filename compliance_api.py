from fastapi import FastAPI
from ai_risk_scoring.risk_model import check_sanctions
from crypto_compliance.blockchain_monitor import check_crypto_wallet

app = FastAPI()

@app.post("/check_transaction")
async def check_transaction(transaction: dict):
    risk = check_sanctions(transaction)
    return {"transaction": transaction, "risk_assessment": risk}

@app.get("/check_wallet/{wallet_address}")
async def check_wallet(wallet_address: str):
    return check_crypto_wallet(wallet_address)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
