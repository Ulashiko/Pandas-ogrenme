import pandas as pd
#Bir liste vererek Series oluşturma, pandas varsayılan tam sayı index'i otomatik atar:
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
#Index kullanarak belirli bir değere erişme
myvar2= pd.Series(a, index = ["x","y","z"])
print(myvar2)
print(myvar2["y"])
#Adım sayısı vererek Series oluşturma
steps= {
    "day1": 10,
    "day2": 20,
    "day3": 30
}
myvar3 = pd.Series(steps)
print(myvar3)
