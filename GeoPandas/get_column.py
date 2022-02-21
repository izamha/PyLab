import pandas as pd

# Make dataframe
data = pd.read_csv('/home/gilfoyle/PycharmProjects/PyLab/GeoPandas/Data/nba.csv')

# Calling head() method
# Storing in new variable

data_limit = data.head()

for col in data.columns:
    print(col)

certain_col = data.loc[:, 'College']
print(certain_col)

