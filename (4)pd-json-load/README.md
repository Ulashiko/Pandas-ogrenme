# Pandas ile JSON Okuma İşlemleri

Bu klasör pandas kütüphanesi ile JSON dosyalarını okuma, işleme ve analiz etme örneklerini içerir.

## 📁 Dosyalar

- **veriler.json** - Örnek çalışan verilerini içeren JSON dosyası
- **main.py** - JSON okuma ve işleme örneklerinin bulunduğu ana script
- **calisanlar_export.json** - DataFrame'den export edilen JSON (records format)
- **calisanlar_table.json** - DataFrame'den export edilen JSON (table format)

## 🚀 Kullanım

Script'i çalıştırmak için:

```bash
python main.py
```

## 📝 Kapsanan Konular

### 1. JSON Okuma Yöntemleri
- Python'un json modülü ile okuma
- `pd.json_normalize()` ile iç içe JSON'ları düzleştirme
- `pd.DataFrame()` ile spesifik key'leri okuma

### 2. Veri Analizi
- `.describe()` - Temel istatistikler
- `.dtypes` - Veri tiplerini görme
- `.isnull()` - Boş değer kontrolü

### 3. Filtreleme İşlemleri
```python
# Tek koşul
df[df['departman'] == 'IT']

# Çoklu koşul
df[(df['sehir'] == 'İstanbul') & (df['departman'] == 'IT')]

# Aralık kontrolü
df[(df['maas'] >= 14000) & (df['maas'] <= 16000)]
```

### 4. Gruplama ve Agregasyon
```python
# Departmana göre ortalama
df.groupby('departman')['maas'].mean()

# Çoklu agregasyon
df.groupby('sehir').agg({
    'maas': ['sum', 'mean', 'count'],
    'tecrube_yili': 'mean'
})
```

### 5. Sıralama
```python
# Azalan sıralama
df.sort_values('maas', ascending=False)

# Artan sıralama
df.sort_values('tecrube_yili')
```

### 6. Yeni Kolonlar Ekleme
```python
# Hesaplama
df['yillik_maas'] = df['maas'] * 12

# Kategorize etme
df['tecrube_seviyesi'] = pd.cut(
    df['tecrube_yili'],
    bins=[0, 3, 5, 10],
    labels=['Junior', 'Mid', 'Senior']
)
```

### 7. JSON Export
```python
# Records formatında
df.to_json('output.json', orient='records', indent=2, force_ascii=False)

# Table formatında
df.to_json('output.json', orient='table', indent=2, force_ascii=False)
```

### 8. İleri Seviye Seçimler
```python
# En yüksek değeri bul
df.loc[df['maas'].idxmax()]

# Koşullu seçim
df[df['tecrube_yili'] >= 5]
```

## 📊 Örnek Veri Yapısı

```json
{
  "calisanlar": [
    {
      "id": 1,
      "isim": "Ahmet Yılmaz",
      "departman": "IT",
      "maas": 15000,
      "sehir": "İstanbul",
      "tecrube_yili": 5
    }
  ],
  "firma_bilgisi": {
    "isim": "Tech Solutions A.Ş.",
    "kurulusYili": 2015,
    "calisanSayisi": 150
  }
}
```

## 🎯 Öğrenilen Pandas Komutları

| Komut | Açıklama |
|-------|----------|
| `pd.json_normalize()` | İç içe JSON'ları düzleştirir |
| `pd.DataFrame()` | Dictionary'den DataFrame oluşturur |
| `.describe()` | Sayısal kolonlar için istatistik |
| `.dtypes` | Veri tiplerini gösterir |
| `.isnull().sum()` | Boş değer sayısı |
| `.groupby()` | Gruplama işlemi |
| `.agg()` | Çoklu agregasyon fonksiyonları |
| `.sort_values()` | Sıralama |
| `.loc[]` | Etiket bazlı indeksleme |
| `.to_json()` | DataFrame'i JSON'a çevirir |
| `pd.cut()` | Sayısal verileri kategorilere böler |

## 💡 İpuçları

1. **JSON Yapısı**: İç içe JSON'lar için `json_normalize()` kullanın
2. **Türkçe Karakterler**: `force_ascii=False` parametresini unutmayın
3. **Okunabilirlik**: `indent=2` ile JSON dosyalarını düzenli yapın
4. **Filtreleme**: Çoklu koşullar için `&` (VE) ve `|` (VEYA) operatörlerini kullanın
5. **Performans**: Büyük veri setlerinde `.loc[]` ve `.iloc[]` daha hızlıdır

## 🔗 İlgili Bölümler

- [(0)pd-start](../(0)pd-start) - Pandas'a başlangıç
- [(1)pd-series](../(1)pd-series) - Series yapısı
- [(2)pd-dataframe](../(2)pd-dataframe) - DataFrame temelleri
- [(3)pd-loc_iloc](../(3)pd-loc_iloc) - İndeksleme işlemleri
