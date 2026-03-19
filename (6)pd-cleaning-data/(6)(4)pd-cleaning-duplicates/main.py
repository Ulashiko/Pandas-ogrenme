import pandas as pd

print("=" * 70)
print("PANDAS ILE TEKRAR EDEN VERILERI TEMIZLEME (CLEANING DUPLICATES)")
print("=" * 70)

# Veriyi oku
df = pd.read_csv('../f1_data.csv')

# Test icin duplicate satirlar ekle
print("\n0. TEST ICIN DUPLICATE SATIRLAR EKLENIYOR")
print("-" * 70)

# Ilk 3 satiri kopyalayip ekle (duplicate oluştur)
df_duplicate = pd.concat([df, df.head(3)], ignore_index=True)

print(f"Orijinal satir sayisi: {len(df)}")
print(f"Duplicate eklenmiş satir sayisi: {len(df_duplicate)}")

print("\nGuncel veri (son 5 satir):")
print(df_duplicate.tail())

# 1. DUPLICATED() ILE TEKRARLARI TESPIT ETME
print("\n1. DUPLICATED() ILE TEKRARLARI TESPIT ET")
print("-" * 70)

# Tum kolonlara gore duplicate kontrol
duplicates = df_duplicate.duplicated()
print(f"Duplicate satir sayisi: {duplicates.sum()}")

# Duplicate olan satirlari goster
dup_rows = df_duplicate[duplicates]
if not dup_rows.empty:
    print("\nDuplicate satirlar:")
    print(dup_rows[['Pilot', 'Takim', 'Puan']])

# 2. DUPLICATED(keep) PARAMETRESI
print("\n2. DUPLICATED() keep PARAMETRESI")
print("-" * 70)

# keep='first' - Ilk gorunumu tut, digerleri duplicate
first_dup = df_duplicate.duplicated(keep='first')
print(f"keep='first': {first_dup.sum()} duplicate")

# keep='last' - Son gorunumu tut, digerleri duplicate
last_dup = df_duplicate.duplicated(keep='last')
print(f"keep='last': {last_dup.sum()} duplicate")

# keep=False - Tum duplicateleri isaretler
all_dup = df_duplicate.duplicated(keep=False)
print(f"keep=False: {all_dup.sum()} duplicate (tum tekrarlar)")

# keep=False ile tum duplicate satirlari goster
print("\nTum duplicate satirlar (hem orijinal hem kopyalar):")
print(df_duplicate[all_dup][['Pilot', 'Takim', 'Puan']])

# 3. SUBSET PARAMETRESI - BELIRLI KOLONLARA GORE
print("\n3. SUBSET - BELIRLI KOLONLARA GORE DUPLICATE KONTROLU")
print("-" * 70)

# Sadece Pilot kolonuna gore duplicate kontrol
pilot_dup = df_duplicate.duplicated(subset=['Pilot'])
print(f"Pilot kolonuna gore duplicate: {pilot_dup.sum()}")

if pilot_dup.sum() > 0:
    print("\nAyni isimli pilotlar:")
    print(df_duplicate[pilot_dup][['Pilot', 'Takim', 'Puan']])

# Pilot ve Takim kombinasyonuna gore
pilot_takim_dup = df_duplicate.duplicated(subset=['Pilot', 'Takim'])
print(f"\nPilot + Takim kombinasyonuna gore: {pilot_takim_dup.sum()}")

# 4. DROP_DUPLICATES() - TEKRARLARI KALDIR
print("\n4. DROP_DUPLICATES() - TEKRARLARI SIL")
print("-" * 70)

df_clean = df_duplicate.drop_duplicates()

print(f"Onceki satir sayisi: {len(df_duplicate)}")
print(f"Temizlenmis satir sayisi: {len(df_clean)}")
print(f"Silinen duplicate: {len(df_duplicate) - len(df_clean)}")

# 5. DROP_DUPLICATES(keep) PARAMETRESI
print("\n5. DROP_DUPLICATES() keep PARAMETRESI")
print("-" * 70)

# keep='first' - Ilk gorunum kalir
df_first = df_duplicate.drop_duplicates(keep='first')
print(f"keep='first': {len(df_first)} satir kaldi")

# keep='last' - Son gorunum kalir
df_last = df_duplicate.drop_duplicates(keep='last')
print(f"keep='last': {len(df_last)} satir kaldi")

# keep=False - Hic bir duplicate kalmasın (tum tekrarlari sil)
df_none = df_duplicate.drop_duplicates(keep=False)
print(f"keep=False: {len(df_none)} satir kaldi (tekrarlar silindi)")

