# Pandas ile Veri Analizi (Data Analyzing)

Bu klasör pandas kütüphanesi ile veri analizi metodlarını içerir. W3Schools Pandas Analyzing Data tutorialından esinlenilmiştir.

## 📁 Dosyalar

- **data.csv** - 206 kayıtlık egzersiz verisi (Duration, Pulse, Maxpulse, Calories)
- **main.py** - Kapsamlı veri analizi örnekleri

## 🚀 Kullanım

```bash
python main.py
```

## 📊 Veri Seti Hakkında

CSV dosyası egzersiz verilerini içerir:
- **Duration**: Egzersiz süresi (dakika)
- **Pulse**: Nabız (bpm)
- **Maxpulse**: Maksimum nabız (bpm)
- **Calories**: Yakılan kalori

⚠️ **Not**: Veri setinde kasıtlı olarak boş değerler bulunmaktadır (özellikle Calories kolonunda). Bu, gerçek dünya verilerini simüle eder ve veri temizleme işlemlerini öğrenmek için kullanılır.

## 📝 Kapsanan Analiz Metodları

### 1. head() ve tail()
```python
df.head()      # İlk 5 satır
df.head(10)    # İlk 10 satır
df.tail()      # Son 5 satır
df.tail(10)    # Son 10 satır
```

**Kullanım Amacı**: Veriyi hızlıca görüntülemek

### 2. info()
```python
df.info()
```

**Çıktı**:
- Toplam satır sayısı
- Her kolonun adı
- Null olmayan değer sayısı
- Veri tipi
- Bellek kullanımı

**Kullanım Amacı**: DataFrame hakkında genel bilgi almak, null değerleri tespit etmek

### 3. describe()
```python
df.describe()
```

**Çıktı** (sayısal kolonlar için):
- count: Değer sayısı
- mean: Ortalama
- std: Standart sapma
- min: Minimum değer
- 25%, 50%, 75%: Yüzdelik dilimler
- max: Maksimum değer

### 4. shape
```python
df.shape        # (satır_sayısı, sutun_sayısı)
df.shape[0]     # Satır sayısı
df.shape[1]     # Sutun sayısı
```

### 5. columns
```python
df.columns              # Sutun isimleri
df.columns.tolist()     # Liste olarak
```

### 6. dtypes
```python
df.dtypes   # Her kolonun veri tipi
```

### 7. index
```python
df.index    # Index bilgisi
```

### 8. isnull()
```python
df.isnull()                          # Boolean DataFrame
df.isnull().sum()                    # Her kolondaki null sayısı
df.isnull().sum().sum()              # Toplam null sayısı
(df.isnull().sum() / len(df) * 100) # Yüzde olarak
```

### 9. nunique()
```python
df.nunique()            # Her kolondaki benzersiz değer sayısı
df['Pulse'].nunique()   # Bir kolondaki benzersiz değer sayısı
```

### 10. value_counts()
```python
df['Duration'].value_counts()   # Değer frekansları
```

### 11. sample()
```python
df.sample(5)      # Rastgele 5 satır
df.sample(frac=0.1)  # %10'luk rastgele örnek
```

### 12. memory_usage()
```python
df.memory_usage(deep=True)              # Her kolonun bellek kullanımı
df.memory_usage(deep=True).sum()        # Toplam bellek
```

### 13. corr()
```python
df.corr()   # Korelasyon matrisi (sayısal kolonlar arası ilişki)
```

**Korelasyon değerleri**:
- 1.0: Tam pozitif ilişki
- 0.0: İlişki yok
- -1.0: Tam negatif ilişki

### 14. Detaylı İstatistikler
```python
df['Column'].mean()      # Ortalama
df['Column'].median()    # Medyan
df['Column'].mode()      # Mod (en sık değer)
df['Column'].std()       # Standart sapma
df['Column'].min()       # Minimum
df['Column'].max()       # Maksimum
df['Column'].count()     # Null olmayan değer sayısı
```

### 15. quantile()
```python
df['Calories'].quantile(0.25)   # %25'lik dilim
df['Calories'].quantile(0.50)   # %50'lik dilim (medyan)
df['Calories'].quantile(0.75)   # %75'lik dilim
df['Calories'].quantile(0.90)   # %90'lık dilim
```

