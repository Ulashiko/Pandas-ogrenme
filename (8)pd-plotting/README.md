# Pandas Grafik Oluşturma (Plotting)

Bu klasör pandas kütüphanesi ile veri görselleştirme metodlarını içerir. Matplotlib kullanarak veri setlerinizi grafiklerle nasıl görselleştireceğinizi öğrenin.

## 📁 Dosyalar

- **main.py** - Plotting örnekleri (basic plot, scatter, histogram)
- **kahve_satis_verisi.csv** - 100 kayıtlık kahve satış verisi

## 🚀 Kullanım

```bash
cd "(8)pd-plotting"
python main.py
```

## 📊 Veri Seti Hakkında

**kahve_satis_verisi.csv** - Kahve Satış Verisi
- **Siparis_ID**: Sipariş kimlik numarası (1001-1100)
- **Tarih**: Sipariş tarihi (Ocak 2024)
- **Urun**: Ürün adı (Latte, Espresso, Filtre Kahve, Muffin, Kurabiye, Sandviç)
- **Adet**: Sipariş adedi (1-4 arası)
- **Kategori**: Ürün kategorisi (İçecek/Yiyecek)
- **Birim_Fiyat**: Ürünün birim fiyatı (TL)
- **Toplam_Kazanc**: Toplam satış tutarı (TL)

## 🎨 Grafik Oluşturma Nedir?

**Plotting (Grafik Oluşturma)**: Verileri görsel formatta sunma işlemidir. Pandas, matplotlib kütüphanesini kullanarak kolay ve hızlı bir şekilde grafikler oluşturmanıza olanak tanır.

### Neden Grafik Kullanırız?

| Amaç | Açıklama |
|------|----------|
| **Veri Keşfi** | Verilerdeki desenleri ve eğilimleri görselleştir |
| **İlişki Analizi** | İki değişken arasındaki ilişkiyi anla |
| **Dağılım** | Verilerin nasıl dağıldığını gör |
| **Sunum** | Bulguları başkalarına göster |
| **Outlier Tespiti** | Aykırı değerleri kolayca tespit et |

## 📝 plot() Metodu

Pandas'ın temel görselleştirme metodudur. Matplotlib'in pyplot modülü ile birlikte çalışır.

### Temel Kullanım

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('veri.csv')
df.plot()
plt.show()
```

### Gerekli Kütüphaneler

```python
import pandas as pd              # Veri işleme
import matplotlib.pyplot as plt  # Grafik görüntüleme
```

**Önemli**: `plt.show()` grafikleri görüntülemek için zorunludur!

## 🔑 Grafik Türleri

### 1. Temel Grafik (Line Plot)

**Kullanım**: Zaman serisi verileri, trendler

```python
df['Toplam_Kazanc'].plot()
plt.title('Kazanç Trendi')
plt.show()
```

**Ne zaman kullanılır?**
- Zaman içindeki değişimi göstermek için
- Trendleri analiz etmek için

---

### 2. Scatter Plot (Dağılım Grafiği)

**Kullanım**: İki değişken arasındaki ilişki

```python
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc')
plt.show()
```

**Parametreler**:
- `kind='scatter'`: Scatter plot türünü belirtir
- `x`: X eksenindeki kolon adı
- `y`: Y eksenindeki kolon adı

**Ne zaman kullanılır?**
- İki değişken arasındaki korelasyonu görmek için
- Pozitif/negatif ilişkileri tespit etmek için
- Outlier'ları (aykırı değerleri) bulmak için

**Örnek Yorumlama**:
```python
# Scatter plot sonrası korelasyon hesapla
correlation = df['Adet'].corr(df['Toplam_Kazanc'])
print(f"Korelasyon: {correlation}")

