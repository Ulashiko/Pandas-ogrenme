# Pandas ile Yanlış Formatları Düzeltme (Cleaning Wrong Format)

Bu klasör pandas kütüphanesi ile yanlış formattaki verileri düzeltme yöntemlerini içerir.

## 🚀 Kullanım

```bash
python main.py
```

## 📊 Veri Seti

F1 pilotları verisi (`../f1_data.csv`) - 20 kayıt

## 📝 Kapsanan Metodlar

### 1. to_numeric() - Sayısal Dönüşüm

```python
# Güvenli dönüşüm (hata varsa NaN)
pd.to_numeric(df['Puan'], errors='coerce')

# Hata varsa ValueError fırlat
pd.to_numeric(df['Puan'], errors='raise')

# Hata varsa olduğu gibi bırak
pd.to_numeric(df['Puan'], errors='ignore')
```

**errors parametresi**:
- `coerce`: Hata varsa NaN yap (en güvenli)
- `raise`: Hata varsa exception fırlat
- `ignore`: Hata varsa hiçbir şey yapma

### 2. astype() - Tip Dönüşümü

```python
df['Puan'].astype(int)          # Integer'a çevir
df['YarisSuresi'].astype(float) # Float'a çevir
df['Pilot'].astype(str)         # String'e çevir
```

⚠️ **Dikkat**: Boş değer varsa `astype()` hata verir! Önce `to_numeric()` kullanın.

### 3. String Metodları

```python
df['Pilot'].str.strip()     # Baş/son boşlukları sil
df['Takim'].str.upper()     # BÜYÜK HARF
df['Pilot'].str.lower()     # küçük harf
df['Takim'].str.title()     # Her Kelime Büyük
df['Pilot'].str.capitalize() # İlk harf büyük
```

### 4. replace() - Değer Değiştirme

```python
# Tek değer
df['Ulke'].replace('Ingiltere', 'İngiltere')

# Çoklu değer
df['Ulke'].replace({
    'Ingiltere': 'İngiltere',
    'Ispanya': 'İspanya'
})

# Regex ile
df['Puan'].replace(0, pd.NA)
```

### 5. clip() - Aralık Sınırlama

```python
# Min-Max sınırlama
df['Puan'].clip(0, 600)        # 0-600 arası
df['Yas'].clip(lower=18)       # En az 18
df['Puan'].clip(upper=500)     # En fazla 500
```

### 6. apply() - Özel Fonksiyon

```python
# Fonksiyon tanımla
def kisalt(takim):
    return takim[:2].upper()

df['TakimKisa'] = df['Takim'].apply(kisalt)

# Lambda ile
df['TakimKisa'] = df['Takim'].apply(lambda x: x[:2])
```

### 7. round() - Yuvarlama

```python
df['Puan'].round(0)     # Tam sayıya yuvarla
df['Oran'].round(2)     # 2 ondalık basamak
```

## 🎯 Format Düzeltme Stratejisi

```
1. VERİ TİPLERİNİ KONTROL ET
   df.dtypes
   ↓
2. SAYISAL OLMASI GEREKENLERI DÖNÜŞTÜR
   pd.to_numeric(errors='coerce')
   ↓
3. STRING'LERİ TEMİZLE
   .str.strip(), .str.upper()
   ↓
4. KATEGORİK VERİLERİ STANDARTLAŞTIR
   .replace() veya .apply()
   ↓
5. ARALIKLARI KONTROL ET
   .clip()
   ↓
6. SONUCU DOĞRULA
   df.info(), df.describe()
```

## 🔑 Önemli Metodlar

| Metod | Kullanım | Ne Zaman |
|-------|----------|----------|
| `pd.to_numeric()` | String → Number | Güvenli dönüşüm |
| `.astype()` | Tip dönüşüm | Kesin dönüşüm |
| `.str.strip()` | Boşluk temizle | Her zaman |
| `.replace()` | Değer değiştir | Kategorik |
| `.clip()` | Sınırla | Aralık kontrolü |
| `.apply()` | Özel fonksiyon | Karmaşık işlem |

## 💡 İpuçları

1. **to_numeric() önce**: Sayısal dönüşümde önce `to_numeric(errors='coerce')` kullanın
2. **Strip her zaman**: String kolonlarda her zaman `.str.strip()` kullanın
3. **Kategorik standart**: Kategorik verileri mutlaka standartlaştırın
4. **apply() son çare**: Mümkünse built-in metodları kullanın, apply() yavaştır

## 🔗 İlgili Bölümler

- [(6)(1)pd-cleaning-empty-cells](../(6)(1)pd-cleaning-empty-cells) - Boş değer temizleme
- [(6)(3)pd-cleaning-wrong-data](../(6)(3)pd-cleaning-wrong-data) - Yanlış veri
- [(6)(4)pd-cleaning-duplicates](../(6)(4)pd-cleaning-duplicates) - Duplicate temizleme
- [Ana README](../README.md) - Genel bakış

## 📖 Referans

- [W3Schools - Cleaning Wrong Format](https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp)
