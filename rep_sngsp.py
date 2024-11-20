"""
50 оттенков matplotlib — The Master Plots (с полным кодом на Python)
https://habr.com/ru/articles/468295/
"""

import os
import requests

import apimoex
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

with requests.Session() as session:
    data = apimoex.get_board_history(session, 'SBERP', start="2024-11-01")
    df = pd.DataFrame(data)
    # df.set_index('TRADEDATE', inplace=True)
    
    print(df)

    print(df.head(), '\n')
    print(df.tail(), '\n')
    df.info()

df.to_csv(os.path.join("data", "sberp_20241119_nov.csv"))
plt.figure(figsize=(16,10), dpi= 80)
plt.plot('TRADEDATE', 'CLOSE', data=df, color='tab:red')
plt.show()