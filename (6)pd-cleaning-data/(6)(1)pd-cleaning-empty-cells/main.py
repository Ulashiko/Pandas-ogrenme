import pandas as pd

print("=" * 70)
print("PANDAS ILE BOS HUCRELERI TEMIZLEME (CLEANING EMPTY CELLS)")
print("=" * 70)

# Veriyi oku (bir ust klasorden)
df = pd.read_csv('../f1_data.csv')

print("\n0. ORIJINAL VERI SETI")
print("-" * 70)
print(df)

# BOS DEGERLERI KONTROL ET
print("\n1. BOS DEGER ANALIZI")
print("-" * 70)
print("\nHer kolondaki bos deger sayisi:")
print(df.isnull().sum())

print("\n\nBos degerlerin toplami:", df.isnull().sum().sum())

# 2. DROPNA() - BOS SATIRLARI SIL
print("\n2. DROPNA() - BOS SATIRI ICEREN SATIRLARI SIL")
print("-" * 70)
df_dropped = df.dropna()
print(f"Orijinal satir sayisi: {len(df)}")
print(f"Temizlenmis satir sayisi: {len(df_dropped)}")
print("\nTemizlenmis veri:")
print(df_dropped)

# 3. FILLNA() - BELIRLI BIR DEGERLE DOLDUR
print("\n3. FILLNA() - BOS DEGERLERI SABIT DEGER ILE DOLDUR")
print("-" * 70)
df_filled = df.copy()
df_filled['YarisSuresi'] = df_filled['YarisSuresi'].fillna(5400)
df_filled['Puan'] = df_filled['Puan'].fillna(0)
print("\nYarisSuresi ve Puan kolonlari dolduruldu:")
print(df_filled[['Pilot', 'YarisSuresi', 'Puan']])

# 4. MEAN() ILE DOLDUR - ORTALAMA
print("\n4. FILLNA() - ORTALAMA ILE DOLDUR")
print("-" * 70)
df_mean = df.copy()
yaris_ort = df_mean['YarisSuresi'].mean()
puan_ort = df_mean['Puan'].mean()

print(f"YarisSuresi ortalamasi: {yaris_ort:.2f}")
print(f"Puan ortalamasi: {puan_ort:.2f}")

df_mean['YarisSuresi'] = df_mean['YarisSuresi'].fillna(yaris_ort)
df_mean['Puan'] = df_mean['Puan'].fillna(puan_ort)

print("\nOrtalama ile doldurulmus veri:")
print(df_mean[['Pilot', 'YarisSuresi', 'Puan']])

# 5. MEDIAN() ILE DOLDUR - MEDYAN
print("\n5. FILLNA() - MEDYAN ILE DOLDUR")
print("-" * 70)
df_median = df.copy()
yaris_med = df_median['YarisSuresi'].median()
puan_med = df_median['Puan'].median()

print(f"YarisSuresi medyani: {yaris_med:.2f}")
print(f"Puan medyani: {puan_med:.2f}")

df_median['YarisSuresi'] = df_median['YarisSuresi'].fillna(yaris_med)
df_median['Puan'] = df_median['Puan'].fillna(puan_med)

print("\nMedyan ile doldurulmus veri:")
print(df_median[['Pilot', 'YarisSuresi', 'Puan']])

# 6. MODE() ILE DOLDUR - EN SIK DEGER
print("\n6. FILLNA() - MODE (EN SIK DEGER) ILE DOLDUR")
print("-" * 70)
df_mode = df.copy()

# Mode genelde kategorik veriler icin kullanilir
# Numerik veriler icin de kullanilebilir ama pek mantikli olmayabilir
if not df_mode['YarisSuresi'].mode().empty:
    yaris_mode = df_mode['YarisSuresi'].mode()[0]
    print(f"YarisSuresi modu: {yaris_mode}")
    df_mode['YarisSuresi'] = df_mode['YarisSuresi'].fillna(yaris_mode)

