import pandas as pd
import calendar

PATH = "data/source-data/perth_metro_monthly_ulp_prices.csv"
DATES_COLUMN_NAME = 'Month'
PRICE_COLUMN_NAME = 'Average'

df = pd.read_csv(PATH, header=1)
df = df[::-1]

dates = df[DATES_COLUMN_NAME]

month_names_to_nums = {month: index for index, month in enumerate(calendar.month_name) if month}
months = [month_names_to_nums[date.split(' ')[0]] for date in dates]
years = [date.split(' ')[1] for date in dates]

new_df = pd.DataFrame(data = {'Year' : years,
                              'Month': months,
                              'ULP Price': df[PRICE_COLUMN_NAME]
                             }
                     )

new_df.to_csv('data/cleaned-data/perth_metro_fuel_prices.csv')