# Pandas Korelasyon Analizi (Data Correlations)

Bu klasör pandas kütüphanesi ile korelasyon analizi metodlarını içerir. İki veya daha fazla değişken arasındaki ilişkileri nasıl ölçeceğinizi öğrenin.

## 📁 Dosyalar

- **workout_data.csv** - 50 kayıtlık egzersiz verisi
- **main.py** - Kapsamlı korelasyon analizi örnekleri

## 🚀 Kullanım

```bash
cd "(7)pd-correlations"
python main.py
```

## 📊 Veri Seti Hakkında

**workout_data.csv** - Egzersiz Performans Verisi
- **Duration**: Egzersiz süresi (dakika) - 30, 45, 60
- **Pulse**: Ortalama nabız (bpm) - 90-120 arası
- **Maxpulse**: Maksimum nabız (bpm) - 120-175 arası
- **Calories**: Yakılan kalori - 195-479 arası

⚠️ **Not**: Veri setinde kasıtlı olarak boş değerler bulunmaktadır (Calories kolonunda 3 adet). Bu, `corr()` metodunun boş değerlerle nasıl çalıştığını göstermek içindir.

## 🎯 Korelasyon Nedir?

**Korelasyon (Correlation)**: İki değişken arasındaki **doğrusal (linear) ilişkinin** gücünü ve yönünü ölçen istatistiksel bir değerdir.

### Korelasyon Değerleri

| Değer | Anlamı | Örnek |
|-------|--------|-------|
| **+1.0** | Mükemmel pozitif ilişki | Egzersiz süresi ↑ → Kalori ↑↑ |
| **+0.9** | Çok güçlü pozitif | Hız ↑ → Mesafe ↑↑ |
| **+0.6** | Güçlü pozitif | Boy ↑ → Kilo ↑ |
| **+0.3** | Orta pozitif | Sıcaklık ↑ → Dondurma satışı ↑ |
| **0.0** | İlişki yok | Ayakkabı numarası ↔ IQ |
| **-0.3** | Orta negatif | Uyku ↑ → Hata sayısı ↓ |
| **-0.6** | Güçlü negatif | Egzersiz ↑ → Ağırlık ↓ |
| **-0.9** | Çok güçlü negatif | Hız ↑ → Varış süresi ↓↓ |
| **-1.0** | Mükemmel negatif ilişki | Kalan süre ↑ → Geçen süre ↓↓ |

### Pratik Kural

```
|korelasyon| >= 0.6  →  Güçlü ilişki, tahmin yapılabilir ✅
|korelasyon| <  0.6  →  Zayıf ilişki, tahmin zor ❌
```

## 📝 corr() Metodu

### Temel Kullanım

```python
import pandas as pd

df = pd.read_csv('workout_data.csv')

# Tüm sayısal kolonlar arasındaki korelasyon
correlation_matrix = df.corr()
print(correlation_matrix)
```

### Çıktı Örneği

```
          Duration     Pulse  Maxpulse  Calories
Duration  1.000000  0.154321  0.009403  0.922721
Pulse     0.154321  1.000000  0.434567  0.287654
Maxpulse  0.009403  0.434567  1.000000  0.032145
Calories  0.922721  0.287654  0.032145  1.000000
```

### Çıktıyı Okuma

1. **Köşegen (diagonal)**: Her zaman 1.0 (kolon kendisiyle)
2. **Simetrik**: Duration→Calories = Calories→Duration
3. **Duration-Calories: 0.922721** → Çok güçlü pozitif ilişki! ✅
   - "Ne kadar uzun egzersiz, o kadar çok kalori"
4. **Duration-Maxpulse: 0.009403** → Çok zayıf ilişki ❌
   - "Süreye bakarak max nabzı tahmin edemeyiz"

## 🔑 Korelasyon Metodları

### 1. Tüm Kolonlar Arası Korelasyon

```python
df.corr()
```

**Açıklama**: Tüm sayısal kolonlar arasındaki korelasyon matrisini döndürür. String kolonlar otomatik olarak göz ardı edilir.

---

### 2. Belirli Bir Kolonla Korelasyon

```python
df.corr()['Calories']
```

**Açıklama**: Sadece Calories kolonunun diğerleriyle korelasyonunu gösterir.

**Sıralama ile**:
```python
df.corr()['Calories'].sort_values(ascending=False)
```