# 6. SUBSET ILE BELIRLI KOLONLARA GORE SILME
print("\n6. SUBSET - BELIRLI KOLONLARA GORE DUPLICATE SIL")
print("-" * 70)

# Sadece Pilot ismine gore unique tut
df_unique_pilot = df_duplicate.drop_duplicates(subset=['Pilot'], keep='first')
print(f"Unique pilot sayisi: {len(df_unique_pilot)}")

print("\nUnique pilotlar:")
print(df_unique_pilot[['Pilot', 'Takim', 'Puan']].head(10))

# 7. INPLACE PARAMETRESI
print("\n7. INPLACE PARAMETRESI")
print("-" * 70)

df_inplace = df_duplicate.copy()
print(f"Oncesi: {len(df_inplace)} satir")

# inplace=True ile dogrudan degistir
df_inplace.drop_duplicates(inplace=True)
print(f"Sonrasi: {len(df_inplace)} satir")

# 8. VALUE_COUNTS() ILE DUPLICATE ANALIZI
print("\n8. VALUE_COUNTS() ILE TEKRAR SAYILARI")
print("-" * 70)

# Her pilotan kac tane var?
pilot_counts = df_duplicate['Pilot'].value_counts()
print("\nHer pilotan kac satir var:")
print(pilot_counts.head(10))

# Birden fazla olan pilotlar
coklu = pilot_counts[pilot_counts > 1]
if not coklu.empty:
    print(f"\n\nBirden fazla satiri olan pilotlar: {len(coklu)}")
    print(coklu)

# 9. GROUPBY ILE DUPLICATE TESPITI
print("\n9. GROUPBY ILE DUPLICATE ANALIZI")
print("-" * 70)

# Pilot bazinda gruplama
grouped = df_duplicate.groupby('Pilot').size()
duplicated_pilots = grouped[grouped > 1]

if not duplicated_pilots.empty:
    print("Duplicate pilotlar ve sayilari:")
    print(duplicated_pilots)

# 10. CONDITIONAL DUPLICATE REMOVAL
print("\n10. KOSULLU DUPLICATE TEMIZLEME")
print("-" * 70)

# Ayni Pilot ama farkli Puan varsa, en yuksek puani tut
df_conditional = df_duplicate.sort_values('Puan', ascending=False)
df_conditional = df_conditional.drop_duplicates(subset=['Pilot'], keep='first')

print("Ayni pilot varsa en yuksek puanli olanı tutuldu:")
print(df_conditional[['Pilot', 'Takim', 'Puan']].head(10))

# 11. NUNIQUE() ILE UNIQUE DEGER SAYISI
print("\n11. NUNIQUE() - UNIQUE DEGER SAYILARI")
print("-" * 70)

print("Her kolondaki unique deger sayisi:")
print(df_duplicate.nunique())

unique_pilots = df_duplicate['Pilot'].nunique()
total_pilots = len(df_duplicate)
print(f"\n\nUnique pilot sayisi: {unique_pilots}")
print(f"Toplam satir: {total_pilots}")
print(f"Duplicate pilot: {total_pilots - unique_pilots}")

# 12. TAMAMLANMIS TEMIZ VERI
print("\n12. TAMAMLANMIS TEMIZ VERI SETI")
print("-" * 70)

df_final = df_duplicate.copy()

# Tum kolonlara gore duplicate sil
df_final = df_final.drop_duplicates()

# Sonucu goster
print(f"Temiz veri: {len(df_final)} satir")
print(df_final[['Pilot', 'Takim', 'YarisSuresi', 'Puan']])

# 13. OZET RAPOR
print("\n13. DUPLICATE TEMIZLEME OZETI")
print("=" * 70)

print(f"""
ORIJINAL VERI:
- F1 pilotlari: {len(df)} satir
- Test icin duplicate eklendi: +3 satir
- Toplam: {len(df_duplicate)} satir

DUPLICATE TESPITI:
- .duplicated() ile tespit
- .value_counts() ile analiz
- .groupby() ile gruplama

TEMIZLEME YONTEMLERI:
- .drop_duplicates() ile silme
- keep='first' - ilk gorunum kalir
- keep='last' - son gorunum kalir
- keep=False - hic bir duplicate kalmasın
- subset=[col] - belirli kolonlara gore

SONUC:
- Orijinal (duplicate'li): {len(df_duplicate)} satir
- Temizlenmis: {len(df_final)} satir
- Cikarilan duplicate: {len(df_duplicate) - len(df_final)} satir
- Unique pilot: {df_final['Pilot'].nunique()}
""")

print("=" * 70)
print("DUPLICATE TEMIZLEME TAMAMLANDI!")
print("=" * 70)