### 16. select_dtypes()
```python
df.select_dtypes(include=['number'])    # Sadece sayısal kolonlar
df.select_dtypes(include=['object'])    # Sadece string kolonlar
df.select_dtypes(exclude=['number'])    # Sayısal olmayanlar
```

## 🎯 Pratik Kullanım Örnekleri

### Hızlı Veri Keşfi
```python
# 1. İlk ve son satırlara bak
df.head()
df.tail()

# 2. Genel bilgi al
df.info()

# 3. İstatistiksel özet
df.describe()

# 4. Null değerleri kontrol et
df.isnull().sum()
```

### Veri Kalitesi Kontrolü
```python
# Null değer oranları
print((df.isnull().sum() / len(df) * 100).round(2))

# Benzersiz değer sayıları
print(df.nunique())

# Veri tipleri doğru mu?
print(df.dtypes)
```

### Korelasyon Analizi
```python
# Hangi değişkenler birbirine bağlı?
print(df.corr())

# Calories ile en çok ilişkili kolon
print(df.corr()['Calories'].sort_values(ascending=False))
```

## 📈 Örnek Çıktılar

### info() Çıktısı
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 206 entries, 0 to 205
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  206 non-null    int64
 1   Pulse     203 non-null    float64
 2   Maxpulse  205 non-null    float64
 3   Calories  105 non-null    float64
dtypes: float64(3), int64(1)
memory usage: 6.6 KB
```

### describe() Çıktısı
```
         Duration       Pulse    Maxpulse    Calories
count  206.000000  203.000000  205.000000  105.000000
mean    54.757282  103.418719  131.185366  290.583810
std      7.321157    7.488410    8.740529   53.292883
min     30.000000   70.000000  104.000000  180.100000
25%     45.000000  100.000000  125.000000  253.000000
50%     60.000000  105.000000  132.000000  280.000000
75%     60.000000  110.000000  136.000000  329.300000
max     60.000000  120.000000  175.000000  479.000000
```

## 🔑 Önemli Metodlar Özet Tablosu

| Metod | Açıklama | Kullanım |
|-------|----------|----------|
| `head(n)` | İlk n satır | `df.head(10)` |
| `tail(n)` | Son n satır | `df.tail(5)` |
| `info()` | Genel bilgi | `df.info()` |
| `describe()` | İstatistiksel özet | `df.describe()` |
| `shape` | Boyut (satır, sütun) | `df.shape` |
| `columns` | Sütun isimleri | `df.columns` |
| `dtypes` | Veri tipleri | `df.dtypes` |
| `isnull()` | Null değer kontrolü | `df.isnull().sum()` |
| `nunique()` | Benzersiz değer sayısı | `df.nunique()` |
| `value_counts()` | Değer frekansları | `df['col'].value_counts()` |
| `corr()` | Korelasyon matrisi | `df.corr()` |
| `sample(n)` | Rastgele n satır | `df.sample(5)` |

## 💡 İpuçları

1. **İlk Analiz**: Her zaman `df.info()` ve `df.describe()` ile başlayın
2. **Null Değerler**: `df.isnull().sum()` ile boş değerleri tespit edin
3. **Veri Kalitesi**: Beklenmeyen veri tiplerini `df.dtypes` ile kontrol edin
4. **Korelasyon**: Sayısal değişkenler arası ilişkiyi `df.corr()` ile keşfedin
5. **Hızlı Görüntüleme**: `head()` ve `tail()` ile veriye hızlıca göz atın
6. **Rastgele Örnekleme**: Büyük veri setlerinde `sample()` kullanın

## 🔗 İlgili Bölümler

- [(0)pd-start](../(0)pd-start) - Pandas'a başlangıç
- [(1)pd-series](../(1)pd-series) - Series yapısı
- [(2)pd-dataframe](../(2)pd-dataframe) - DataFrame temelleri
- [(3)pd-loc_iloc](../(3)pd-loc_iloc) - İndeksleme işlemleri
- [(4)pd-json-load](../(4)pd-json-load) - JSON okuma işlemleri

## 📖 Referans

- [W3Schools - Pandas Analyzing Data](https://www.w3schools.com/python/pandas/pandas_analyzing.asp)
