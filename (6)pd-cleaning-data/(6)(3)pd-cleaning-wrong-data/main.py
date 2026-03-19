import pandas as pd

print("=" * 70)
print("PANDAS ILE YANLIS VERILERI DUZELTME (CLEANING WRONG DATA)")
print("=" * 70)

# Veriyi oku
df = pd.read_csv('../f1_data.csv')

print("\n0. ORIJINAL VERI SETI")
print("-" * 70)
print(df)

# 1. MANTIKLI OLMAYAN DEGERLERI TESPIT ETME
print("\n1. MANTIKLI OLMAYAN DEGERLERI TESPIT ET")
print("-" * 70)

print("Temel istatistikler:")
print(df.describe())

# YarisSuresi icin min/max kontrol
print(f"\nYarisSuresi araligi: {df['YarisSuresi'].min()} - {df['YarisSuresi'].max()}")
print(f"Puan araligi: {df['Puan'].min()} - {df['Puan'].max()}")
print(f"Yas araligi: {df['Yas'].min()} - {df['Yas'].max()}")

# 2. OUTLIER (AYKIRI DEGER) TESPITI - IQR YONTEMI
print("\n2. OUTLIER TESPITI (IQR YONTEMI)")
print("-" * 70)

def outlier_tespit(df, kolon):
    """IQR yontemi ile outlier tespit eder"""
    Q1 = df[kolon].quantile(0.25)
    Q3 = df[kolon].quantile(0.75)
    IQR = Q3 - Q1

    alt_sinir = Q1 - 1.5 * IQR
    ust_sinir = Q3 + 1.5 * IQR

    outliers = df[(df[kolon] < alt_sinir) | (df[kolon] > ust_sinir)]

    print(f"\n{kolon} icin:")
    print(f"  Q1 (25%): {Q1}")
    print(f"  Q3 (75%): {Q3}")
    print(f"  IQR: {IQR}")
    print(f"  Alt Sinir: {alt_sinir}")
    print(f"  Ust Sinir: {ust_sinir}")
    print(f"  Outlier sayisi: {len(outliers)}")

    return outliers

# Puan kolonunda outlier var mi?
puan_outliers = outlier_tespit(df.dropna(subset=['Puan']), 'Puan')
if not puan_outliers.empty:
    print("\nOutlier satirlar:")
    print(puan_outliers[['Pilot', 'Puan', 'Takim']])

# 3. BELIRLI BIR ARALIK DISI DEGERLERI TEMIZLEME
print("\n3. ARALIK KONTROLU VE DUZELTME")
print("-" * 70)

# Yas icin mantikli aralik: 18-50
print("Yanlis yas degerleri (18-50 arasi olmayan):")
yanlis_yas = df[(df['Yas'] < 18) | (df['Yas'] > 50)]
if not yanlis_yas.empty:
    print(yanlis_yas[['Pilot', 'Yas']])
else:
    print("Tum yaslar 18-50 araliginda - OK!")

# YarisSuresi icin mantikli aralik: 5300-5500 saniye
print("\n\nYanlis YarisSuresi degerleri (5300-5500 arasi olmayan):")
yanlis_sure = df[(df['YarisSuresi'] < 5300) | (df['YarisSuresi'] > 5500)]
yanlis_sure = yanlis_sure.dropna(subset=['YarisSuresi'])
if not yanlis_sure.empty:
    print(yanlis_sure[['Pilot', 'YarisSuresi']])
else:
    print("Tum sureler normal aralikta!")

# 4. LOC ILE BELIRLI DEGERLERI DUZELTME
print("\n4. LOC ILE YANLIS DEGERLERI DUZELT")
print("-" * 70)

df_corrected = df.copy()

# Mantik disi degerleri NaN yap
df_corrected.loc[df_corrected['Yas'] > 50, 'Yas'] = pd.NA
df_corrected.loc[df_corrected['Yas'] < 18, 'Yas'] = pd.NA

df_corrected.loc[(df_corrected['YarisSuresi'] < 5300) | (df_corrected['YarisSuresi'] > 5500), 'YarisSuresi'] = pd.NA

print("Aralik disi degerler NaN'a cevrildi:")
print(df_corrected[['Pilot', 'YarisSuresi', 'Yas']].head(10))

# 5. DROP() ILE YANLIS SATIRLARI KALDIRMA
print("\n5. DROP() ILE BELIRLI SATIRLARI SIL")
print("-" * 70)

df_drop = df.copy()

# Puan 575'ten buyuk satirlari sil (mantikli sinir)
outlier_indices = df_drop[df_drop['Puan'] > 600].index
if not outlier_indices.empty:
    df_drop = df_drop.drop(outlier_indices)
    print(f"{len(outlier_indices)} satir silindi (Puan > 600)")
