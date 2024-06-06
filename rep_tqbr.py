"""
    Перечень акций, торгующихся в режиме TQBR (описание запроса):
"""
import os
import requests

import apimoex
import pandas as pd


request_url = ('https://iss.moex.com/iss/engines/stock/'
               'markets/shares/boards/TQBR/securities.json')
arguments = {'securities.columns': ('SECID,'
                                    'REGNUMBER,'
                                    'LOTSIZE,'
                                    'SHORTNAME')}
with requests.Session() as session:
    iss = apimoex.ISSClient(session, request_url, arguments)
    data = iss.get()
    print(type(data))
    df = pd.DataFrame(data['securities'])
    df.to_csv(os.path.join("data", "tqbr_shares.csv"), index=False)
    print(df)
    df.set_index('SECID', inplace=True)
    print(df.head(), '\n')
    print(df.tail(), '\n')
    df.info()