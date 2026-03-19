# Pandas Veri Temizleme Metodları (Data Cleaning Methods)

Bu klasör pandas kütüphanesi ile veri temizleme (data cleaning) işlemlerini içerir. Gerçek dünya verilerinde sıkça karşılaşılan problemleri çözme yöntemlerini öğrenin.

## 📁 Klasör Yapısı

```
(6)pd-cleaning-data/
├── f1_data.csv                          # Ortak F1 veri seti
├── (6)(1)pd-cleaning-empty-cells/       # Boş değer temizleme
├── (6)(2)pd-cleaning-wrong-format/      # Format düzeltme
├── (6)(3)pd-cleaning-wrong-data/        # Yanlış veri düzeltme
├── (6)(4)pd-cleaning-duplicates/        # Duplicate temizleme
└── README.md                            # Bu dosya
```

## 🎯 Veri Seti Hakkında

**f1_data.csv** - Formula 1 Pilotları Verisi (2024 Sezonu)
- 20 pilot
- 6 kolon: Pilot, Takim, YarisSuresi, Puan, Yas, Ulke
- Kasıtlı veri problemleri içerir (eğitim amaçlı):
  - 9 boş değer
  - Format sorunları
  - Muhtemel outlier'lar
  - Test için eklenebilecek duplicate'ler

## 📚 Alt Modüller

### 1️⃣ Boş Hücreleri Temizleme (Cleaning Empty Cells)

**Klasör**: `(6)(1)pd-cleaning-empty-cells/`

**Kapsam**:
- Boş değerleri tespit etme (`isnull()`, `notnull()`)
- Boş satırları silme (`dropna()`)
- Boş değerleri doldurma (`fillna()`)
  - Sabit değer ile
  - Ortalama (mean) ile
  - Medyan (median) ile
  - Mod (mode) ile
- İleri doldurma (`ffill()`)
- Geri doldurma (`bfill()`)
- İnterpolasyon (`interpolate()`)

**Temel Komutlar**:
```python
df.isnull().sum()                    # Boş değer sayısı
df.dropna()                          # Boş satırları sil
df['Puan'].fillna(0)                 # 0 ile doldur
df['Puan'].fillna(df['Puan'].mean()) # Ortalama ile doldur
df['Puan'].ffill()                   # Önceki değerle doldur
```

**W3Schools**: [Cleaning Empty Cells](https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp)

---

### 2️⃣ Yanlış Formatları Düzeltme (Cleaning Wrong Format)

**Klasör**: `(6)(2)pd-cleaning-wrong-format/`

**Kapsam**:
- Sayısal dönüşümler (`to_numeric()`, `astype()`)
- String temizleme (`str.strip()`, `str.upper()`, `str.lower()`)
- Değer değiştirme (`replace()`)
- Aralık sınırlandırma (`clip()`)
- Özel dönüşüm fonksiyonları (`apply()`)

**Temel Komutlar**:
```python
pd.to_numeric(df['Puan'], errors='coerce')  # Sayıya çevir
df['Pilot'].str.strip()                      # Boşlukları temizle
df['Ulke'].replace({'old': 'new'})           # Değer değiştir
df['Puan'].clip(0, 600)                      # Aralık sınırla
df['Takim'].apply(lambda x: x[:2])           # Özel fonksiyon
```

**W3Schools**: [Cleaning Wrong Format](https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_format.asp)

---

### 3️⃣ Yanlış Verileri Düzeltme (Cleaning Wrong Data)

**Klasör**: `(6)(3)pd-cleaning-wrong-data/`

**Kapsam**:
- Outlier (aykırı değer) tespiti
  - IQR metodu
  - Z-Score metodu
- Aralık kontrolü (`between()`)
- Mantıksız değerleri düzeltme (`loc[]`)
- Yanlış satırları silme (`drop()`)
- Veri doğrulama kuralları (custom validation)

**Temel Komutlar**:
```python
# IQR ile outlier tespiti
Q1 = df['Puan'].quantile(0.25)
Q3 = df['Puan'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Puan'] < Q1-1.5*IQR) | (df['Puan'] > Q3+1.5*IQR)]

# Aralık kontrolü
df[df['Yas'].between(18, 50)]

# Değer düzeltme
df.loc[df['Yas'] > 100, 'Yas'] = pd.NA
```

