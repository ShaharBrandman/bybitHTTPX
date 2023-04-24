import httpx

from bs4 import BeautifulSoup

from typing import Optional

from .signature import getSignature

class historicDB:
    '''
    contains a simple scrapper interface for the public.bybit.com database
    '''
    ENDPOINT = 'https://public.bybit.com'
    KLINE_FOR_METATRADER4 = ENDPOINT + '/kline_for_metatrader4/'
    PREMIUM_INDEX = ENDPOINT + '/premium_index/'
    SPOT_INDEX = ENDPOINT + '/spot_index/'
    TRADING = ENDPOINT + '/trading/'

    def __init__(self) -> None:
        pass

    def getEndpoint(self) -> BeautifulSoup:
        res = httpx.get(url = self.ENDPOINT)
        return BeautifulSoup(res.content, 'html.parser')

    def getKlineItems(self) -> list:
        res = httpx.get(url = self.KLINE_FOR_METATRADER4)
        soup = BeautifulSoup(res.content, 'html.parser')

        arr = []

        for e in soup.find_all('a'):
            arr.append(e.get('href'))

        return arr

    def getPremiumIndexItems(self) -> list:
        res = httpx.get(url = self.PREMIUM_INDEX)
        soup = BeautifulSoup(res.content, 'html.parser')

        arr = []

        for e in soup.find_all('a'):
            arr.append(e.get('href'))
            
        return arr

    def getSpotIndexItems(self) -> list:
        res = httpx.get(url = self.SPOT_INDEX)
        soup = BeautifulSoup(res.content, 'html.parser')

        arr = []

        for e in soup.find_all('a'):
            arr.append(e.get('href'))
            
        return arr

    def getTradingItems(self) -> list:
        res = httpx.get(url = self.TRADING)
        soup = BeautifulSoup(res.content, 'html.parser')

        arr = []

        for e in soup.find_all('a'):
            arr.append(e.get('href'))
            
        return arr

    def getKeyItems(self, URL: str) -> list:
        res = httpx.get(url = URL)
        soup = BeautifulSoup(res.content, 'html.parser')

        arr = []

        for e in soup.find_all('a'):
            arr.append(e.get('href'))
            
        return arr

    def getItem(self, URL: str, pathToSave: Optional[str] = None, timeout: Optional[int] = 20) -> any:
        res = httpx.get(
            url = URL,
            headers = {
                'Content-Type': 'text/csv',
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip'
            },
            timeout = timeout
        )

        if pathToSave != None:
            with open(pathToSave, 'wb') as f:
                f.write(res.content)
                f.close()
        else:
            return res.content
        
