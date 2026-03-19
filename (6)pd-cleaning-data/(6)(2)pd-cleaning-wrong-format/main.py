import pandas as pd

print("=" * 70)
print("PANDAS ILE YANLIS FORMATLARI DUZELTME (CLEANING WRONG FORMAT)")
print("=" * 70)

# Veriyi oku (bir ust klasorden)
df = pd.read_csv('../f1_data.csv')

print("\n0. ORIJINAL VERI SETI")
print("-" * 70)
print(df)
print("\nVeri Tipleri:")
print(df.dtypes)

# 1. SAYISAL VERI TIPLERINI DUZELTME
print("\n1. SAYISAL VERI TIPLERINI DUZELTME")
print("-" * 70)

# YarisSuresi ve Puan float olarak okundu, ama bos degerler var
print("Orijinal tipler:")
print(f"YarisSuresi: {df['YarisSuresi'].dtype}")
print(f"Puan: {df['Puan'].dtype}")

# Bos degerleri kontrol et
print(f"\nBos degerler:")
print(f"YarisSuresi: {df['YarisSuresi'].isnull().sum()}")
print(f"Puan: {df['Puan'].isnull().sum()}")

# 2. TO_NUMERIC() ILE DUZELTME
print("\n2. TO_NUMERIC() ILE DUZELTME")
print("-" * 70)

# Herhangi bir string veri varsa numeric'e cevirir, yoksa NaN yapar
df['YarisSuresiNumeric'] = pd.to_numeric(df['YarisSuresi'], errors='coerce')
df['PuanNumeric'] = pd.to_numeric(df['Puan'], errors='coerce')

print("\nDuzeltilmis veri tipleri:")
print(f"YarisSuresiNumeric: {df['YarisSuresiNumeric'].dtype}")
print(f"PuanNumeric: {df['PuanNumeric'].dtype}")

# 3. ASTYPE() ILE TIP DONUSUMU
print("\n3. ASTYPE() ILE TIP DONUSUMU")
print("-" * 70)

# Yas zaten tam sayi ama float'a cevirelim
df['YasFloat'] = df['Yas'].astype(float)

print("Yas kolonu donusturuldu:")
print(df[['Pilot', 'Yas', 'YasFloat']].head())

# 4. STRING FORMATLARI DUZELTME
print("\n4. STRING FORMATLARI DUZELTME")
print("-" * 70)

# Pilot isimlerini temizle
df['PilotTemiz'] = df['Pilot'].str.strip()  # Bosluk temizle
df['PilotUpper'] = df['Pilot'].str.upper()  # Buyuk harf
df['PilotLower'] = df['Pilot'].str.lower()  # Kucuk harf
df['PilotTitle'] = df['Pilot'].str.title()  # Her Kelimenin Ilk Harfi Buyuk

print(df[['Pilot', 'PilotUpper', 'PilotLower']].head())

# 5. REPLACE() ILE DEGER DEGISTIRME
print("\n5. REPLACE() ILE FORMAT DUZELTME")
print("-" * 70)

# Ulke isimlerindeki olasi yazim hatalarini duzeltelim
df_replace = df.copy()

ulke_map = {
    'Ingiltere': 'İngiltere',
    'Ispanya': 'İspanya',
    'Cin': 'Çin'
}

df_replace['UlkeDuzeltilmis'] = df_replace['Ulke'].replace(ulke_map)

print(df_replace[['Pilot', 'Ulke', 'UlkeDuzeltilmis']].head(10))

# 6. STRIP() VE WHITESPACE TEMIZLEME
print("\n6. WHITESPACE TEMIZLEME")
print("-" * 70)

# Tum string kolonlari temizle
string_cols = df.select_dtypes(include=['object']).columns

df_clean = df.copy()
for col in string_cols:
    df_clean[col] = df_clean[col].str.strip() if df_clean[col].dtype == 'object' else df_clean[col]

