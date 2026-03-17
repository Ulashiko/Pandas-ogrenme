import pandas as pd
#Creating a Series by passing a list of values, letting pandas create a default integer index:
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)