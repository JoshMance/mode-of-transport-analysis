import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned-data/wa_employment_data.csv')

plt.figure()
plt.plot(df['Number of Employed People'])
plt.show()