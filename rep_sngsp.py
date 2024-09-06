import os
import requests

import apimoex
import pandas as pd


with requests.Session() as session:
    data = apimoex.get_board_history(session, 'SBERP')
    df = pd.DataFrame(data)
    df.set_index('TRADEDATE', inplace=True)
    
    print(df)

    print(df.head(), '\n')
    print(df.tail(), '\n')
    df.info()

df.to_csv(os.path.join("data", "sberp.csv"))