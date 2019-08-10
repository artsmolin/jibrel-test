import logging
from dataclasses import dataclass
from typing import List
from urllib.parse import urljoin

import requests


logger = logging.getLogger(__name__)


@dataclass
class Candle:
    mts: int
    close: int
    volume: float


class BitfinexAPI:
    BASE_URL = 'https://api-pub.bitfinex.com/'
    CANDLES_PATH = '/v2/candles'

    TIME_FRAMES = ('1m', '5m', '15m', '30m', '1h', '3h', '6h', '12h', '1D', '7D', '14D', '1M')
    SYMBOLS = ('tBTCUSD', 'tETHUSD', 'tXRPUSD', 'tLTCUSD', 'tZECUSD')
    SECTIONS = ('hist', 'last')

    def get_candles(self, symbol: str, time_frame: str, section: str = 'hist', limit: int = 5000,
                    after: int = None) -> List[Candle]:
        if symbol not in self.SYMBOLS:
            raise Exception(f'Invalid symbol ({symbol}). Allowed values: {self.SYMBOLS}')

        if time_frame not in self.TIME_FRAMES:
            raise Exception(f'Invalid time_frame ({time_frame}). Allowed values: {self.TIME_FRAMES}')

        if section not in self.SECTIONS:
            raise Exception(f'Invalid section ({section}). Allowed values: {self.SECTIONS}')

        url = urljoin(self.BASE_URL, f'{self.CANDLES_PATH}/trade:{time_frame}:{symbol}/{section}')
        params = {
            'limit': limit,
            'start': after,
        }

        r = requests.get(url, params=params)

        logger.info(r.url)

        r.raise_for_status()

        raw_candles = r.json()
        filtered_raw_candles = raw_candles[:-1] if after else raw_candles

        return [
            Candle(
                candle_data[0],
                candle_data[2],
                candle_data[5],
            )
            for candle_data in filtered_raw_candles
        ]
