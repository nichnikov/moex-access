import os
import requests
import pandas as pd
from apimoex import get_market_candles


with requests.Session() as session:
    data = get_market_candles(session=session, security="SBER", start="2023-05-06", end="2024-06-06", interval=60)
    print(data)
    data_df = pd.DataFrame(data)

print(data_df)
data_df.to_csv(os.path.join("data", "sber_stocks_Y.csv"), index=False)
    