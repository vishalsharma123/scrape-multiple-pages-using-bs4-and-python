import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

bridge_height = {'meters':[10.26,12,26,25,23,24,23,29,34,36,95,46]}

df = pd.DataFrame(bridge_height)
df['STD'] = pd.rolling_std(df['meters'],2)
print(df)

df.plot()
plt.show()
