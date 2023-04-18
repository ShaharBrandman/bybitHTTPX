import hmac
import hashlib

def getSignature(apiKey: str, apiSecret: str, recvWindow: int, timestamp: int, payload: dict) -> str:
        
    param= str(timestamp) + apiKey + str(recvWindow) + str(payload)
    
    hash = hmac.new(bytes(apiSecret, "utf-8"), param.encode("utf-8"), hashlib.sha256)
    
    signature = hash.hexdigest()

    return signature
