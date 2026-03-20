import pandas as pd

print("=" * 80)
print("PANDAS KORELASYON ANALIZI (CORRELATION ANALYSIS)")
print("=" * 80)

# Veriyi oku
df = pd.read_csv('workout_data.csv')

print("\n" + "=" * 80)
print("VERI SETI HAKKINDA")
print("=" * 80)
print("\nIlk 10 satir:")
print(df.head(10))

print("\n\nVeri seti bilgisi:")
print(df.info())

print("\n\nIstatistiksel ozet:")
print(df.describe())

# 1. KORELASYON MATRISI (CORRELATION MATRIX)
print("\n" + "=" * 80)
print("1. KORELASYON MATRISI - df.corr()")
print("=" * 80)
print("""
KORELASYON NEDIR?
- Iki degisken arasindaki dogrusal (linear) iliskiyi olcer
- Bir degisken arttikca digeri nasil degisir?
- Deger araligi: -1 ile +1 arasinda

KORELASYON DEGERLERI:
  +1.0  = Mukemmel POZITIF korelasyon (biri artarsa digeri de artar)
  +0.9  = Cok guclu pozitif korelasyon
  +0.6  = Guclu pozitif korelasyon (tahmin yapilabilir)
  +0.3  = Orta pozitif korelasyon
   0.0  = Hic iliski yok
  -0.3  = Orta negatif korelasyon
  -0.6  = Guclu negatif korelasyon (biri artarsa digeri azalir)
  -0.9  = Cok guclu negatif korelasyon
  -1.0  = Mukemmel NEGATIF korelasyon

PRATIK KURAL:
- |korelasyon| >= 0.6 -> Guclu iliski, tahmin yapilabilir
- |korelasyon| < 0.6  -> Zayif iliski, tahmin zor
""")

print("\nKORELASYON MATRISI:")
print("-" * 80)
correlation_matrix = df.corr()
print(correlation_matrix)


# 2. KORELASYON MATRISINI ANLAMA

print("\n" + "=" * 80)
print("2. KORELASYON MATRISINI YORUMLAMA")
print("=" * 80)

print("\n2.1. HER KOLON KENDISIYLE MUKEMMEL KORELASYONA SAHIPTIR (1.0)")
print("-" * 80)
print(f"Duration - Duration: {correlation_matrix.loc['Duration', 'Duration']:.6f}")
print(f"Calories - Calories: {correlation_matrix.loc['Calories', 'Calories']:.6f}")
print("-> Her kolon kendisiyle mukemmel uyumludur (degeri 1.000000)")

print("\n2.2. DURATION VE CALORIES ARASINDAKI ILISKI")
print("-" * 80)
duration_calories_corr = correlation_matrix.loc['Duration', 'Calories']
print(f"Duration - Calories korelasyonu: {duration_calories_corr:.6f}")

if abs(duration_calories_corr) >= 0.6:
    print(f"-> GUCLU KORELASYON! ({duration_calories_corr:.3f})")
    if duration_calories_corr > 0:
        print("-> YORUM: Egzersiz suresi arttikca yakilan kalori de artar!")
        print("-> PRATIK: Sureden kaloriyi tahmin edebiliriz.")
    else:
        print("-> YORUM: Egzersiz suresi arttikca yakilan kalori azalir (mantikli degil!)")
else:
    print(f"-> Zayif korelasyon ({duration_calories_corr:.3f})")
    print("-> YORUM: Sureden kaloriyi tahmin etmek zor")

print("\n2.3. DURATION VE MAXPULSE ARASINDAKI ILISKI")
print("-" * 80)
duration_maxpulse_corr = correlation_matrix.loc['Duration', 'Maxpulse']
print(f"Duration - Maxpulse korelasyonu: {duration_maxpulse_corr:.6f}")

if abs(duration_maxpulse_corr) >= 0.6:
    print(f"-> GUCLU KORELASYON! ({duration_maxpulse_corr:.3f})")
else:
    print(f"-> ZAYIF KORELASYON ({duration_maxpulse_corr:.3f})")
    print("-> YORUM: Egzersiz suresine bakarak max nabzi tahmin edemeyiz!")
    print("-> PRATIK: Farkli faktorler max nabzi etkiliyor (kondisyon, yas, vb)")

print("\n2.4. PULSE VE MAXPULSE ARASINDAKI ILISKI")
print("-" * 80)
pulse_maxpulse_corr = correlation_matrix.loc['Pulse', 'Maxpulse']
print(f"Pulse - Maxpulse korelasyonu: {pulse_maxpulse_corr:.6f}")

if abs(pulse_maxpulse_corr) >= 0.6:
    print(f"-> GUCLU KORELASYON! ({pulse_maxpulse_corr:.3f})")
    print("-> YORUM: Ortalama nabiz ile max nabiz arasinda guclu iliski var")
