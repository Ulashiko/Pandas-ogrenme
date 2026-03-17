import pandas as pd
#Pandas DataFrame (Bir sözlüğü DataFrame'e dönüştürme)
mydataset= {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
#Versiyon kontrolü (Örn: 2.3.2)
print(pd.__version__)
