import pandas as pd
import matplotlib.pyplot as plt

employment_df = pd.read_csv('data/cleaned-data/wa_employment_data.csv')
fuel_price_df = pd.read_csv('data/cleaned-data/pert_metro_fuel_prices.csv')

print(employment_df)
print(fuel_price_df)

plt.figure()
plt.plot()
plt.show()