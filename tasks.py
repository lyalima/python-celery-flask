import sqlite3
import requests
from celery import Celery


app = Celery(
    main='tasks',
    broker='pyamqp://guest@localhost//',
    backend='db+sqlite:///celery.sqlite',
)


@app.task
def get_price_crypto(chain, address):
    url = f'https://coins.llama.fi/prices/current/{chain}:{address},coingecko:{chain}'

    response = requests.get(url)
    data = response.json()

    name = chain
    price = data['coins'][f'coingecko:{chain}']['price']
    symbol = data['coins'][f'coingecko:{chain}']['symbol']

    with sqlite3.connect('cryptos.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CRYPTOS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            symbol TEXT,
            moment DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            '''
        )
        cursor.execute('''
        INSERT OR IGNORE INTO CRYPTOS (name, price, symbol)
        VALUES (?, ?, ?)
        ''', (name, price, symbol))
        conn.commit()

    return price, symbol