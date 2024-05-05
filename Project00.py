#%%
import pandas as pd
import plotly.express as px

#%%
df = pd.read_csv('mpg.csv')
#%%
df['year']
df['class']
df['manufacturer']
df['cyl']
df['trans']

(df['cty'].mean())
(df['displ'].mean())
m = df['cty'].mean()
print(df[['cty', 'hwy']].sum())
print(df[['cty', 'hwy']])
print(f'The mean for CTY is {m}')
print('Model: Ranger')
print('year: 1999')
print('manufacturer:Ford')
print('trans: auto')
print('cty: San Diego')
print('Hwy: I - 10')
px.scatter(df,x = 'displ', y = 'hwy')
# %%
