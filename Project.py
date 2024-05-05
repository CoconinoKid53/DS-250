#%%
import pandas as pd


#%%
df = pd.read_csv('name_year.csv')
#%%
john = df.query('name == John # has to be one whole string')

#%%
john
# %%
fig = px.line(
    john,
    x = 'year',
    y = 'Total'
)
fig.show()

# %%
