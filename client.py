import httpx

from typing import Optional

from datetime import datetime

from .signature import getSignature

class BybitClient:
    def __init__(self, url: str, apiKey: str, apiSecret: str, recvWindow: Optional[int] = 5000) -> None:
        self.url = url
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.recvWindow = recvWindow

    def getHeader(self, payload: dict) -> dict:
        t = datetime.now().timestamp() / 10

        self.headers = {
            'X-BAPI-API-KEY': self.apiKey,
            'X-BAPI-SIGN': getSignature(
                self.apiKey,
                self.apiSecret,
                self.recvWindow,
                t,
                payload
            ),
            'X-BAPI-TIMESTAMP': t,
            'X-BAPI-RECV-WINDOW': self.recvWindow,
            'Content-Type': 'application/json'
        }

    def getkLines(self, category: str, symbol: str, interval: str, fromTimestamp: str, limit: Optional[int] = 1000) -> httpx.Response:
        endpoint = '/v5/market/kline'
        return self.getRequest(endpoint, params = {
            'category': category,
            'symbol': symbol,
            'interval': interval,
            'from_time': fromTimestamp,
            'limit': limit
        })

    def getRequest(self, endpoint: str, params: dict) -> httpx.Response:
        '''
        POST METHOD REQUEST
        '''
        return httpx.get(
                url = self.url + endpoint,
                params = params,
                headers = self.getHeader(params)
        )