else:
    print("Silinecek outlier yok")

print(f"Kalan satir sayisi: {len(df_drop)}")

# 6. Z-SCORE ILE AYKIRI DEGER TESPITI
print("\n6. Z-SCORE ILE AYKIRI DEGER TESPITI")
print("-" * 70)

from scipy import stats

# Puan icin Z-score hesapla (bos olmayan degerler icin)
df_zscore = df.dropna(subset=['Puan']).copy()
df_zscore['PuanZScore'] = stats.zscore(df_zscore['Puan'])

# Z-score > 3 veya < -3 ise aykiri kabul edilir
aykiriler = df_zscore[abs(df_zscore['PuanZScore']) > 2]

print("Z-Score degerleri:")
print(df_zscore[['Pilot', 'Puan', 'PuanZScore']].head(10))

if not aykiriler.empty:
    print(f"\n\nZ-Score > 2 olan satirlar (aykiri): {len(aykiriler)}")
    print(aykiriler[['Pilot', 'Puan', 'PuanZScore']])

# 7. VERI DOGRULAMA - CUSTOM KURALLAR
print("\n7. CUSTOM VERI DOGRULAMA KURALLARI")
print("-" * 70)

def veri_dogrula(row):
    """Her satir icin dogrulama kurallari"""
    hatalar = []

    # Kural 1: YarisSuresi 5000-6000 arasi olmali
    if pd.notna(row['YarisSuresi']) and not (5000 <= row['YarisSuresi'] <= 6000):
        hatalar.append("YarisSuresi aralik disi")

    # Kural 2: Puan 0-600 arasi olmali
    if pd.notna(row['Puan']) and not (0 <= row['Puan'] <= 600):
        hatalar.append("Puan aralik disi")

    # Kural 3: Yas 18-50 arasi olmali
    if not (18 <= row['Yas'] <= 50):
        hatalar.append("Yas aralik disi")

    return ', '.join(hatalar) if hatalar else 'OK'

df['DogrulamaHata'] = df.apply(veri_dogrula, axis=1)

print("\nDogrulama sonuclari:")
hatali = df[df['DogrulamaHata'] != 'OK']
if not hatali.empty:
    print(f"Hatali satir: {len(hatali)}")
    print(hatali[['Pilot', 'DogrulamaHata']])
else:
    print("Tum satirlar dogrulama kurallarini gecti!")

# 8. QUERY() ILE MANTIKLI VERILERI SECME
print("\n8. QUERY() ILE FILTRE")
print("-" * 70)

# Mantikli deger araligindaki satirlari sec
mantikli = df.query('Yas >= 20 and Yas <= 45')
print(f"\n20-45 yas araligindaki pilotlar: {len(mantikli)}")
print(mantikli[['Pilot', 'Yas', 'Puan']].head(10))

# 9. TEMIZ VERI SETI OLUSTURMA
print("\n9. TAMAMLANMIS TEMIZ VERI SETI")
print("-" * 70)

df_final = df.copy()

# Mantikli aralik disini NaN yap
df_final.loc[(df_final['YarisSuresi'] < 5000) | (df_final['YarisSuresi'] > 6000), 'YarisSuresi'] = pd.NA
df_final.loc[(df_final['Puan'] < 0) | (df_final['Puan'] > 600), 'Puan'] = pd.NA
df_final.loc[(df_final['Yas'] < 18) | (df_final['Yas'] > 50), 'Yas'] = pd.NA

# NaN'lari doldur veya sil
df_final = df_final.dropna()

print(f"Temiz veri: {len(df_final)} satir")
print(df_final[['Pilot', 'Takim', 'YarisSuresi', 'Puan', 'Yas']])

# 10. OZET RAPOR
print("\n10. YANLIS VERI TEMIZLEME OZETI")
print("=" * 70)

print(f"""
TESPIT EDILEN PROBLEMLER:
- Aykiri degerler (outliers)
- Mantikli aralik disi degerler
- Olasi veri giris hatalari

KULLANILAN YONTEMLER:
1. IQR metodu ile outlier tespiti
2. Z-Score ile aykiri deger analizi
3. .between() ile aralik kontrolu
4. .loc[] ile deger duzeltme
5. .drop() ile satir silme
6. Custom dogrulama fonksiyonlari
7. .query() ile filtreleme

SONUC:
- Orijinal: {len(df)} satir
- Temiz veri: {len(df_final)} satir
- Cikarilan: {len(df) - len(df_final)} satir
""")

print("=" * 70)
print("YANLIS VERI TEMIZLEME TAMAMLANDI!")
print("=" * 70)