# Yorum:
# 0.8 - 1.0   : Çok güçlü pozitif ilişki
# 0.6 - 0.8   : Güçlü pozitif ilişki
# 0.4 - 0.6   : Orta ilişki
# 0.0 - 0.4   : Zayıf ilişki
# < 0         : Negatif ilişki
```

---

### 3. Histogram (Frekans Dağılımı)

**Kullanım**: Tek bir değişkenin dağılımı

```python
df['Toplam_Kazanc'].plot(kind='hist')
plt.show()
```

**Parametreler**:
- `kind='hist'`: Histogram türünü belirtir
- `bins`: Çubuk sayısı (varsayılan: 10)
- `edgecolor`: Çubukların kenar rengi

**Ne zaman kullanılır?**
- Verilerin nasıl dağıldığını görmek için
- En sık görülen değerleri bulmak için
- Veri setinin şeklini (normal dağılım, çarpık, vb.) anlamak için

**Histogram Özellikleri**:
```python
# Histogram sadece TEK kolon gerektirir
df['Toplam_Kazanc'].plot(kind='hist', bins=15)

# Çoklu histogram (aynı grafikte)
df[['Adet', 'Birim_Fiyat']].plot(kind='hist', alpha=0.5)
```

## 🎓 Grafik Türleri ve Kullanım Senaryoları

### Grafik Seçim Tablosu

| Grafik Türü | kind Değeri | Veri Türü | Kullanım Amacı |
|-------------|-------------|-----------|----------------|
| **Line Plot** | (varsayılan) | Zaman serisi | Trendleri göstermek |
| **Scatter Plot** | 'scatter' | İki sayısal değişken | İlişki analizi |
| **Histogram** | 'hist' | Tek sayısal değişken | Dağılım göstermek |
| **Bar Chart** | 'bar' | Kategorik + sayısal | Kategorileri karşılaştırmak |
| **Box Plot** | 'box' | Sayısal değişkenler | Outlier ve çeyrekler |
| **Pie Chart** | 'pie' | Kategorik (oranlar) | Yüzdelik dağılım |

### Hangi Grafiği Ne Zaman Kullanmalı?

#### Scenario 1: Zaman İçinde Değişim
```python
# SORU: Satışlar zaman içinde nasıl değişiyor?
# CEVAP: Line plot
df['Toplam_Kazanc'].plot()
```

#### Scenario 2: İki Değişken İlişkisi
```python
# SORU: Adet ile kazanç arasında ilişki var mı?
# CEVAP: Scatter plot
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc')
```

#### Scenario 3: Değerlerin Dağılımı
```python
# SORU: Kazançlar hangi aralıkta yoğunlaşıyor?
# CEVAP: Histogram
df['Toplam_Kazanc'].plot(kind='hist')
```

## 💡 Grafik Özelleştirme

### Başlık ve Etiketler

```python
df['Toplam_Kazanc'].plot()
plt.title('Toplam Kazanç Trendi')        # Başlık
plt.xlabel('Sipariş Numarası')           # X ekseni etiketi
plt.ylabel('Kazanç (TL)')                # Y ekseni etiketi
plt.show()
```

### Renk ve Stil

```python
# Renk değiştirme
df['Toplam_Kazanc'].plot(color='red')

# Scatter plot rengi
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc', color='green')

# Histogram rengi ve kenar
df['Adet'].plot(kind='hist', color='coral', edgecolor='black')
```

### Grid (Izgara) Ekleme

```python
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc')
plt.grid(True, alpha=0.3)  # alpha: şeffaflık (0-1)
plt.show()
```

### Şeffaflık (Alpha)

```python
# Üst üste binen noktaları görmek için
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc', alpha=0.5)
```

### Grafik Boyutu

```python
df['Toplam_Kazanc'].plot(figsize=(10, 6))  # genişlik, yükseklik
plt.show()
```

### Grafik Kaydetme

```python
df.plot()
plt.savefig('grafik.png')  # PNG olarak kaydet
plt.savefig('grafik.pdf')  # PDF olarak kaydet
plt.show()
```

## 🔬 İleri Düzey Özellikler

### Çoklu Grafik (Subplots)

```python
# Yan yana grafikler
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Sol grafik
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc', ax=axes[0])
axes[0].set_title('Adet vs Kazanç')

