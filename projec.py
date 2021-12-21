import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()

b = ff.create_distplot([data],["Weight curve"],show_hist=False)
b.show()