**Çıktı**:
```
Calories    1.000000    # Kendisi
Duration    0.922721    # En güçlü ilişki
Pulse       0.287654
Maxpulse    0.032145    # En zayıf ilişki
```

---

### 3. İki Kolon Arasındaki Korelasyon

```python
# Yöntem 1: Loc ile
df.corr().loc['Duration', 'Calories']

# Yöntem 2: Alt küme ile
df[['Duration', 'Calories']].corr()
```

**Çıktı**: Tek bir sayı (örn: 0.922721)

---

### 4. Güçlü Korelasyonları Filtreleme

```python
# Korelasyonu 0.6'dan büyük olan çiftler
corr_matrix = df.corr()
strong_corr = corr_matrix[abs(corr_matrix) >= 0.6]
print(strong_corr)
```

## 🎓 Korelasyon Analizi Adım Adım

### Adım 1: Veriyi Hazırla

```python
import pandas as pd

df = pd.read_csv('workout_data.csv')

# Veriyi incele
print(df.info())
print(df.describe())

# Boş değerleri kontrol et
print(df.isnull().sum())
```

### Adım 2: Korelasyon Matrisini Oluştur

```python
# Korelasyon matrisini hesapla
correlation = df.corr()
print(correlation)
```

### Adım 3: Güçlü İlişkileri Tespit Et

```python
# Calories ile en çok ilişkili kolonlar
print(correlation['Calories'].sort_values(ascending=False))
```

### Adım 4: Yorumla ve Karar Ver

```python
duration_calories = correlation.loc['Duration', 'Calories']

if abs(duration_calories) >= 0.6:
    print("Güçlü ilişki! Duration'dan Calories tahmin edilebilir")
else:
    print("Zayıf ilişki, tahmin zor")
```

## 💡 Pratik Kullanım Senaryoları

### 1. Tahmin Modellemesi (Predictive Modeling)

```python
# Hangi değişkenler hedef değişkeni (target) tahmin edebilir?
target = 'Calories'
predictors = df.corr()[target].abs().sort_values(ascending=False)
print(predictors[predictors >= 0.6])  # Güçlü ilişkiler
```

**Kullanım**: Makine öğrenmesinde hangi feature'ları kullanacağınıza karar verin.

---

### 2. Çoklu Doğrusal Bağlantılık (Multicollinearity)

```python
# Birbirine çok benzeyen kolonları tespit et
corr_matrix = df.corr()

# 0.95'ten büyük korelasyonlar (kendisi hariç)
for i in range(len(corr_matrix.columns)):
    for j in range(i+1, len(corr_matrix.columns)):
        if abs(corr_matrix.iloc[i, j]) > 0.95:
            print(f"{corr_matrix.columns[i]} ve {corr_matrix.columns[j]}")
```

**Kullanım**: Regresyon modellerinde bir kolon çıkarılabilir (gereksiz).

---

### 3. Veri Keşfi (Data Exploration)

```python
# İlginç ilişkileri bulun
print(df.corr())
```

**Kullanım**: Beklenmedik ilişkileri keşfedin, veriyi daha iyi anlayın.

---

### 4. Feature Engineering

```python
# Yüksek korelasyonlu kolonlardan yeni feature
if df.corr().loc['Duration', 'Pulse'] > 0.5:
    df['Workout_Intensity'] = df['Duration'] * df['Pulse']
```

**Kullanım**: Güçlü ilişkili kolonlardan yeni özellikler türetin.

## ⚠️ Önemli Uyarılar

### 1. Korelasyon ≠ Nedensellik

```python
# Yüksek korelasyon ≠ Biri diğerine sebep oluyor

# ÖRNEK:
# Dondurma Satışı ile Boğulma Vakası arasında yüksek korelasyon
# Ama dondurma boğulmaya sebep OLMUYOR!
# İkisi de yazın artıyor (gizli değişken: sıcaklık)
```

**Ders**: Korelasyon ilişkiyi gösterir ama sebep-sonuç ilişkisini kanıtlamaz!

---

### 2. Sadece Doğrusal İlişkiler

```python
# corr() sadece LINEAR ilişkileri ölçer
# Karmaşık non-linear ilişkiler tespit edilemez

# ÖRNEK:
# y = x² ilişkisi var ama korelasyon düşük çıkabilir
# Çünkü ilişki doğrusal değil!
```