# Sağ grafik
df['Toplam_Kazanc'].plot(kind='hist', ax=axes[1])
axes[1].set_title('Kazanç Dağılımı')

plt.tight_layout()
plt.show()
```

### Alt Alta Grafikler

```python
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# Üst grafik
df['Toplam_Kazanc'].plot(ax=axes[0])
axes[0].set_title('Kazanç Trendi')

# Alt grafik
df['Adet'].plot(ax=axes[1], color='red')
axes[1].set_title('Adet Trendi')

plt.tight_layout()
plt.show()
```

### Histogram Bins (Çubuk Sayısı)

```python
# Az çubuk (genel görünüm)
df['Toplam_Kazanc'].plot(kind='hist', bins=5)

# Orta çubuk (dengeli)
df['Toplam_Kazanc'].plot(kind='hist', bins=15)

# Çok çubuk (detaylı)
df['Toplam_Kazanc'].plot(kind='hist', bins=50)
```

**Kural**: Veri sayısı / 10 iyi bir başlangıçtır.

## 📈 main.py'deki Örnekler

### 1. Temel Grafik
- Tüm kolonların grafiği
- Toplam kazanç trend grafiği

### 2. Scatter Plot
- Adet vs Toplam Kazanç ilişkisi
- Birim Fiyat vs Toplam Kazanç ilişkisi
- Korelasyon hesaplamaları

### 3. Histogram
- Toplam kazanç dağılımı
- Sipariş adet dağılımı
- Birim fiyat dağılımı

### 4. Özelleştirme
- Başlık ve etiketler
- Renkler ve stiller
- Grid ekleme
- Grafikleri kaydetme

## 🎯 Gerçek Dünya Örnekleri

### Örnek 1: E-Ticaret Satış Analizi

```python
# Scatter: Reklam bütçesi vs satış
df.plot(kind='scatter', x='Ad_Budget', y='Sales')
plt.title('Reklam Bütçesi ve Satış İlişkisi')
plt.show()

# Histogram: Satış dağılımı
df['Sales'].plot(kind='hist', bins=20)
plt.title('Satış Dağılımı')
plt.show()
```

**Kullanım**: Hangi reklam bütçesi en çok satış getiriyor?

---

### Örnek 2: Öğrenci Performans Analizi

```python
# Scatter: Çalışma saati vs sınav notu
df.plot(kind='scatter', x='Study_Hours', y='Exam_Score')
plt.title('Çalışma Saati ve Not İlişkisi')
plt.show()

# Histogram: Not dağılımı
df['Exam_Score'].plot(kind='hist', bins=10)
plt.title('Sınav Notu Dağılımı')
plt.show()
```

**Kullanım**: Çalışma saati ile not arasında ilişki var mı?

---

### Örnek 3: Hava Durumu Analizi

```python
# Line plot: Sıcaklık trendi
df['Temperature'].plot()
plt.title('Aylık Sıcaklık Trendi')
plt.xlabel('Gün')
plt.ylabel('Sıcaklık (°C)')
plt.show()

# Histogram: Sıcaklık dağılımı
df['Temperature'].plot(kind='hist', bins=15)
plt.title('Sıcaklık Dağılımı')
plt.show()
```

**Kullanım**: Sıcaklık zaman içinde nasıl değişiyor?

## ⚠️ Önemli Notlar ve Uyarılar

### 1. plt.show() Kullanımı

```python
# YANLIŞ: show() çağrılmadan grafik görünmez
df.plot()

# DOĞRU: Her grafikten sonra show() çağır
df.plot()
plt.show()
```

---

### 2. Scatter Plot İçin x ve y Zorunlu

```python
# YANLIŞ: x ve y belirtilmemiş
df.plot(kind='scatter')  # HATA!

