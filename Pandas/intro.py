import pandas as pd
import numpy as np


# Creating empty series
ser = pd.Series()

print(ser)

# Simple array
data = np.array(['a', 'b', 'd', 'f'])

ser = pd.Series(data)
print(ser)

# Creating a DataFrame

df = pd.DataFrame()
print(df)

# list of strings
lst = ['Financial', 'Freedom', 'is',
       'my', 'only', 'hope']

# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)