---

### 3. Outlier'ların Etkisi

```python
# Aykırı değerler korelasyonu bozabilir
# Önce outlier'ları temizleyin, sonra korelasyon hesaplayın

# Outlier'sız korelasyon
df_clean = df[(df['Calories'] < 500)]
print(df_clean.corr())
```

---

### 4. Boş Değerler

```python
# corr() metodu boş değerleri otomatik atlar
# Ancak çok fazla boş değer varsa korelasyon yanıltıcı olabilir

# Boş değer oranını kontrol et
print((df.isnull().sum() / len(df) * 100))

# %50'den fazla boş değer varsa dikkatli ol!
```

## 🔬 Korelasyon Katsayısı Hesaplama

### Pearson Korelasyon Formülü

Pandas `corr()` metodu varsayılan olarak **Pearson korelasyon katsayısını** kullanır:

```
r = Σ((x - x̄)(y - ȳ)) / √(Σ(x - x̄)² × Σ(y - ȳ)²)

r: Korelasyon katsayısı
x, y: Değişkenler
x̄, ȳ: Ortalamalar
```

### Korelasyon Metod Türleri

```python
# Pearson (varsayılan) - doğrusal ilişki
df.corr(method='pearson')

# Spearman - sıralı ilişki (rank correlation)
df.corr(method='spearman')

# Kendall - sıralı ilişki (alternatif)
df.corr(method='kendall')
```

**Not**: Pearson çoğu durumda yeterlidir.

## 📈 main.py'deki Örnekler

### 1. Temel Korelasyon Matrisi
```python
correlation_matrix = df.corr()
print(correlation_matrix)
```

### 2. Korelasyon Yorumlama
- Duration-Calories: Güçlü pozitif
- Duration-Maxpulse: Zayıf ilişki

### 3. Belirli Kolona Göre Sıralama
```python
df.corr()['Calories'].sort_values(ascending=False)
```

### 4. Güçlü Korelasyonları Bulma
- |korelasyon| >= 0.6 olan çiftler

### 5. Negatif Korelasyon Kontrolü
- Ters yönlü ilişkileri tespit etme

### 6. Boş Değerlerin Etkisi
- `corr()` boş değerleri nasıl işler?

### 7. Korelasyon Matrisi Özellikleri
- Simetrik yapı
- Köşegen = 1.0
- Sadece sayısal kolonlar

## 🎯 Gerçek Dünya Örnekleri

### Örnek 1: E-Ticaret
```python
# Hangi faktörler satışı etkiliyor?
df = pd.read_csv('sales_data.csv')
print(df.corr()['Sales'].sort_values(ascending=False))

# Çıktı:
# Advertising_Budget    0.85  -> Güçlü!
# Website_Traffic       0.72  -> Güçlü!
# Product_Price        -0.32  -> Zayıf negatif
# Season                0.15  -> Çok zayıf
```

---

### Örnek 2: Emlak Fiyatları
```python
# Ev fiyatını ne etkiliyor?
df = pd.read_csv('house_prices.csv')
print(df.corr()['Price'].sort_values(ascending=False))

# Olası Çıktı:
# Square_Feet     0.78  -> Güçlü! (alan ↑ → fiyat ↑)
# Bedrooms        0.52  -> Orta
# Age            -0.43  -> Orta negatif (eski ev → ucuz)
# Distance       -0.65  -> Güçlü negatif (uzak → ucuz)
```

---

### Örnek 3: Öğrenci Başarısı
```python
# Sınav notunu ne etkiliyor?
df = pd.read_csv('student_grades.csv')
print(df.corr()['Exam_Score'].sort_values(ascending=False))

# Olası Çıktı:
# Study_Hours      0.82  -> Güçlü! (çalışma ↑ → not ↑)
# Attendance       0.67  -> Güçlü (devam ↑ → not ↑)
# Sleep_Hours      0.38  -> Orta
# Social_Media    -0.55  -> Orta negatif (sosyal medya ↑ → not ↓)
```

## 🔗 Korelasyon ile Neler Yapabilirsiniz?

### ✅ Yapabilecekleriniz

