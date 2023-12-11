import pandas as pd
import calendar
import ausdex

PATH = "data/source-data/perth_metro_monthly_ulp_prices.csv"
DATES_COLUMN = 'Month'
PRICE_COLUMN = 'Average'

df = pd.read_csv(PATH, header=1)
df = df[::-1]

dates = df[DATES_COLUMN]

# Adjusting for inflation and converting to dollars
prices = [ausdex.calc_inflation(price, dates[i], location="perth")
         for i, price in enumerate(df[PRICE_COLUMN])]

prices = [val/100 for val in prices]

month_names_to_nums = {month: index for index, month in enumerate(calendar.month_name) if month}
months = [month_names_to_nums[date.split(' ')[0]] for date in dates]
years = [date.split(' ')[1] for date in dates]

new_df = pd.DataFrame(data = {'Year' : years,
                              'Month': months,
                              'ULP Price': prices
                             }
                     )




new_df.to_csv('data/cleaned-data/perth_metro_fuel_prices.csv')