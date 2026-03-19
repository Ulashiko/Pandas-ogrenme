# Pandas ile Yanlış Verileri Düzeltme (Cleaning Wrong Data)

Bu klasör pandas kütüphanesi ile yanlış/mantıksız verileri tespit etme ve düzeltme yöntemlerini içerir.

## 🚀 Kullanım

```bash
python main.py
```

## 📊 Veri Seti

F1 pilotları verisi (`../f1_data.csv`) - 20 kayıt

## 📝 Kapsanan Metodlar

### 1. IQR Metodu - Outlier Tespiti

**IQR (Interquartile Range)**: Q3 - Q1

```python
Q1 = df['Puan'].quantile(0.25)     # %25'lik dilim
Q3 = df['Puan'].quantile(0.75)     # %75'lik dilim
IQR = Q3 - Q1

alt_sinir = Q1 - 1.5 * IQR
ust_sinir = Q3 + 1.5 * IQR

# Outlier'ları bul
outliers = df[(df['Puan'] < alt_sinir) | (df['Puan'] > ust_sinir)]
```

**Neden 1.5 × IQR?**
- İstatistiksel standart
- Extreme outlier için 3 × IQR kullanılır

### 2. Z-Score Metodu

```python
from scipy import stats

df['ZScore'] = stats.zscore(df['Puan'])

# |Z| > 3 ise güçlü outlier
# |Z| > 2 ise olası outlier
outliers = df[abs(df['ZScore']) > 3]
```

**Z-Score = (X - μ) / σ**
- μ: Ortalama
- σ: Standart sapma

### 3. between() - Aralık Kontrolü

```python
# 18-50 yaş aralığı
gecerli = df[df['Yas'].between(18, 50)]

# Manuel kontrol (aynı şey)
gecerli = df[(df['Yas'] >= 18) & (df['Yas'] <= 50)]
```

### 4. loc[] - Değer Düzeltme

```python
# Mantıksız yaşları NaN yap
df.loc[df['Yas'] > 100, 'Yas'] = pd.NA
df.loc[df['Yas'] < 18, 'Yas'] = pd.NA

# Negatif puanları 0 yap
df.loc[df['Puan'] < 0, 'Puan'] = 0
```

### 5. drop() - Satır Silme

```python
# Belirli satırları sil
df.drop(index=[0, 5, 10])

# Koşula göre sil
outlier_indices = df[df['Puan'] > 600].index
df.drop(outlier_indices)
```

### 6. clip() - Değer Sınırlama

```python
# 0-600 arasına sınırla
df['Puan'].clip(0, 600)

# Sadece alt sınır
df['Yas'].clip(lower=18)

# Sadece üst sınır
df['Puan'].clip(upper=500)
```

### 7. query() - SQL-benzeri Filtreleme

```python
# Tek koşul
df.query('Yas >= 18')

# Çoklu koşul
df.query('Yas >= 18 and Yas <= 50')
df.query('Puan > 100 and Takim == "Ferrari"')
```

### 8. Custom Validation

```python
def validate_row(row):
    errors = []

    if not (18 <= row['Yas'] <= 50):
        errors.append("Yaş geçersiz")

    if not (0 <= row['Puan'] <= 600):
        errors.append("Puan geçersiz")

    return ', '.join(errors) if errors else 'OK'

df['Dogrulama'] = df.apply(validate_row, axis=1)

# Hatalı satırları bul
hatalilar = df[df['Dogrulama'] != 'OK']
```

## ⚠️ Outlier (Aykırı Değer) Nedir?

**Outlier**: Diğer değerlerden önemli ölçüde farklı olan değer.

### Örnekler

| Veri | Normal Aralık | Outlier |
|------|---------------|---------|
| Yaş | 20-45 | 150 |
| Maaş | 10K-50K | 500K |
| Süre | 90-100 dak | 10 dak |

### Ne Yapmalı?

1. **İncele**: Veri hatası mı yoksa gerçek mi?
2. **Düzelt**: Veri girişi hatası ise
3. **Sil**: Analizi bozuyorsa
4. **Tut**: Gerçek ve önemli ise

## 🎯 IQR vs Z-Score

| Özellik | IQR | Z-Score |
|---------|-----|---------|
| **Robust** | ✅ Evet | ❌ Hayır |
| **Çarpık dağılım** | ✅ İyi | ❌ Kötü |
| **Normal dağılım** | ✅ İyi | ✅ İyi |
| **Kullanım** | Kolay | Orta |
| **Öneri** | **Genelde daha iyi** | Normal dağılım için |

## 💡 İpuçları

1. **IQR tercih edin**: Çoğu durumda daha güvenilir
2. **Silmeden önce düşünün**: Outlier önemli bilgi içerebilir
3. **Görselleştir**: Boxplot ile outlier'ları görün
4. **İş kuralı**: Aralıkları iş mantığına göre belirleyin
5. **Dokümante edin**: Hangi değerleri neden sild iğinizi not alın

## 🔗 İlgili Bölümler

- [(6)(1)pd-cleaning-empty-cells](../(6)(1)pd-cleaning-empty-cells) - Boş değer temizleme
- [(6)(2)pd-cleaning-wrong-format](../(6)(2)pd-cleaning-wrong-format) - Format düzeltme
- [(6)(4)pd-cleaning-duplicates](../(6)(4)pd-cleaning-duplicates) - Duplicate temizleme
- [Ana README](../README.md) - Genel bakış

## 📖 Referans

- [W3Schools - Cleaning Wrong Data](https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_data.asp)