# DOĞRU: x ve y belirtilmiş
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc')
```

---

### 3. Histogram Sadece Tek Kolon

```python
# DOĞRU: Tek kolon
df['Toplam_Kazanc'].plot(kind='hist')

# YANLIŞ: Çoklu kolon direkt histogram olmaz
df.plot(kind='hist')  # Beklenmeyen sonuç
```

---

### 4. Sayısal Kolonlar Gerekli

```python
# String kolonlar grafiğe alınamaz
# Önce sayısal kolonları seç
numeric_df = df.select_dtypes(include=['number'])
numeric_df.plot()
```

---

### 5. Grafik Üst Üste Binmesin

```python
# Her grafikten sonra show() veya close()
df['Toplam_Kazanc'].plot()
plt.show()  # Grafiği göster ve kapat

df['Adet'].plot()
plt.show()  # Yeni grafik
```

## 💻 Grafik Komutları Cheat Sheet

### Temel Plot Komutları

```python
# 1. TEMEL GRAFİK (Line plot)
df.plot()
df['Kolon'].plot()

# 2. SCATTER PLOT
df.plot(kind='scatter', x='Kolon1', y='Kolon2')

# 3. HISTOGRAM
df['Kolon'].plot(kind='hist')
df['Kolon'].plot(kind='hist', bins=20)

# 4. BAR CHART
df['Kategori'].value_counts().plot(kind='bar')

# 5. BOX PLOT
df.plot(kind='box')

# 6. PIE CHART
df['Kategori'].value_counts().plot(kind='pie')
```

### Özelleştirme Komutları

```python
# Başlık ve etiketler
plt.title('Grafik Başlığı')
plt.xlabel('X Ekseni')
plt.ylabel('Y Ekseni')

# Renk ve stil
df.plot(color='red')
df.plot(kind='scatter', x='X', y='Y', color='blue', alpha=0.5)

# Grid
plt.grid(True)
plt.grid(True, alpha=0.3)

# Grafik boyutu
df.plot(figsize=(10, 6))

# Kaydetme
plt.savefig('grafik.png')
plt.savefig('grafik.png', dpi=300)  # Yüksek çözünürlük

# Gösterme
plt.show()
```

### Çoklu Grafik

```python
# Yan yana
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
df.plot(ax=axes[0])
df.plot(kind='hist', ax=axes[1])
plt.tight_layout()
plt.show()

# Alt alta
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
df['Kolon1'].plot(ax=axes[0])
df['Kolon2'].plot(ax=axes[1])
plt.tight_layout()
plt.show()
```

## 🧮 Pratik Örnekler

### Veri Keşfi İçin Grafik

```python
import pandas as pd
import matplotlib.pyplot as plt

# Veri yükle
df = pd.read_csv('kahve_satis_verisi.csv')

# 1. Hızlı genel bakış
df.plot()
plt.title('Tüm Kolonlar')
plt.show()

# 2. İlişki analizi
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc')
plt.title('Adet vs Kazanç')
print(f"Korelasyon: {df['Adet'].corr(df['Toplam_Kazanc']):.3f}")
plt.show()

# 3. Dağılım analizi
df['Toplam_Kazanc'].plot(kind='hist', bins=15, edgecolor='black')
plt.title('Kazanç Dağılımı')
plt.show()