1. **Feature Selection**: En önemli değişkenleri seçin
2. **Veri Keşfi**: Beklenmedik ilişkileri bulun
3. **Multicollinearity**: Gereksiz kolonları tespit edin
4. **Tahmin**: Bir değişkenden diğerini tahmin edin (basit modeller)

### ❌ Yapamayacaklarınız

1. **Sebep-Sonuç**: Korelasyon nedensellik kanıtlamaz
2. **Non-linear İlişkiler**: Karmaşık ilişkileri göremez
3. **Kategorik Değişkenler**: Sadece sayısal verilerle çalışır

## 🧮 Korelasyon Matrisi Özellikleri

### Simetrik Matris
```
corr(A, B) = corr(B, A)

Duration → Calories = 0.922721
Calories → Duration = 0.922721  (aynı!)
```

### Köşegen Her Zaman 1.0
```
corr(Duration, Duration) = 1.0
corr(Pulse, Pulse) = 1.0
corr(Calories, Calories) = 1.0
```

### Sadece Sayısal Kolonlar
```python
# String kolonlar otomatik atlanır
df = pd.DataFrame({
    'Name': ['Ali', 'Ayşe'],      # Atlanır
    'Age': [25, 30],               # Dahil
    'Score': [85, 90]              # Dahil
})

df.corr()  # Sadece Age ve Score
```

## 📊 İleri Düzey Kullanım

### Korelasyon Heatmap (Isı Haritası)

Korelasyon matrisini görselleştirmek için:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('workout_data.csv')
correlation_matrix = df.corr()

# Heatmap oluştur
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Korelasyon Isı Haritası')
plt.show()
```

**Not**: Bu örnek `matplotlib` ve `seaborn` gerektirir. Kurulum:
```bash
pip install matplotlib seaborn
```

### Korelasyon Eşik Değeri Uygulama

```python
# Sadece güçlü korelasyonları göster
corr_matrix = df.corr()
strong_corr = corr_matrix[(abs(corr_matrix) >= 0.6) & (corr_matrix != 1.0)]
print(strong_corr)
```

## 💡 En İyi Uygulamalar (Best Practices)

### ✅ Yapılması Gerekenler

1. **Önce Veriyi Temizleyin**
   ```python
   # Boş değerleri doldur veya çıkar
   df = df.dropna()  # veya df.fillna(df.mean())

   # Sonra korelasyon hesapla
   print(df.corr())
   ```

2. **Outlier'ları Kontrol Edin**
   ```python
   # Önce outlier'ları temizle
   Q1 = df['Calories'].quantile(0.25)
   Q3 = df['Calories'].quantile(0.75)
   IQR = Q3 - Q1
   df_clean = df[(df['Calories'] >= Q1-1.5*IQR) &
                 (df['Calories'] <= Q3+1.5*IQR)]

   # Sonra korelasyon
   print(df_clean.corr())
   ```

3. **Veri Tiplerini Doğrulayın**
   ```python
   # Sayısal olmayan kolonlar var mı?
   print(df.dtypes)

   # Sadece sayısalları seç
   numeric_df = df.select_dtypes(include=['number'])
   print(numeric_df.corr())
   ```

4. **Sonuçları Görselleştirin**
   - Heatmap ile daha kolay anlaşılır
   - Scatter plot ile ilişkiyi görün

### ❌ Yaygın Hatalar

1. **Korelasyonu Nedensellik Sanmak**
   ```python
   # YANLIŞ: "Duration yüksek korelasyona sahip, o yüzeden Calories'e sebep"
   # DOĞRU: "Duration ve Calories ilişkili, ama hangisi sebep belli değil"
   ```

2. **Non-linear İlişkileri Gözden Kaçırmak**
   ```python
   # Korelasyon düşük ama güçlü non-linear ilişki olabilir
   # Örnek: y = x² (parabol) düşük korelasyon verebilir
   ```

3. **Boş Değerleri Görmezden Gelmek**
   ```python
   # YANLIŞ: Boş değerlerle direk corr()
   # DOĞRU: Önce boş değerleri temizle/doldur
   ```

4. **Outlier'ları Temizlememek**
   ```python
   # Aykırı değerler korelasyonu bozabilir
   # Önce df.describe() ile outlier'ları kontrol edin
   ```

## 🔗 İlgili Bölümler

- [(0)pd-start](../(0)pd-start) - Pandas'a başlangıç
- [(1)pd-series](../(1)pd-series) - Series yapısı
- [(2)pd-dataframe](../(2)pd-dataframe) - DataFrame temelleri
- [(3)pd-loc_iloc](../(3)pd-loc_iloc) - İndeksleme işlemleri
- [(4)pd-json-load](../(4)pd-json-load) - JSON okuma işlemleri
- [(5)pd-analyzing-data](../(5)pd-analyzing-data) - Veri analizi metodları (korelasyon dahil)
- [(6)pd-cleaning-data](../(6)pd-cleaning-data) - Veri temizleme (korelasyon öncesi önemli!)

## 📖 Referanslar

- [W3Schools - Pandas Correlations](https://www.w3schools.com/python/pandas/pandas_correlations.asp)
- [Pandas Documentation - corr()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)
- [Statistics - Correlation Coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)

## 🎓 Öğrenme Hedefleri

Bu modülü tamamladığınızda:

- ✅ `corr()` metodunu kullanabilirsiniz
- ✅ Korelasyon değerlerini yorumlayabilirsiniz
- ✅ Güçlü ve zayıf ilişkileri ayırt edebilirsiniz
- ✅ Korelasyon matrisini okuyabilirsiniz
- ✅ Korelasyon != Nedensellik ayrımını bilirsiniz
- ✅ Pratik veri bilimi senaryolarında korelasyon kullanabilirsiniz

## 🚀 Cheat Sheet

### Temel Korelasyon Komutları

```python
# 1. TÜM KORELASYONLAR - Tüm sayısal kolonlar arası
df.corr()

