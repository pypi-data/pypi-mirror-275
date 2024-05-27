import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import datetime

df=pd.read_excel('./data/iphone.xlsx')

df['Year'] = df['Release Date'].dt.year
df['Date'] = df['Release Date'].dt.strftime('%m-%d')
df = df.drop(columns=['Release Date'])

df = df[['Model', 'Year', 'Date', 'Price', 'Classification']]
df['Price'] = df['Price'].str.replace('円', '').str.replace(',', '').astype(int)

def price_fluctuation_now():    
    plt.figure(figsize=(8, 4))
    for classification, group in df.groupby('Classification'):
        plt.plot(group['Year'], group['Price'], marker='o', label=f'Classification {classification}')

    plt.xlabel('Year')
    plt.ylabel('Price (yen)')
    plt.title('iPhone Prices by Year')
    plt.legend()
    plt.grid(True)
    plt.show()

""" price_fluctuation_now() """


df_class1 = df[df['Classification'] == 1]
def Predicted_price_change_in_XX_years(XX):
    # 線形回帰モデルの訓練
    X = df_class1['Year'].values.reshape(-1, 1)
    y = df_class1['Price'].values
    model = LinearRegression()
    model.fit(X, y)
    current_year = datetime.datetime.now().year


    future_years = np.arange(df_class1['Year'].min(), current_year+XX).reshape(-1, 1)
    predicted_prices = model.predict(future_years)

    # 結果のプロット
    plt.figure(figsize=(8, 3))
    plt.scatter(df_class1['Year'], df_class1['Price'], color='blue', label='Actual Prices')
    plt.plot(future_years, predicted_prices, color='red', linestyle='--', label='Predicted Prices')
    plt.xlabel('Year')
    plt.ylabel('Price (yen)')
    plt.title('Predicted price change for iphone in XX years')
    plt.legend()
    plt.grid(True)
    plt.show()

""" Predicted_price_change_in_XX_years(10) """
