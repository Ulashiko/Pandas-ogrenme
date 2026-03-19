import pandas as pd

# Örnek veri içeren sözlük
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# Veriyi DataFrame objesine dönüştürmek için yüklüyorum
df = pd.DataFrame(data)

# Tüm DataFrame'i göster
print(df)

# loc kullanarak tek bir satıra (index 0) erişim
print(df.loc[0])

# loc kullanarak birden fazla satıra (index 0 ve 1) erişim
print(df.loc[[0, 1]])

# CSV dosyasından veri okuma
df = pd.read_csv('./(2)pd-dataframe/data.csv')

# CSV'den yüklenen DataFrame'i göster
print(df) 