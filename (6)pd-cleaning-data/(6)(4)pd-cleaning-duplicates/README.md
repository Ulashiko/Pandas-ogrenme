# Pandas ile Tekrar Eden Verileri Temizleme (Cleaning Duplicates)

Bu klasör pandas kütüphanesi ile tekrar eden (duplicate) verileri tespit etme ve temizleme yöntemlerini içerir.

## 🚀 Kullanım

```bash
python main.py
```

## 📊 Veri Seti

F1 pilotları verisi (`../f1_data.csv`) - Script, test için duplicate ekler

## 📝 Kapsanan Metodlar

### 1. duplicated() - Tespit Etme

```python
# Duplicate var mı?
df.duplicated()                    # Her satır için True/False
df.duplicated().sum()              # Kaç tane duplicate?

# Duplicate olan satırları göster
df[df.duplicated()]
```

### 2. keep Parametresi

```python
# İlk görünümü tut, diğerleri duplicate
df.duplicated(keep='first')   # [F, F, T, T]

# Son görünümü tut, diğerleri duplicate
df.duplicated(keep='last')    # [T, T, F, F]

# Hepsini duplicate olarak işaretle
df.duplicated(keep=False)     # [T, T, T, T]
```

**Örnek**:
```python
df = pd.DataFrame({
    'Pilot': ['Max', 'Max', 'Max', 'Lewis']
})

df.duplicated(keep='first')   # [False, True, True, False]
df.duplicated(keep='last')    # [True, True, False, False]
df.duplicated(keep=False)     # [True, True, True, False]
```

### 3. drop_duplicates() - Silme

```python
# Tüm duplicate'leri sil
df.drop_duplicates()

# İlk görünümü tut
df.drop_duplicates(keep='first')    # Varsayılan

# Son görünümü tut
df.drop_duplicates(keep='last')

# Hiçbirini tutma (hepsini sil)
df.drop_duplicates(keep=False)
```

### 4. subset - Belirli Kolonlara Göre

```python
# Sadece Pilot kolonuna göre
df.drop_duplicates(subset=['Pilot'])

# Pilot ve Takim kombinasyonuna göre
df.drop_duplicates(subset=['Pilot', 'Takim'])

# Birden fazla kolon
df.drop_duplicates(subset=['Pilot', 'Puan', 'Yas'])
```

### 5. Koşullu Duplicate Temizleme

```python
# Aynı Pilot varsa en yüksek puanlıyı tut
df_sorted = df.sort_values('Puan', ascending=False)
df_unique = df_sorted.drop_duplicates(subset=['Pilot'], keep='first')

# En düşük yaşlıyı tut
df_sorted = df.sort_values('Yas', ascending=True)
df_unique = df_sorted.drop_duplicates(subset=['Pilot'], keep='first')

# En güncel (son kayıt) tut
df_sorted = df.sort_values('Tarih', ascending=False)
df_unique = df_sorted.drop_duplicates(subset=['ID'], keep='first')
```

### 6. Duplicate Analizi

```python
# Her değerden kaç tane var?
df['Pilot'].value_counts()

# Birden fazla olanlar
counts = df['Pilot'].value_counts()
duplicates = counts[counts > 1]

# Unique sayısı
df['Pilot'].nunique()

# Groupby ile
df.groupby('Pilot').size()

# Detaylı analiz
df.groupby('Pilot').agg({
    'Puan': ['count', 'mean', 'max']
})
```

## 🎯 keep Parametresi Detaylı

### Örnek Veri
```python
df = pd.DataFrame({
    'Pilot': ['Max', 'Lewis', 'Max', 'Max', 'Charles'],
    'Puan': [100, 90, 100, 85, 80]
})
```

### keep='first' (Varsayılan)
İlk görünümü tut:
```
Pilot    Puan
Max      100    ← Tutulur
Lewis    90     ← Tutulur
Charles  80     ← Tutulur
```

### keep='last'
Son görünümü tut:
```
Pilot    Puan
Lewis    90     ← Tutulur
Max      85     ← Tutulur
Charles  80     ← Tutulur
```

### keep=False
Hiçbir duplicate'i tutma:
```
Pilot    Puan
Lewis    90     ← Tutulur (duplicate değil)
Charles  80     ← Tutulur (duplicate değil)
```

## 💡 Pratik Senaryolar

### Senaryo 1: En Güncel Kaydı Tut
```python
df = df.sort_values('TarihSaat', ascending=False)
df = df.drop_duplicates(subset=['MusteriID'], keep='first')
```

### Senaryo 2: En Yüksek Değeri Tut
```python
df = df.sort_values('Gelir', ascending=False)
df = df.drop_duplicates(subset=['Sirket'], keep='first')
```

### Senaryo 3: Tamamen Aynı Satırları Sil
```python
df = df.drop_duplicates()
```

### Senaryo 4: Duplicate Varsa Hepsini Sil
```python
df = df.drop_duplicates(subset=['Email'], keep=False)
```

## ⚠️ Duplicate Ne Zaman Sorun?

### Sorun Olabilir ✗
- Veri girişi hatası (aynı kayıt 2 kez)
- Database merge hatası
- İstatistiksel analiz (frekansları bozar)
- Model eğitimi (bias oluşturur)

### Sorun Olmayabilir ✓
- Zaman serisi (aynı kişi her gün kayıt yapabilir)
- Log dosyaları
- Transaction kayıtları
- Sensor verisi

## 🔍 Duplicate Tespit Stratejisi

```
1. TÜM VERIYI KONTROL ET
   df.duplicated().sum()
   ↓
2. HANGİ KOLONLARA GÖRE?
   df.duplicated(subset=['ID']).sum()
   ↓
3. DUPLICATE'LERİ İNCELE
   df[df.duplicated(keep=False)]
   ↓
4. NEDENINI ANLA
   Veri hatası mı? Normalmali mi?
   ↓
5. STRATEJİ BELİRLE
   Sil? İlkini tut? Sonuncuyu tut?
   ↓
6. UYGULA ve DOĞRULA
   df.drop_duplicates()
```

## 💡 İpuçları

1. **subset kullan**: Anahtar kolonları belirle
2. **keep='first' > keep=False**: Genelde ilkini tutmak daha güvenli
3. **Sıralama önemli**: İlkini tutuyorsan önce sırala
4. **Backup al**: Duplicate silmeden önce df.copy()
5. **Doğrula**: Silme sonrası .nunique() ile kontrol et

## 🔗 İlgili Bölümler

- [(6)(1)pd-cleaning-empty-cells](../(6)(1)pd-cleaning-empty-cells) - Boş değer temizleme
- [(6)(2)pd-cleaning-wrong-format](../(6)(2)pd-cleaning-wrong-format) - Format düzeltme
- [(6)(3)pd-cleaning-wrong-data](../(6)(3)pd-cleaning-wrong-data) - Yanlış veri
- [Ana README](../README.md) - Genel bakış

## 📖 Referans

- [W3Schools - Cleaning Duplicates](https://www.w3schools.com/python/pandas/pandas_cleaning_duplicates.asp)
