import pandas as pd
#Pandas as data frame (Mapping a dictionary to DataFrame)
mydataset= {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
#Version control (Ex: 2.3.2)
print(pd.__version__)
