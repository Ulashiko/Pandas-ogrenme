import pandas as pd

print("=" * 70)
print("PANDAS ILE VERI ANALIZI (DATA ANALYZING)")
print("=" * 70)

# Veriyi oku
df = pd.read_csv('data.csv')

# 1. HEAD() - ILK SATIRLARI GOSTERIR
print("\n1. HEAD() - ILK 5 SATIRI GOSTERIR")
print("-" * 70)
print(df.head())

print("\n1.1. HEAD(10) - ILK 10 SATIRI GOSTERIR")
print("-" * 70)
print(df.head(10))

# 2. TAIL() - SON SATIRLARI GOSTERIR
print("\n2. TAIL() - SON 5 SATIRI GOSTERIR")
print("-" * 70)
print(df.tail())

print("\n2.1. TAIL(10) - SON 10 SATIRI GOSTERIR")
print("-" * 70)
print(df.tail(10))

# 3. INFO() - DATAFRAME HAKKINDA DETAYLI BILGI
print("\n3. INFO() - DATAFRAME HAKKINDA DETAYLI BILGI")
print("-" * 70)
print(df.info())

# 4. DESCRIBE() - ISTATISTIKSEL OZET
print("\n4. DESCRIBE() - SAYISAL KOLONLAR ICIN ISTATISTIKLER")
print("-" * 70)
print(df.describe())

# 5. SHAPE - SATIR VE SUTUN SAYISI
print("\n5. SHAPE - DATAFRAME'IN BOYUTLARI (SATIR, SUTUN)")
print("-" * 70)
print(f"Boyut: {df.shape}")
print(f"Toplam Satir: {df.shape[0]}")
print(f"Toplam Sutun: {df.shape[1]}")

# 6. COLUMNS - SUTUN ISIMLERI
print("\n6. COLUMNS - SUTUN ISIMLERI")
print("-" * 70)
print(df.columns)
print(f"\nSutun Listesi: {df.columns.tolist()}")

# 7. DTYPES - VERI TIPLERI
print("\n7. DTYPES - HER KOLONUN VERI TIPI")
print("-" * 70)
print(df.dtypes)

# 8. INDEX - INDEX BILGISI
print("\n8. INDEX - INDEX BILGISI")
print("-" * 70)
print(df.index)

# 9. ISNULL() - BOS DEGER KONTROLU
print("\n9. ISNULL() - BOS DEGER ANALIZI")
print("-" * 70)
print("\nHer kolondaki bos deger sayisi:")
print(df.isnull().sum())

print("\n\nBos degerlerin yuzdesi:")
print((df.isnull().sum() / len(df) * 100).round(2))

print(f"\n\nToplam bos deger: {df.isnull().sum().sum()}")

# 10. NUNIQUE() - BENZERSIZ DEGER SAYILARI
print("\n10. NUNIQUE() - HER KOLONDAKI BENZERSIZ DEGER SAYISI")
print("-" * 70)
print(df.nunique())

# 11. VALUE_COUNTS() - DEGER FREKANSLARI
print("\n11. VALUE_COUNTS() - DURATION KOLONUNUN DEGER DAGILIMI")
print("-" * 70)
print(df['Duration'].value_counts())

# 12. SAMPLE() - RASTGELE ORNEKLER
print("\n12. SAMPLE() - RASTGELE 5 SATIR")
print("-" * 70)
print(df.sample(5))

# 13. MEMORY_USAGE() - BELLEK KULLANIMI
print("\n13. MEMORY_USAGE() - BELLEK KULLANIMI")
print("-" * 70)
print(df.memory_usage(deep=True))
print(f"\nToplam Bellek: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")

# 14. CORR() - KORELASYON MATRISI
print("\n14. CORR() - KORELASYON MATRISI (SAYISAL KOLONLAR ARASI ILISKI)")
print("-" * 70)
print(df.corr())

# 15. DETAYLI VERI ANALIZI
print("\n15. DETAYLI VERI ANALIZI")
print("-" * 70)

print("\nDuration Kolonunun Analizi:")
print(f"  Ortalama: {df['Duration'].mean():.2f}")
print(f"  Medyan: {df['Duration'].median():.2f}")
print(f"  Mod: {df['Duration'].mode()[0] if not df['Duration'].mode().empty else 'N/A'}")
print(f"  Standart Sapma: {df['Duration'].std():.2f}")
print(f"  Min: {df['Duration'].min()}")
print(f"  Max: {df['Duration'].max()}")

print("\n\nCalories Kolonunun Analizi:")
print(f"  Ortalama: {df['Calories'].mean():.2f}")
print(f"  Medyan: {df['Calories'].median():.2f}")
print(f"  Dolu Deger Sayisi: {df['Calories'].count()}")
print(f"  Bos Deger Sayisi: {df['Calories'].isnull().sum()}")

# 16. QUANTILE() - YUZDELIK DILIMLER
print("\n16. QUANTILE() - YUZDELIK DILIMLER")
print("-" * 70)
print("Calories kolonunun yuzdelik dilimleri:")
print(f"  %25: {df['Calories'].quantile(0.25)}")
print(f"  %50 (Medyan): {df['Calories'].quantile(0.50)}")
print(f"  %75: {df['Calories'].quantile(0.75)}")
print(f"  %90: {df['Calories'].quantile(0.90)}")

# 17. SELECT_DTYPES() - BELIRLI TIP KOLONLARI SECME
print("\n17. SELECT_DTYPES() - SADECE SAYISAL KOLONLARI SEC")
print("-" * 70)
numeric_df = df.select_dtypes(include=['number'])
print(numeric_df.head())
print(f"\nSayisal kolonlar: {numeric_df.columns.tolist()}")

# 18. DETAYLI OZET RAPOR
print("\n18. GENEL OZET RAPOR")
print("=" * 70)
print(f"""
VERI SETI OZETI:
- Toplam Kayit: {len(df)}
- Toplam Sutun: {len(df.columns)}
- Sutunlar: {', '.join(df.columns)}
- Bos Deger: {df.isnull().sum().sum()} adet
- Bellek Kullanimi: {df.memory_usage(deep=True).sum() / 1024:.2f} KB

SAYISAL ISTATISTIKLER:
- Ortalama Egzersiz Suresi: {df['Duration'].mean():.2f} dakika
- Ortalama Nabiz: {df['Pulse'].mean():.2f} bpm
- Ortalama Max Nabiz: {df['Maxpulse'].mean():.2f} bpm
- Ortalama Kalori: {df['Calories'].mean():.2f} cal

VERI KALITESI:
- Duration - Bos: {df['Duration'].isnull().sum()} ({(df['Duration'].isnull().sum() / len(df) * 100):.1f}%)
- Pulse - Bos: {df['Pulse'].isnull().sum()} ({(df['Pulse'].isnull().sum() / len(df) * 100):.1f}%)
- Maxpulse - Bos: {df['Maxpulse'].isnull().sum()} ({(df['Maxpulse'].isnull().sum() / len(df) * 100):.1f}%)
- Calories - Bos: {df['Calories'].isnull().sum()} ({(df['Calories'].isnull().sum() / len(df) * 100):.1f}%)
""")

print("=" * 70)
print("ANALIZ TAMAMLANDI!")
print("=" * 70)