# 2. BELİRLİ KOLON İLE - Sadece Calories'in diğerleriyle korelasyonu
df.corr()['Calories']

# 3. SIRALI - En yüksekten en düşüğe
df.corr()['Calories'].sort_values(ascending=False)

# 4. İKİ KOLON ARASI - Tek bir korelasyon değeri
df.corr().loc['Duration', 'Calories']

# 5. ALT KÜME - Sadece seçili kolonlar arasında
df[['Duration', 'Calories']].corr()

# 6. GÜÇLÜ KORELASYONLAR - Filtreleme
corr_matrix = df.corr()
strong = corr_matrix[abs(corr_matrix) >= 0.6]
print(strong)

# 7. METOD SEÇİMİ
df.corr(method='pearson')   # Varsayılan - doğrusal ilişki
df.corr(method='spearman')  # Sıralı ilişki (rank)
df.corr(method='kendall')   # Alternatif rank correlation
```

### Pratik İpuçları

```python
# Belirli kolon için en güçlü ilişkileri bul
target = 'Calories'
df.corr()[target].abs().sort_values(ascending=False).head(5)

# Negatif korelasyonları bul
negative = df.corr()[df.corr() < 0]
print(negative)

# Kendisi hariç korelasyonlar (köşegen değil)
import numpy as np
corr = df.corr()
corr[corr == 1.0] = np.nan  # Kendisini null yap
print(corr)

# Yüksek korelasyonlu çiftleri listele
for col1 in df.columns:
    for col2 in df.columns:
        if col1 < col2:  # Tekrarı önle
            corr_val = df.corr().loc[col1, col2]
            if abs(corr_val) >= 0.6:
                print(f"{col1} <-> {col2}: {corr_val:.3f}")
```

### Korelasyon Yorumlama Tablosu

```
|Değer|     Anlamı              Kullanım
---------------------------------------------------
 1.00      Mükemmel pozitif     Neredeyse aynı bilgi
 0.90      Çok güçlü            Tahmin yapılabilir ✅
 0.70      Güçlü                Tahmin yapılabilir ✅
 0.50      Orta                 Orta seviye ilişki
 0.30      Zayıf                Tahmin zor
 0.00      İlişki yok           Bağımsız değişkenler
-0.30      Zayıf negatif        Ters yönlü ama zayıf
-0.50      Orta negatif         Orta seviye ters ilişki
-0.70      Güçlü negatif        Ters tahmin yapılabilir ✅
-0.90      Çok güçlü negatif    Ters yönde çok güçlü ✅
-1.00      Mükemmel negatif     Tam ters ilişki
```

---

**💪 Egzersiz verileri ile korelasyon analizi öğrenin! Bu, veri bilimi ve makine öğrenmesinin temel taşlarından biridir.**
