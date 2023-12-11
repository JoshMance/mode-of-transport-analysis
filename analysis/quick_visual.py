import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

employment_df = pd.read_csv('data/cleaned-data/wa_employment_data.csv')
fuel_price_df = pd.read_csv('data/cleaned-data/perth_metro_fuel_prices.csv')

df = employment_df.merge(fuel_price_df, on=['Year', 'Month'])
df = df.drop(['Unnamed: 0_x', 'Unnamed: 0_y'], axis=1)

#employment_and_price = list(zip(df['ULP Price'], df['Number of Employed People']))
#employment_and_price.sort()

y1 = df['ULP Price']/np.mean(fuel_price_df['ULP Price'])
y2 = df['Number of Employed People']/np.mean(employment_df['Number of Employed People'])
x = list(range(len(y1)))

plt.figure(figsize=(20, 10))
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()


