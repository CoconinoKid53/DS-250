#%%
import pandas as pd



#%% df = pd.read_csv('mpg.csv')
# df.shape returns tupple
# row = df.sjape[0]
# cols = df.shape [1]
# df['year']
# df['class']
# new_df = df [['year', 'class']] //how to put two things together

#%% new_df
# (df['cty].mean())
# (df'[disp]'.mean())
# mean min and max only works on numbers meaning ints and floats
# m = df[c='cty]
# print(df[['cty', 'hwy']].sum())
# print(df[['cty', hwy]]())
# print(f'The mean for CTY is {m}')



# df['class'].unique()

# df ['class'].value_counts()
# df.describe()
# fig.show()
# df2 = df[['iso_code','data',''total_cause', 'new_cases']]
# d2.info()
usa = d2.query('iso_code == "USA"')
usa
#%%
fig = px.line(
    usa2,
    x = 'date',
    y = 'new_cases'
)
fig.show()

#%%
can = df2.query('ido_code == "CAN" ')
fig = px,line(
    both,
    x = 'date',
    y = 'new cases',
    
)
