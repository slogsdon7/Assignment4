import pandas as pd
import matplotlib as mpl

df = pd.read_csv('data.csv')
df.time = pd.to_datetime(df.time)

intervals = [
    (4,4.5),
    (4.5,5),
    (5,6),
    (6,7),
    (7, df.mag.max())
]

df['magbins'] = pd.cut(df.mag, pd.IntervalIndex.from_tuples(intervals))