**W3Schools**: [Cleaning Wrong Data](https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_data.asp)

---

### 4️⃣ Tekrar Eden Verileri Temizleme (Cleaning Duplicates)

**Klasör**: `(6)(4)pd-cleaning-duplicates/`

**Kapsam**:
- Duplicate tespiti (`duplicated()`)
- Duplicate silme (`drop_duplicates()`)
- keep parametresi (first, last, False)
- Belirli kolonlara göre duplicate kontrolü (subset)
- Koşullu duplicate temizleme

**Temel Komutlar**:
```python
df.duplicated()                          # Duplicate mu?
df.duplicated().sum()                    # Kaç tane?
df.drop_duplicates()                     # Duplicate'leri sil
df.drop_duplicates(subset=['Pilot'])     # Pilot'a göre
df.drop_duplicates(keep='first')         # İlkini tut
df.drop_duplicates(keep='last')          # Sonuncuyu tut
df.drop_duplicates(keep=False)           # Hiçbirini tutma
```

**W3Schools**: [Cleaning Duplicates](https://www.w3schools.com/python/pandas/pandas_cleaning_duplicates.asp)

---

## 🚀 Hızlı Başlangıç

Tüm modülleri sırayla çalıştırın:

```bash
# 1. Boş değer temizleme
cd "(6)(1)pd-cleaning-empty-cells"
python main.py

# 2. Format düzeltme
cd "../(6)(2)pd-cleaning-wrong-format"
python main.py

# 3. Yanlış veri düzeltme
cd "../(6)(3)pd-cleaning-wrong-data"
python main.py

# 4. Duplicate temizleme
cd "../(6)(4)pd-cleaning-duplicates"
python main.py
```

## 📊 Veri Temizleme İş Akışı (Workflow)

Gerçek projelerde veri temizleme şu sırada yapılır:

```
1. VERİYİ YÜKLE
   ↓
2. VERİYİ İNCELE
   - df.info()
   - df.describe()
   - df.head() / df.tail()
   ↓
3. BOŞ DEĞERLERİ KONTROL ET
   - df.isnull().sum()
   - Boş değer oranları
   ↓
4. DUPLICATE KONTROL ET
   - df.duplicated().sum()
   - df.drop_duplicates()
   ↓
5. VERİ TİPLERİNİ DÜZELT
   - pd.to_numeric()
   - .astype()
   ↓
6. FORMATLARI DÜZELT
   - Tarih formatları
   - String temizleme
   ↓
7. YANLIŞ VERİLERİ DÜZELT
   - Outlier tespiti
   - Aralık kontrolü
   ↓
8. DOĞRULAMA
   - Veri kalitesi kontrolü
   - İstatistiksel analiz
   ↓
9. TEMİZ VERİYİ KAYDET
   - df.to_csv()
```

## 🎓 Örnek: Tam Temizleme İşlemi

```python
import pandas as pd

# 1. Veriyi yükle
df = pd.read_csv('f1_data.csv')
print(f"Orijinal: {len(df)} satır, {len(df.columns)} kolon")

# 2. Duplicate'leri temizle
df = df.drop_duplicates()
print(f"Duplicate temizlendi: {len(df)} satır")

# 3. Boş değerleri doldur
df['YarisSuresi'] = df['YarisSuresi'].fillna(df['YarisSuresi'].median())
df['Puan'] = df['Puan'].fillna(0)
print(f"Boş değerler dolduruldu: {df.isnull().sum().sum()} boş değer kaldı")

# 4. Formatları düzelt
df['Pilot'] = df['Pilot'].str.strip()
df['Puan'] = pd.to_numeric(df['Puan'], errors='coerce')
print("Formatlar düzeltildi")

# 5. Outlier'ları temizle
Q1 = df['Puan'].quantile(0.25)
Q3 = df['Puan'].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df['Puan'] < Q1-1.5*IQR) | (df['Puan'] > Q3+1.5*IQR))]
print(f"Outlier'lar temizlendi: {len(df)} satır kaldı")

# 6. Kaydet
df.to_csv('f1_data_clean.csv', index=False)
print("Temiz veri kaydedildi!")
```

## 🔑 Önemli Pandas Metodları Özeti

### Boş Değer İşlemleri
| Metod | Açıklama |
|-------|----------|
| `df.isnull()` | Boş değerleri tespit et (True/False) |
| `df.notnull()` | Dolu değerleri tespit et (True/False) |
| `df.isnull().sum()` | Her kolondaki boş değer sayısı |
| `df.dropna()` | Boş satırları sil |
| `df.fillna(value)` | Boş değerleri doldur |
| `df.ffill()` | İleri doldur (forward fill) |
| `df.bfill()` | Geri doldur (backward fill) |
| `df.interpolate()` | İnterpolasyon ile doldur |

### Format Düzeltme
| Metod | Açıklama |
|-------|----------|
| `pd.to_numeric()` | String'i sayıya çevir |
| `df.astype()` | Veri tipini değiştir |
| `df.str.strip()` | Boşlukları temizle |
| `df.str.upper()` | Büyük harfe çevir |
| `df.replace()` | Değer değiştir |
| `df.clip()` | Aralık sınırla |
| `df.apply()` | Özel fonksiyon uygula |

### Yanlış Veri Kontrolü
| Metod | Açıklama |
|-------|----------|
| `df.describe()` | İstatistiksel özet |
| `df.quantile()` | Yüzdelik dilimler |
| `df.between()` | Aralık kontrolü |
| `df.loc[]` | Koşullu değer değiştirme |
| `df.drop()` | Satır/kolon silme |
| `df.query()` | SQL benzeri filtreleme |

### Duplicate İşlemleri
| Metod | Açıklama |
|-------|----------|
| `df.duplicated()` | Duplicate tespit et |
| `df.drop_duplicates()` | Duplicate'leri sil |
| `df.nunique()` | Benzersiz değer sayısı |
| `df.value_counts()` | Değer frekansları |

## 💡 Best Practices (En İyi Uygulamalar)

1. **Her Zaman Yedek Alın**
   ```python
   df_backup = df.copy()
   ```

2. **İşlemleri Adım Adım Yapın**
   - Her adımda sonucu kontrol edin
   - Tek seferde çok şey yapmayın

3. **Veriyi İyi Tanıyın**
   - `df.info()`, `df.describe()` ile başlayın
   - Boş değerleri, duplicate'leri, outlier'ları inceleyin

4. **Belgeleme Yapın**
   - Hangi işlemleri yaptığınızı not alın
   - Kodunuza yorum ekleyin

5. **Doğrulama Yapmayı Unutmayın**
   - Temizleme sonrası veriyi kontrol edin
   - İstatistiksel analizlerle doğrulayın

## 🔗 Bu Klasördeki Alt Modüller

- [(6)(1)pd-cleaning-empty-cells](./(6)(1)pd-cleaning-empty-cells) - Boş değer temizleme
- [(6)(2)pd-cleaning-wrong-format](./(6)(2)pd-cleaning-wrong-format) - Format düzeltme
- [(6)(3)pd-cleaning-wrong-data](./(6)(3)pd-cleaning-wrong-data) - Yanlış veri düzeltme
- [(6)(4)pd-cleaning-duplicates](./(6)(4)pd-cleaning-duplicates) - Duplicate temizleme

## 🔗 Diğer İlgili Bölümler

- [(5)pd-analyzing-data](../(5)pd-analyzing-data) - Veri analizi metodları
- [(4)pd-json-load](../(4)pd-json-load) - JSON okuma işlemleri
- [(3)pd-loc_iloc](../(3)pd-loc_iloc) - İndeksleme işlemleri
- [(2)pd-dataframe](../(2)pd-dataframe) - DataFrame temelleri
- [(0)pd-start](../(0)pd-start) - Pandas'a başlangıç

## 📖 Kaynaklar

- [W3Schools - Pandas Cleaning Data](https://www.w3schools.com/python/pandas/pandas_cleaning.asp)
- [Pandas Documentation - Data Cleaning](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Real Python - Data Cleaning Guide](https://realpython.com/python-data-cleaning-numpy-pandas/)

## 📝 Notlar

- Tüm örnekler aynı F1 veri seti (`f1_data.csv`) üzerinden çalışır
- Her modül bağımsız çalışır
- Örnekler eğitim amaçlıdır, gerçek projelerde daha karmaşık durumlarla karşılaşabilirsiniz
- Veri temizleme, veri bilimi iş akışının %80'ini oluşturur!

---

**🏁 Formula 1 verileri ile veri temizleme öğrenin! Her modül gerçek dünya problemlerini çözer.**
