# Pandas ile Boş Hücreleri Temizleme (Cleaning Empty Cells)

Bu klasör pandas kütüphanesi ile boş/eksik değerleri (null, NaN) temizleme yöntemlerini içerir.

## 🚀 Kullanım

```bash
python main.py
```

## 📊 Veri Seti

F1 pilotları verisi (`../f1_data.csv`) - 20 kayıt, 9 boş değer

## 📝 Kapsanan Metodlar

### 1. isnull() - Boş Değer Tespit

```python
df.isnull()                # Her hücre için True/False
df.isnull().sum()          # Her kolondaki boş sayısı
df.isnull().sum().sum()    # Toplam boş sayısı
```

### 2. dropna() - Boş Satırları Sil

```python
df.dropna()                      # Herhangi bir boş değer içeren satırı sil
df.dropna(subset=['Puan'])       # Sadece Puan boş olanları sil
df.dropna(thresh=3)              # En az 3 dolu değer olmalı
```

### 3. fillna() - Sabit Değer ile Doldur

```python
df['Puan'].fillna(0)                           # 0 ile doldur
df.fillna({'YarisSuresi': 5400, 'Puan': 0})   # Her kolon için farklı
```

### 4. mean() - Ortalama ile Doldur

```python
ortalama = df['Puan'].mean()
df['Puan'] = df['Puan'].fillna(ortalama)
```

### 5. median() - Medyan ile Doldur

```python
medyan = df['Puan'].median()
df['Puan'] = df['Puan'].fillna(medyan)
```

**Medyan genelde ortalamadan daha güvenlidir** (outlier'lardan etkilenmez)

### 6. mode() - En Sık Değer ile Doldur

```python
mod = df['Takim'].mode()[0]
df['Takim'] = df['Takim'].fillna(mod)
```

Kategorik veriler için idealdir.

### 7. ffill() - Önceki Değerle Doldur

```python
df['Puan'] = df['Puan'].ffill()
```

Zaman serisi verileri için kullanışlıdır.

### 8. bfill() - Sonraki Değerle Doldur

```python
df['Puan'] = df['Puan'].bfill()
```

### 9. interpolate() - İnterpolasyon

```python
df['YarisSuresi'] = df['YarisSuresi'].interpolate()
```

Sayısal değerler arasında doğrusal interpolasyon yapar.

## 🎯 Hangi Yöntemi Kullanmalı?

| Durum | Önerilen Metod | Neden |
|-------|----------------|-------|
| Sayısal veri | `median()` | Outlier'lardan etkilenmez |
| Kategorik veri | `mode()` | En sık görülen değer |
| Zaman serisi | `ffill()` / `interpolate()` | Trend korunur |
| Varsayılan değer var | `fillna(sabit)` | İş kuralı |
| Çok az boş değer | `dropna()` | Veri kaybı az |

## 💡 İpuçları

1. **median() > mean()**: Çoğu durumda medyan daha güvenlidir
2. **Önce analiz**: Boş değerlerin nedenini araştırın
3. **Veri kaybı**: dropna() kullanmadan önce iki kez düşünün
4. **Kategorik**: mode() veya en mantıklı sabit değeri kullanın

## 📈 Örnek Sonuçlar

Script çalıştırıldığında 9 boş değer için tüm yöntemlerin sonuçlarını karşılaştırabilirsiniz:

- **dropna()**: 20 → 11 satır (9 satır kaybı)
- **fillna(0)**: Tüm boş değerler 0 oldu
- **mean()**: YarisSuresi=5409.29, Puan=150.53
- **median()**: YarisSuresi=5409.00, Puan=62.00
- **ffill()**: Önceki değerlerle dolduruldu

## 🔗 İlgili Bölümler

- [(6)(2)pd-cleaning-wrong-format](../(6)(2)pd-cleaning-wrong-format) - Format düzeltme
- [(6)(3)pd-cleaning-wrong-data](../(6)(3)pd-cleaning-wrong-data) - Yanlış veri
- [(6)(4)pd-cleaning-duplicates](../(6)(4)pd-cleaning-duplicates) - Duplicate temizleme
- [Ana README](../README.md) - Genel bakış

## 📖 Referans

- [W3Schools - Cleaning Empty Cells](https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp)
