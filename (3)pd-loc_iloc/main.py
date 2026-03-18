import pandas as pd

# Örnek veri seti oluşturma
data = {
    'Name': ['Ali', 'Ayşe', 'Mehmet', 'Fatma', 'Ahmet'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya'],
    'Salary': [5000, 6000, 7000, 5500, 6500]
}

df = pd.DataFrame(data)
print("Orijinal DataFrame:")
print(df)
print("\n" + "="*50 + "\n")

# ========== LOC ÖRNEKLERI (Label-based) ==========
print("LOC ÖRNEKLERI (Etiket/İsim Tabanlı):")
print("-" * 50)

# Tek bir satıra erişim (index etiketine göre)
print("\n1. df.loc[0] - Index etiketi 0 olan satır:")
print(df.loc[0])

# Birden fazla satıra erişim
print("\n2. df.loc[[0, 2, 4]] - Index 0, 2, 4 olan satırlar:")
print(df.loc[[0, 2, 4]])

# Satır aralığı (BİTİŞ DAHİL!)
print("\n3. df.loc[1:3] - Index 1'den 3'e kadar (3 DAHİL):")
print(df.loc[1:3])

# Belirli bir sütuna erişim
print("\n4. df.loc[:, 'Name'] - Tüm satırlar, sadece 'Name' sütunu:")
print(df.loc[:, 'Name'])

# Belirli satır ve sütun
print("\n5. df.loc[2, 'City'] - 2. index, 'City' sütunu:")
print(df.loc[2, 'City'])

# Birden fazla sütun
print("\n6. df.loc[:, ['Name', 'Salary']] - Name ve Salary sütunları:")
print(df.loc[:, ['Name', 'Salary']])

# Satır ve sütun birlikte
print("\n7. df.loc[0:2, ['Name', 'Age']] - İlk 3 satır, Name ve Age:")
print(df.loc[0:2, ['Name', 'Age']])

print("\n" + "="*50 + "\n")

# ========== ILOC ÖRNEKLERI (Position-based) ==========
print("ILOC ÖRNEKLERI (Pozisyon/Sıra Tabanlı):")
print("-" * 50)

# Tek bir satıra erişim (pozisyona göre)
print("\n1. df.iloc[0] - İlk satır (pozisyon 0):")
print(df.iloc[0])

# Birden fazla satıra erişim
print("\n2. df.iloc[[0, 2, 4]] - 1., 3. ve 5. satırlar:")
print(df.iloc[[0, 2, 4]])

# Satır aralığı (BİTİŞ HARİÇ!)
print("\n3. df.iloc[1:4] - Pozisyon 1'den 4'e kadar (4 HARİÇ):")
print(df.iloc[1:4])

# Belirli bir sütuna erişim (pozisyonla)
print("\n4. df.iloc[:, 0] - Tüm satırlar, ilk sütun:")
print(df.iloc[:, 0])

# Belirli satır ve sütun pozisyonu
print("\n5. df.iloc[2, 2] - 3. satır, 3. sütun:")
print(df.iloc[2, 2])

# Birden fazla sütun (pozisyonla)
print("\n6. df.iloc[:, [0, 3]] - İlk ve dördüncü sütunlar:")
print(df.iloc[:, [0, 3]])

# Satır ve sütun pozisyonu birlikte
print("\n7. df.iloc[0:3, 0:2] - İlk 3 satır, ilk 2 sütun:")
print(df.iloc[0:3, 0:2])

# Negatif indexleme (sondan saymak)
print("\n8. df.iloc[-1] - Son satır:")
print(df.iloc[-1])

print("\n9. df.iloc[:, -1] - Tüm satırlar, son sütun:")
print(df.iloc[:, -1])

print("\n" + "="*50 + "\n")

# ========== FARK ÖRNEĞİ ==========
print("ÖNEMLİ FARK ÖRNEĞİ:")
print("-" * 50)

# Özel index'li DataFrame oluştur
df2 = pd.DataFrame(data, index=[10, 20, 30, 40, 50])
print("\nÖzel Index'li DataFrame:")
print(df2)

print("\ndf2.loc[10] - Index etiketi 10 olan satır:")
print(df2.loc[10])

print("\ndf2.iloc[10] - HATA! Çünkü sadece 5 satır var (0-4):")
try:
    print(df2.iloc[10])
except IndexError as e:
    print(f"IndexError: {e}")

print("\ndf2.iloc[1] - 2. sıradaki satır (index etiketi 20):")
print(df2.iloc[1])

print("\ndf2.loc[20] - Index etiketi 20 olan satır:")
print(df2.loc[20])
