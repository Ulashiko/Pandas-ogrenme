import pandas as pd
#Bir liste vererek Series oluşturma, pandas varsayılan tam sayı index'i otomatik atar:
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)