if not df_mode['Puan'].mode().empty:
    puan_mode = df_mode['Puan'].mode()[0]
    print(f"Puan modu: {puan_mode}")
    df_mode['Puan'] = df_mode['Puan'].fillna(puan_mode)

print("\nMode ile doldurulmus veri:")
print(df_mode[['Pilot', 'YarisSuresi', 'Puan']])

# 7. FORWARD FILL (FFILL) - ONCEKI DEGERLE DOLDUR
print("\n7. FFILL() - ONCEKI DEGERLE DOLDUR")
print("-" * 70)
df_ffill = df.copy()
df_ffill['Puan'] = df_ffill['Puan'].ffill()
print("\nOnce bos olan satirlari goster:")
print(df_ffill[['Pilot', 'Puan']])

# 8. BACKWARD FILL (BFILL) - SONRAKI DEGERLE DOLDUR
print("\n8. BFILL() - SONRAKI DEGERLE DOLDUR")
print("-" * 70)
df_bfill = df.copy()
df_bfill['Puan'] = df_bfill['Puan'].bfill()
print("\nSonra bos olan satirlari goster:")
print(df_bfill[['Pilot', 'Puan']])

# 9. INTERPOLATE() - INTERPOLASYON ILE DOLDUR
print("\n9. INTERPOLATE() - INTERPOLASYON ILE DOLDUR")
print("-" * 70)
df_interp = df.copy()
df_interp['YarisSuresi'] = df_interp['YarisSuresi'].interpolate()
df_interp['Puan'] = df_interp['Puan'].interpolate()
print("\nInterpolasyon ile doldurulmus:")
print(df_interp[['Pilot', 'YarisSuresi', 'Puan']])

# 10. OZEL DOLDURMA - KOLONLARA GORE FARKLI DEGERLER
print("\n10. FILLNA() - HER KOLON ICIN FARKLI DEGER")
print("-" * 70)
df_custom = df.copy()
df_custom.fillna({
    'YarisSuresi': 5400,
    'Puan': 0
}, inplace=True)
print("\nHer kolon icin ozel degerlerle doldurulmus:")
print(df_custom[['Pilot', 'YarisSuresi', 'Puan']])

# 11. DROPNA() ILE SADECE BELIRLI KOLONLARI KONTROL ET
print("\n11. DROPNA(subset=[]) - SADECE BELIRLI KOLONLARA BAK")
print("-" * 70)
df_subset = df.dropna(subset=['Puan'])
print(f"Sadece 'Puan' kolonu bos olmayan satirlar: {len(df_subset)} satir")
print(df_subset[['Pilot', 'Puan']])

# 12. KARSILASTIRMA TABLOSU
print("\n12. YONTEMLERIN KARSILASTIRILMASI")
print("=" * 70)

print(f"""
TEMIZLEME YONTEMLERI SONUCLARI:

1. ORIJINAL VERI:
   - Toplam satir: {len(df)}
   - Bos deger: {df.isnull().sum().sum()}

2. DROPNA() - SATIRLARI SIL:
   - Kalan satir: {len(df_dropped)}
   - Silinen satir: {len(df) - len(df_dropped)}

3. FILLNA(SABIT) - SABIT DEGER:
   - YarisSuresi -> 5400
   - Puan -> 0

4. FILLNA(MEAN) - ORTALAMA:
   - YarisSuresi -> {yaris_ort:.2f}
   - Puan -> {puan_ort:.2f}

5. FILLNA(MEDIAN) - MEDYAN:
   - YarisSuresi -> {yaris_med:.2f}
   - Puan -> {puan_med:.2f}

ONERILER:
- Numerik veriler icin: mean() veya median()
- Kategorik veriler icin: mode() veya sabit deger
- Zaman serisi icin: ffill(), bfill() veya interpolate()
- Cok bos deger varsa: dropna() dusunulebilir
""")

print("=" * 70)
print("TEMIZLEME ISLEMI TAMAMLANDI!")
print("=" * 70)