# 4. Özet
print(df.describe())
```

### Kategorik Veri Görselleştirme

```python
# Ürün sayıları
df['Urun'].value_counts().plot(kind='bar')
plt.title('Ürün Satış Sayıları')
plt.xlabel('Ürün')
plt.ylabel('Satış Adedi')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Kategori oranları
df['Kategori'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Kategori Dağılımı')
plt.ylabel('')  # Pie chart'ta y etiketi kaldır
plt.show()
```

## 🔗 İlgili Bölümler

- [(0)pd-start](../(0)pd-start) - Pandas'a başlangıç
- [(1)pd-series](../(1)pd-series) - Series yapısı
- [(2)pd-dataframe](../(2)pd-dataframe) - DataFrame temelleri
- [(3)pd-loc_iloc](../(3)pd-loc_iloc) - İndeksleme işlemleri
- [(4)pd-json-load](../(4)pd-json-load) - JSON okuma işlemleri
- [(5)pd-analyzing-data](../(5)pd-analyzing-data) - Veri analizi metodları
- [(6)pd-cleaning-data](../(6)pd-cleaning-data) - Veri temizleme
- [(7)pd-correlations](../(7)pd-correlations) - Korelasyon analizi

## 📖 Referanslar

- [W3Schools - Pandas Plotting](https://www.w3schools.com/python/pandas/pandas_plotting.asp)
- [Pandas Documentation - plot()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## 🎓 Öğrenme Hedefleri

Bu modülü tamamladığınızda:

- ✅ `plot()` metodunu kullanabilirsiniz
- ✅ Scatter plot ile ilişki analizi yapabilirsiniz
- ✅ Histogram ile dağılım analizi yapabilirsiniz
- ✅ Grafikleri özelleştirebilirsiniz (başlık, renk, grid)
- ✅ Grafikleri kaydedebilirsiniz
- ✅ Hangi durum için hangi grafiğin uygun olduğunu bilirsiniz
- ✅ Matplotlib ile Pandas'ı birlikte kullanabilirsiniz

## 💡 En İyi Uygulamalar (Best Practices)

### ✅ Yapılması Gerekenler

1. **Her Zaman plt.show() Kullan**
   ```python
   df.plot()
   plt.show()  # Mutlaka!
   ```

2. **Anlamlı Başlık ve Etiketler Ekle**
   ```python
   df.plot()
   plt.title('Satış Trendi')
   plt.xlabel('Ay')
   plt.ylabel('Satış (TL)')
   plt.show()
   ```

3. **Doğru Grafik Türünü Seç**
   - İlişki → Scatter
   - Dağılım → Histogram
   - Trend → Line plot

4. **Grafikleri Kaydet**
   ```python
   plt.savefig('grafik.png', dpi=300, bbox_inches='tight')
   ```

### ❌ Yaygın Hatalar

1. **plt.show() Unutmak**
   ```python
   # YANLIŞ
   df.plot()  # Grafik görünmez

   # DOĞRU
   df.plot()
   plt.show()
   ```

2. **Scatter İçin x, y Belirtmemek**
   ```python
   # YANLIŞ
   df.plot(kind='scatter')  # HATA!

   # DOĞRU
   df.plot(kind='scatter', x='Adet', y='Kazanc')
   ```

3. **String Kolonları Grafiklemeye Çalışmak**
   ```python
   # YANLIŞ
   df['Urun'].plot()  # String, sayısal değil

   # DOĞRU
   df['Urun'].value_counts().plot(kind='bar')
   ```

4. **Çok Fazla Bins Kullanmak**
   ```python
   # YANLIŞ: Çok detaylı, anlaşılmaz
   df['Kazanc'].plot(kind='hist', bins=100)

   # DOĞRU: Dengeli
   df['Kazanc'].plot(kind='hist', bins=15)
   ```

## 🚀 Hızlı Başlangıç

```python
# 1. Kütüphaneleri içe aktar
import pandas as pd
import matplotlib.pyplot as plt

# 2. Veri yükle
df = pd.read_csv('kahve_satis_verisi.csv')

# 3. İlk grafiğinizi oluşturun
df['Toplam_Kazanc'].plot()
plt.title('Toplam Kazanç')
plt.show()

# 4. Scatter plot deneyin
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc')
plt.title('Adet vs Kazanç')
plt.show()

# 5. Histogram oluşturun
df['Toplam_Kazanc'].plot(kind='hist', bins=15)
plt.title('Kazanç Dağılımı')
plt.show()
```

---

**📊 Kahve satış verileri ile grafik oluşturmayı öğrenin! Görselleştirme, veri analizinin en güçlü araçlarından biridir.**
