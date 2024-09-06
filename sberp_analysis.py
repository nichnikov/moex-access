"""
Открытый курс машинного обучения. Тема 9. Анализ временных рядов с помощью Python
https://habr.com/ru/companies/ods/articles/327242/
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def exponential_smoothing(series, alpha):
    result = [series[0]] # first value is same as series
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n-1])
    return result

df = pd.read_csv(os.path.join("data", "sberp.csv"))
print(df)



plt.figure(figsize=(16,10), dpi= 80)
plt.plot('TRADEDATE', 'CLOSE', data=df, color='tab:red')
plt.show()