else:
    print(f"-> Orta/Zayif korelasyon ({pulse_maxpulse_corr:.3f})")

# =============================================================================
# 3. BELIRLI BIR KOLONA GORE KORELASYONLARI SIRALAMA
# =============================================================================
print("\n" + "=" * 80)
print("3. CALORIES ILE EN COK ILISKILI KOLONLAR")
print("=" * 80)
print("\nCalories kolonunun diger kolonlarla korelasyonu (buyukten kucuge):")
print("-" * 80)
calories_correlations = correlation_matrix['Calories'].sort_values(ascending=False)
print(calories_correlations)

print("\nYORUM:")
print("-" * 80)
for column, corr_value in calories_correlations.items():
    if column == 'Calories':
        print(f"  {column:12} -> {corr_value:.3f} (kendisi)")
    elif abs(corr_value) >= 0.6:
        print(f"  {column:12} -> {corr_value:.3f} (GUCLU iliski)")
    elif abs(corr_value) >= 0.3:
        print(f"  {column:12} -> {corr_value:.3f} (Orta iliski)")
    else:
        print(f"  {column:12} -> {corr_value:.3f} (Zayif iliski)")

# =============================================================================
# 4. SADECE BELIRLI KOLONLAR ARASINDA KORELASYON
# =============================================================================
print("\n" + "=" * 80)
print("4. BELIRLI KOLONLAR ARASINDA KORELASYON")
print("=" * 80)
print("\nSadece Duration ve Calories arasindaki korelasyon:")
print("-" * 80)
specific_corr = df[['Duration', 'Calories']].corr()
print(specific_corr)

# =============================================================================
# 5. KORELASYON MATRISINDE FILTRELEME
# =============================================================================
print("\n" + "=" * 80)
print("5. GUCLU KORELASYONLARI BULMA (|korelasyon| >= 0.6)")
print("=" * 80)

print("\nGuclu korelasyonlara sahip kolon ciftleri:")
print("-" * 80)
# Korelasyon matrisini duzlestir (flatten)
corr_pairs = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        col1 = correlation_matrix.columns[i]
        col2 = correlation_matrix.columns[j]
        corr_value = correlation_matrix.iloc[i, j]

        if abs(corr_value) >= 0.6:
            corr_pairs.append((col1, col2, corr_value))

if corr_pairs:
    for col1, col2, corr_value in sorted(corr_pairs, key=lambda x: abs(x[2]), reverse=True):
        print(f"  {col1:12} <-> {col2:12}: {corr_value:7.3f}")
else:
    print("  Guclu korelasyon bulunamadi (|korelasyon| >= 0.6)")

# =============================================================================
# 6. NEGATIF KORELASYON ORNEGI
# =============================================================================
print("\n" + "=" * 80)
print("6. NEGATIF KORELASYON ORNEGI")
print("=" * 80)
print("""
NEGATIF KORELASYON: Bir degisken arttikca digeri azalir

ORNEK SENARYOLAR:
- Egzersiz Suresi vs Dinlenme Suresi (biri artarsa digeri azalir)
- Yas vs Hiz (genelde yas arttikca hiz azalir)
- Arac Agirligi vs Yakit Ekonomisi (agir arac = daha fazla yakit)

Bu veri setinde negatif korelasyonlar:
""")
print("-" * 80)

negative_corrs = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        col1 = correlation_matrix.columns[i]
        col2 = correlation_matrix.columns[j]
        corr_value = correlation_matrix.iloc[i, j]

        if corr_value < 0:
            negative_corrs.append((col1, col2, corr_value))

if negative_corrs:
    for col1, col2, corr_value in sorted(negative_corrs, key=lambda x: x[2]):
        print(f"  {col1:12} <-> {col2:12}: {corr_value:7.3f}")
        if abs(corr_value) >= 0.6:
            print(f"    -> Guclu negatif iliski!")
else:
    print("  Bu veri setinde negatif korelasyon yok")

# =============================================================================
# 7. BOS DEGERLERIN KORELASYONA ETKISI
# =============================================================================
print("\n" + "=" * 80)
print("7. BOS DEGERLERIN (NULL) KORELASYONA ETKISI")
print("=" * 80)
print("\nVeri setindeki bos degerler:")
print("-" * 80)
print(df.isnull().sum())

print("\n\nONEMLI:")
print("-" * 80)
print("""
- df.corr() metodu otomatik olarak bos degerleri (null/NaN) GORMUYOR
- Her kolon cifti icin sadece her ikisinde de deger olan satirlari kullanir
- Bu sayede korelasyon hesaplanabilir
- Ancak cok fazla bos deger varsa korelasyon yaniltici olabilir!

ONERI:
- Korelasyon analizinden once bos degerleri doldurun (fillna)
- Veya bos degerleri cikarin (dropna)
- Bos deger orani %50'den fazlaysa dikkatli olun
""")

