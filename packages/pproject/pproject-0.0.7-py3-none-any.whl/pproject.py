import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import datetime


import pandas as pd

# データの作成
data = {
    'Model': [
        'iPhone 15 Pro Max', 'iPhone 15 Pro', 'iPhone 15 Plus', 'iPhone 15', 'iPhone 14 Plus',
        'iPhone 14 Pro Max', 'iPhone 14 Pro', 'iPhone 14', 'iPhone SE(第3世代)', 'iPhone 13 Pro Max',
        'iPhone 13 mini', 'iPhone 13 Pro', 'iPhone 13', 'iPhone 12 Pro Max', 'iPhone 12 mini',
        'iPhone 12 Pro', 'iPhone 12', 'iPhone SE(第2世代)', 'iPhone 11 Pro Max', 'iPhone 11 Pro',
        'iPhone 11', 'iPhone XS Max', 'iPhone XS', 'iPhone XR', 'iPhone X', 'iPhone 8 Plus',
        'iPhone 8', 'iPhone 7 Plus', 'iPhone 7', 'iPhone SE(第1世代)', 'iPhone 6s Plus',
        'iPhone 6s', 'iPhone 6 Plus', 'iPhone 6', 'iPhone 5s', 'iPhone 5c', 'iPhone 5',
        'iPhone 4S', 'iPhone 4', 'iPhone 3GS', 'iPhone 3G'
    ],
    'Year': [
        2023, 2023, 2023, 2023, 2022, 2022, 2022, 2022, 2022, 2021, 2021, 2021, 2021, 2020, 2020,
        2020, 2020, 2020, 2019, 2019, 2019, 2018, 2018, 2018, 2017, 2017, 2017, 2016, 2016, 2016,
        2015, 2015, 2014, 2014, 2013, 2013, 2012, 2011, 2010, 2009, 2008
    ],
    'Date': [
        '09-22', '09-22', '09-22', '09-22', '10-07', '09-16', '09-16', '09-16', '03-18', '09-24',
        '09-24', '09-24', '09-24', '11-13', '11-13', '10-23', '10-23', '04-24', '09-20', '09-20',
        '09-20', '09-21', '09-21', '10-26', '11-03', '09-22', '09-22', '09-16', '09-16', '03-31',
        '09-25', '09-25', '09-19', '09-19', '09-20', '09-20', '09-21', '10-14', '06-24', '06-19', '07-11'
    ],
    'Price': [
        189800, 159800, 139800, 124800, 134800, 164800, 149800, 119800, 57800, 122545, 78909, 111636,
        89818, 117800, 74800, 106800, 85800, 44800, 119800, 106800, 74800, 124800, 112800, 84800,
        112800, 89800, 78800, 85800, 72800, 52800, 98800, 86800, 79800, 67800, 85680, 95760, 61680,
        46080, 46080, 69120, 23040
    ],
    'Classification': [
        4, 3, 2, 1, 4, 3, 2, 1, 0, 4, 3, 2, 1, 4, 3, 2, 1, 0, 3, 2, 1, 3, 2, 1, 1, 2, 1, 2, 1, 0,
        2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1
    ]
}

# データフレームの作成
df = pd.DataFrame(data)

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

""" Predicted_price_change_in_XX_years(100) """
