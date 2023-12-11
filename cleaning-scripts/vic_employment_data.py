import pandas as pd

# https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/latest-release#data-downloads

SHEET_NAME = 'Data1'
YEAR_COLUMN_NAME = 'Unnamed: 0'
NUM_COLUMN_NAME = "Employed total ;  Persons ;"
HEADER_DATA_OFFSET = 9

df = pd.read_excel('data/source-data/abs_vic_employment_data.xlsx', 
                   sheet_name=[SHEET_NAME]
                   ).pop(SHEET_NAME)


dates = [str(date).split(" ")[0]
         for date in df[YEAR_COLUMN_NAME][HEADER_DATA_OFFSET:]]
years = [date.split("-")[0] for date in dates]
months = [date.split("-")[1] for date in dates]

number_employed_people = [num*1000 for num in df[NUM_COLUMN_NAME][HEADER_DATA_OFFSET:]]


new_df = pd.DataFrame(data = {'Year' : years,
                              'Month': months,
                              'Number of Employed People': number_employed_people
                             }
                     )

new_df.to_csv('data/cleaned-data/vic_employment_data.csv')
