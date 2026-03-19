import pandas as pd
import json

print("=" * 70)
print("PANDAS İLE JSON OKUMA İŞLEMLERİ")
print("=" * 70)

# 1. TEMEL JSON OKUMA
print("\n1. TEMEL JSON OKUMA (pd.read_json)")
print("-" * 70)
df = pd.read_json('veriler.json')
print(df)

# 2. JSON DOSYASINI NORMALIZE EDEREK OKUMA (İÇİÇE VERİLER İÇİN)
print("\n2. JSON NORMALIZE İLE OKUMA")
print("-" * 70)
with open('veriler.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Çalışanlar verisini normalize et
df_calisanlar = pd.json_normalize(data['calisanlar'])
print(df_calisanlar)

# 3. SPESIFIK BİR JSON KEY'İNİ OKUMA
print("\n3. SPESİFİK BİR KEY'İ DATAFRAME OLARAK OKUMA")
print("-" * 70)
df_calisanlar2 = pd.DataFrame(data['calisanlar'])
print(df_calisanlar2)

# 4. JSON DOSYASINI FARKLI ORIENT İLE OKUMA
print("\n4. FARKLI ORIENT MODLARı")
print("-" * 70)
# Orient parametresi JSON'ın yapısını belirtir
# 'records': [{col1: val1, col2: val2}, {col1: val1, col2: val2}]
print("Orient: 'records' formatı zaten kullanılıyor\n")

# 5. JSON VERİSİNDEN İSTATİSTİKLER
print("\n5. VERİ İSTATİSTİKLERİ")
print("-" * 70)
print("\nTemel İstatistikler:")
print(df_calisanlar.describe())

print("\n\nVeri Tipleri:")
print(df_calisanlar.dtypes)

print("\n\nBoş Değer Kontrolü:")
print(df_calisanlar.isnull().sum())

# 6. JSON VERİSİNİ FİLTRELEME
print("\n6. VERİ FİLTRELEME ÖRNEKLERİ")
print("-" * 70)

print("\nIT Departmanındaki Çalışanlar:")
it_calisanlari = df_calisanlar[df_calisanlar['departman'] == 'IT']
print(it_calisanlari[['isim', 'maas', 'tecrube_yili']])

print("\n\nMaaşı 15000'den Fazla Olanlar:")
yuksek_maas = df_calisanlar[df_calisanlar['maas'] > 15000]
print(yuksek_maas[['isim', 'departman', 'maas']])

# 7. GRUPLAMA VE AGREGASYON
print("\n7. GRUPLAMA VE AGREGASYON")
print("-" * 70)

print("\nDepartmana Göre Ortalama Maaş:")
departman_maas = df_calisanlar.groupby('departman')['maas'].mean()
print(departman_maas)

print("\n\nDepartmana Göre Çalışan Sayısı:")
departman_sayi = df_calisanlar.groupby('departman').size()
print(departman_sayi)

print("\n\nŞehre Göre Toplam ve Ortalama Maaş:")
sehir_stats = df_calisanlar.groupby('sehir').agg({
    'maas': ['sum', 'mean', 'count'],
    'tecrube_yili': 'mean'
})
print(sehir_stats)

# 8. SIRALAMA İŞLEMLERİ
print("\n8. SIRALAMA İŞLEMLERİ")
print("-" * 70)

print("\nMaaşa Göre Sıralama (Azalan):")
maas_sirali = df_calisanlar.sort_values('maas', ascending=False)
print(maas_sirali[['isim', 'maas', 'departman']])

print("\n\nTecrübeye Göre Sıralama (Artan):")
tecrube_sirali = df_calisanlar.sort_values('tecrube_yili')
print(tecrube_sirali[['isim', 'tecrube_yili', 'departman']])

# 9. YENİ KOLONLAR EKLEME
print("\n9. YENİ KOLONLAR EKLEME VE HESAPLAMALAR")
print("-" * 70)

# Yıllık toplam maaş hesapla
df_calisanlar['yillik_maas'] = df_calisanlar['maas'] * 12

# Tecrübe seviyesi kategorisi ekle
df_calisanlar['tecrube_seviyesi'] = pd.cut(
    df_calisanlar['tecrube_yili'],
    bins=[0, 3, 5, 10],
    labels=['Junior', 'Mid', 'Senior']
)

print(df_calisanlar[['isim', 'maas', 'yillik_maas', 'tecrube_yili', 'tecrube_seviyesi']])

# 10. JSON'DAN DATAFRAME'E VE TEKRAR JSON'A
print("\n10. DATAFRAME'İ JSON'A EXPORT ETME")
print("-" * 70)

# Farklı JSON formatlarına export
df_calisanlar.to_json('calisanlar_export.json', orient='records', indent=2, force_ascii=False)
print("✓ JSON dosyası 'calisanlar_export.json' olarak kaydedildi (orient='records')")

df_calisanlar.to_json('calisanlar_table.json', orient='table', indent=2, force_ascii=False)
print("✓ JSON dosyası 'calisanlar_table.json' olarak kaydedildi (orient='table')")

# 11. İLERİ SEVİYE FİLTRELEME
print("\n11. İLERİ SEVİYE FİLTRELEME ÖRNEKLERİ")
print("-" * 70)

# Çoklu koşul ile filtreleme
print("\nİstanbul'daki IT çalışanları:")
istanbul_it = df_calisanlar[
    (df_calisanlar['sehir'] == 'İstanbul') &
    (df_calisanlar['departman'] == 'IT')
]
print(istanbul_it[['isim', 'departman', 'sehir', 'maas']])

print("\n\nMaaşı 14000-16000 arası olanlar:")
orta_maas = df_calisanlar[
    (df_calisanlar['maas'] >= 14000) &
    (df_calisanlar['maas'] <= 16000)
]
print(orta_maas[['isim', 'maas']])

# 12. ÖZETLEYİCİ BİLGİLER
print("\n12. GENEL ÖZET İSTATİSTİKLER")
print("-" * 70)

print(f"\nToplam Çalışan Sayısı: {len(df_calisanlar)}")
print(f"Ortalama Maaş: {df_calisanlar['maas'].mean():.2f} TL")
print(f"En Yüksek Maaş: {df_calisanlar['maas'].max()} TL")
print(f"En Düşük Maaş: {df_calisanlar['maas'].min()} TL")
print(f"Toplam Maaş Gideri: {df_calisanlar['maas'].sum()} TL/ay")
print(f"Ortalama Tecrübe: {df_calisanlar['tecrube_yili'].mean():.2f} yıl")

# 13. KOŞULLU SEÇİM VE İNDEXLEME
print("\n13. KOŞULLU SEÇİM VE İNDEXLEME")
print("-" * 70)

# En yüksek maaşlı çalışan
en_yuksek_maas = df_calisanlar.loc[df_calisanlar['maas'].idxmax()]
print("\nEn Yüksek Maaşlı Çalışan:")
print(f"İsim: {en_yuksek_maas['isim']}")
print(f"Maaş: {en_yuksek_maas['maas']} TL")
print(f"Departman: {en_yuksek_maas['departman']}")

# Tecrübeli çalışanlar (5 yıl üzeri)
print("\n\nTecrübeli Çalışanlar (5+ yıl):")
tecrubeliler = df_calisanlar[df_calisanlar['tecrube_yili'] >= 5]
print(tecrubeliler[['isim', 'tecrube_yili', 'departman']].to_string(index=False))

print("\n" + "=" * 70)
print("JSON OKUMA İŞLEMLERİ TAMAMLANDI!")
print("=" * 70)