print("String kolonlar temizlendi:")
print(df_clean[['Pilot', 'Takim', 'Ulke']].head())

# 7. KATEGORIK VERILERI STANDARTLASTIRMA
print("\n7. KATEGORIK VERILERI STANDARTLASTIRMA")
print("-" * 70)

# Takim isimlerini standart hale getir
print("Benzersiz takimlar:")
print(df['Takim'].unique())

# 8. FLOAT'I INTEGER'A CEVIRME (BOS DEGERLER VARSA)
print("\n8. FLOAT'I INTEGER'A CEVIRME")
print("-" * 70)

# YarisSuresi'nde bos olmayan degerleri integer'a cevir
df_int = df.dropna(subset=['YarisSuresi'])
df_int['YarisSuresiInt'] = df_int['YarisSuresi'].astype(int)

print("Float'tan Integer'a donusum:")
print(df_int[['Pilot', 'YarisSuresi', 'YarisSuresiInt']].head())

# 9. ROUND() ILE YUVARLAMA
print("\n9. SAYILARI YUVARLAMA")
print("-" * 70)

# Puan degerlerini yuvarla (eger ondalikli olsaydi)
df['PuanYuvarlanmis'] = df['Puan'].round(0)

print(df[['Pilot', 'Puan', 'PuanYuvarlanmis']].head(10))

# 10. APPLY() ILE OZEL DONUSUM
print("\n10. APPLY() ILE OZEL DONUSUM FONKSIYONU")
print("-" * 70)

def takim_kisalt(takim):
    """Takim isimlerini kisaltir"""
    kisaltmalar = {
        'Red Bull': 'RB',
        'Mercedes': 'MB',
        'Ferrari': 'FR',
        'McLaren': 'MC',
        'Aston Martin': 'AM',
        'Alpine': 'AL',
        'Alfa Romeo': 'AR',
        'AlphaTauri': 'AT',
        'Haas': 'HA',
        'Williams': 'WL'
    }
    return kisaltmalar.get(takim, takim)

df['TakimKisa'] = df['Takim'].apply(takim_kisalt)

print(df[['Pilot', 'Takim', 'TakimKisa']].head(10))

# 11. TAMAMLANMIS TEMIZ VERI
print("\n11. TAMAMLANMIS TEMIZ VERI SETI")
print("-" * 70)

df_final = pd.DataFrame({
    'Pilot': df['Pilot'].str.strip(),
    'Takim': df['Takim'].str.strip(),
    'TakimKisa': df['TakimKisa'],
    'YarisSuresi': pd.to_numeric(df['YarisSuresi'], errors='coerce'),
    'Puan': pd.to_numeric(df['Puan'], errors='coerce'),
    'Yas': df['Yas'].astype(int),
    'Ulke': df['Ulke'].str.strip()
})

print(df_final)

# 12. OZET RAPOR
print("\n12. FORMAT DUZELTME OZETI")
print("=" * 70)

print(f"""
UYGULANAN FORMAT DUZELTMELERI:

1. SAYISAL DONUSUMLER:
   - pd.to_numeric() ile guvenli numeric donusum
   - .astype(int/float) ile tip donusumu
   - .round() ile yuvarlama

2. STRING TEMIZLEME:
   - .str.strip() ile bosluk temizleme
   - .str.upper/lower/title() ile buyukluk donusumu
   - .replace() ile deger degistirme

3. KATEGORIK STANDARTLASTIRMA:
   - Takim isimlerini kisaltma
   - Ulke isimlerini duzeltme

4. OZEL DONUSUMLER:
   - .apply() ile custom fonksiyon
   - Lambda fonksiyonlari

SONUC:
- Tum sayisal kolonlar dogru tipte
- String kolonlar temizlendi
- Kategorik veriler standartlastirildi
- {df_final.shape[0]} satir, {df_final.shape[1]} kolon
""")

print("=" * 70)
print("FORMAT DUZELTME TAMAMLANDI!")
print("=" * 70)
