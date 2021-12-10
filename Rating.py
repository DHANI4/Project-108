import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("Data.csv")
data=df["Avg Rating"].tolist()

fig=ff.create_distplot([data],["Avg Rating"],show_hist=False)
fig.show()