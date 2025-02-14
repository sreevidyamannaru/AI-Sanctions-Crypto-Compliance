import json

HIGH_RISK_WALLETS = {"3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy", "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}

def check_crypto_wallet(wallet_address):
    return {"wallet": wallet_address, "risk": "High" if wallet_address in HIGH_RISK_WALLETS else "Low"}

print(check_crypto_wallet("3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy"))