# =============================================================================
# 8. KORELASYON MATRISI OZELLIKLERI
# =============================================================================
print("\n" + "=" * 80)
print("8. KORELASYON MATRISI OZELLIKLERI")
print("=" * 80)

print("\n8.1. SIMETRIK MATRIS")
print("-" * 80)
print("Duration-Calories ile Calories-Duration ayni degerdir:")
print(f"  Duration -> Calories: {correlation_matrix.loc['Duration', 'Calories']:.6f}")
print(f"  Calories -> Duration: {correlation_matrix.loc['Calories', 'Duration']:.6f}")

print("\n8.2. CAPRAZ KORELASYON (1.0)")
print("-" * 80)
print("Matrisin kosegeni her zaman 1.0'dir (kolon kendisiyle):")
print(f"  Duration-Duration: {correlation_matrix.loc['Duration', 'Duration']}")
print(f"  Pulse-Pulse: {correlation_matrix.loc['Pulse', 'Pulse']}")
print(f"  Maxpulse-Maxpulse: {correlation_matrix.loc['Maxpulse', 'Maxpulse']}")
print(f"  Calories-Calories: {correlation_matrix.loc['Calories', 'Calories']}")

print("\n8.3. SADECE SAYISAL KOLONLAR")
print("-" * 80)
print("corr() metodu otomatik olarak sadece sayisal kolonlari kullanir")
print(f"  Sayisal kolonlar: {df.select_dtypes(include=['number']).columns.tolist()}")

# =============================================================================
# 9. PRATIK KULLANIM SENARYOLARI
# =============================================================================
print("\n" + "=" * 80)
print("9. PRATIK KULLANIM SENARYOLARI")
print("=" * 80)

print("""
9.1. TAHMIN MODELLEMESI
----------------------------------------------
- Guclu korelasyona sahip degiskenler birbirini tahmin edebilir
- Ornek: Duration'dan Calories'i tahmin edebilirsiniz
- Makine ogrenmesinde feature selection icin kullanilir

9.2. COKLU DOGRUSAL BAGLANTILIK (MULTICOLLINEARITY)
----------------------------------------------
- Iki bagimsiz degisken birbiriyle cok yuksek korelasyona sahipse
- Regresyon modellerinde problem olusturabilir
- Cozum: Biri cikarilabilir veya birlestirilebilir

9.3. VERI KEŞFI
----------------------------------------------
- Hangi degiskenler birbirine bagli?
- Beklenmedik iliskiler var mi?
- Hangi kolonlar birbiriyle benzer bilgi tasiyor?

9.4. FEATURE ENGINEERING
----------------------------------------------
- Yuksek korelasyona sahip kolonlardan yeni ozellikler turetebilirsiniz
- Ornek: Duration * Pulse -> Egzersiz yogunlugu

9.5. VERI TEMIZLEME
----------------------------------------------
- Cok yuksek korelasyon (> 0.95) -> biri gereksiz olabilir
- Hic korelasyon yok (~ 0.0) -> hedef degisken icin faydali olmayabilir
""")

# =============================================================================
# 10. OZET VE EN IYI UYGULAMALAR
# =============================================================================
print("\n" + "=" * 80)
print("OZET VE EN IYI UYGULAMALAR")
print("=" * 80)

print("""
KORELASYON ANALIZI ADIM ADIM:
====================================
1. Veriyi yukleyin ve inceleyin (df.info(), df.describe())
2. Bos degerleri kontrol edin (df.isnull().sum())
3. Korelasyon matrisini olusturun (df.corr())
4. Guclu korelasyonlari tespit edin (|korelasyon| >= 0.6)
5. Ilginc iliski ve patternleri yorumlayin
6. Bulduglarinizi modellemede veya feature engineering'de kullanin

UNUTMAYIN:
====================================
- Korelasyon != Nedensellik (correlation != causation)
  Iki degisken iliskili olabilir ama biri digeri sebep olmayabilir!

- Korelasyon sadece DOGRUSAL iliskileri olcer
  Karmasik non-linear iliskiler tespit edilemez

- Korelasyon outlier'lara duyarlidir
  Aykiri degerler korelasyonu bozabilir

- Korelasyon sadece sayisal degiskenler icin calisir
  Kategorik degiskenler icin baska metodlar gerekir

PRATIK ESIK DEGERLERI:
====================================
|Korelasyon|   Yorum               Tahmin Yapilabilir mi?
------------------------------------------------------------
0.9 - 1.0     Cok guclu iliski     Evet, cok iyi
0.6 - 0.9     Guclu iliski         Evet, iyi
0.3 - 0.6     Orta iliski          Mumkun ama zor
0.0 - 0.3     Zayif iliski         Hayir
""")

print("\n" + "=" * 80)
print("KORELASYON ANALIZI TAMAMLANDI!")
print("=" * 80)
