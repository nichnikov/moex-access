"""
https://external.software/archives/12582
"""
import os
import requests
import pandas as pd
from apimoex import get_market_candles
import pyodbc

def execute_query(conn: pyodbc.Connection, query: str) -> None:
    """Выполняет SQL-запрос."""
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()


def connect_to_access_db(db_file: str) -> pyodbc.Connection:
    """Устанавливает соединение с базой данных Access."""
    connection_string = rf'DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_file};'
    return pyodbc.connect(connection_string)

conn = connect_to_access_db(os.path.join('data', 'Finance.accdb'))


securities = ["SBER", "SNGSP", "ROSN", "MGNT", "LKOH", "YDEX"]

for security in securities:
    execute_query(conn, "DELETE FROM securities_price WHERE security = '{}'".format(security))
    with requests.Session() as session:
        data = get_market_candles(session=session, security=security, start="2025-02-01", end="2025-02-21", interval=60)
        data_df = pd.DataFrame(data)


    for line in list(data_df.itertuples(index=False, name=None)):
        line = (security, ) + line
        q = 'INSERT INTO securities_price (security, begin, open, close, high, low, volume, quantity) VALUES {}'.format(line)
        execute_query(conn, q)