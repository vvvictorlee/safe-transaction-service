import logging
import os
from dataclasses import dataclass
from typing import Any, Dict, List
from urllib.parse import urljoin

import requests
from eth_utils import to_checksum_address
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

logger = logging.getLogger(__name__)


@dataclass
class CoinMarketCapToken:
    id: int  # CoinMarketCap id
    name: str
    symbol: str
    token_address: str  # For tokens
    logo_uri: str


class CoinMarketCapClient:
    base_url = 'https://pro-api.coinmarketcap.com/'
    base_logo_uri = 'https://s2.coinmarketcap.com/static/img/coins/200x200/'

    def __init__(self, api_token: str):
        self.api_token = api_token
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': api_token,
        }

    def download_file(self, url: str, taget_folder: str, local_filename: str) -> str:
        if not os.path.exists(taget_folder):
            os.makedirs(taget_folder)
        r = requests.get(url, stream=True)
        if not r.ok:
            logger.warning("Image not found for url %s", url)
            return
        with open(os.path.join(taget_folder, local_filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return local_filename

    def get_map(self) -> List[Dict[str, Any]]:
        """
        [
            {'id': 1659,
             'name': 'Gnosis',
             'symbol': 'GNO',
             'slug': 'gnosis-gno',
             'is_active': 1,
             'rank': 137,
             'first_historical_data': '2017-05-01T20:09:54.000Z',
             'last_historical_data': '2020-06-15T09:24:12.000Z',
             'platform': {'id': 1027,
                          'name': 'Ethereum',
                          'symbol': 'ETH',
                          'slug': 'ethereum',
                          'token_address': '0x6810e776880c02933d47db1b9fc05908e5386b96'}
            }, ...
        ]
        :return:
        """
        relative_url = 'v1/cryptocurrency/map'
        url = urljoin(self.base_url, relative_url)
        parameters = {
            # 'listing_status': 'active',
            # 'start': '1',
            'limit': '5000',
        }

        try:
            return requests.get(url, headers=self.headers, params=parameters).json().get('data', [])
        except (ConnectionError, Timeout, TooManyRedirects):
            logger.warning('Problem getting tokens from coinmarketcap', exc_info=True)
            return []

    def get_ethereum_tokens(self) -> List[CoinMarketCapToken]:
        tokens = []
        for token in self.get_map():
            if token and token['is_active'] and token['platform'] and token['platform']['symbol'] == 'ETH':
                try:
                    checksummed_address = to_checksum_address(token['platform']['token_address'])
                    tokens.append(CoinMarketCapToken(token['id'], token['name'], token['symbol'], checksummed_address,
                                                     urljoin(self.base_logo_uri, f'{token["id"]}.png'))
                                  )
                except ValueError:
                    logger.warning('Invalid address %s for token %s with id %d', token['platform']['token_address'],
                                   token['name'], token['id'])

        return tokens
