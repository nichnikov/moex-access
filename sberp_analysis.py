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

def plotMovingAverage(series, n):

    """
    series - dataframe with timeseries
    n - rolling window size 

    """

    rolling_mean = series.rolling(window=n).mean()

    # При желании, можно строить и доверительные интервалы для сглаженных значений
    #rolling_std =  series.rolling(window=n).std()
    #upper_bond = rolling_mean+1.96*rolling_std
    #lower_bond = rolling_mean-1.96*rolling_std

    plt.figure(figsize=(15,5))
    plt.title("Moving average\n window size = {}".format(n))
    plt.plot(rolling_mean, "g", label="Rolling mean trend")

    #plt.plot(upper_bond, "r--", label="Upper Bond / Lower Bond")
    #plt.plot(lower_bond, "r--")
    plt.plot(dataset[n:], label="Actual values")
    plt.legend(loc="upper left")
    plt.grid(True)

if __name__ == "__main__":

    df = pd.read_csv(os.path.join("data", "sberp.csv"))
    print(df)
    df.fillna(0.0, inplace=True)
    
    '''
    res = exponential_smoothing(df.CLOSE, 0.01)
    print(res)
    print(len(res))'''

    with plt.style.context('seaborn-v0_8-whitegrid'):
        alpha = 0.01
        plt.figure(figsize=(20, 8))
        for alpha in [0.1, 0.05, 0.3, 0.01]:
            plt.plot(exponential_smoothing(df.CLOSE, alpha), label="Alpha {}".format(alpha))
        plt.plot(df.CLOSE.values, "c", label = "Actual")
        plt.legend(loc="best")
        plt.axis('tight')
        plt.title("Exponential Smoothing")
        plt.grid(True)
        plt.show()
    
    '''
    plt.figure(figsize=(16,10), dpi= 80)
    plt.plot('TRADEDATE', 'CLOSE', data=df, color='tab:red')
    plt.show()
    '''