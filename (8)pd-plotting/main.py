# -*- coding: utf-8 -*-
"""
Pandas Plotting - Grafik Oluşturma
====================================
Pandas, matplotlib kütüphanesi kullanarak veri görselleştirme sağlar.
plot() metodu ile çeşitli grafik türleri oluşturulabilir.
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for saving plots
import matplotlib.pyplot as plt

# Veri setini yükle
df = pd.read_csv('../kahve_satis_verisi.csv')

print("Veri Seti:")
print(df.head(10))
print("\n" + "="*70 + "\n")

# =============================================================================
# 1. TEMEL GRAFİK (Basic Plotting)
# =============================================================================
"""
plot() metodu temel grafik oluşturmak için kullanılır.
Varsayılan olarak çizgi grafik (line plot) oluşturur.
"""

print("1. TEMEL GRAFİK OLUŞTURMA")
print("-" * 70)

# Toplam kazancın siparişlere göre dağılımı
df.plot()
plt.title('Kahve Satış Verileri - Tüm Kolonlar')
plt.xlabel('Sipariş Index')
plt.ylabel('Değer')
plt.tight_layout()
plt.savefig('01_basic_plot.png')
plt.close()

# Sadece toplam kazancı görselleştir
df['Toplam_Kazanc'].plot()
plt.title('Toplam Kazanç Trendi')
plt.xlabel('Sipariş Index')
plt.ylabel('Toplam Kazanç (TL)')
plt.tight_layout()
plt.savefig('02_revenue_trend.png')
plt.close()

print("[OK] Temel grafikler olusturuldu\n")

# =============================================================================
# 2. SCATTER PLOT (Dağılım Grafiği)
# =============================================================================
"""
Scatter plot iki değişken arasındaki ilişkiyi gösterir.
kind='scatter' parametresi kullanılır.
x ve y eksenleri belirtilmelidir.
"""

print("2. SCATTER PLOT (Dağılım Grafiği)")
print("-" * 70)

# Sipariş adedi ile toplam kazanç arasındaki ilişki
df.plot(kind='scatter', x='Adet', y='Toplam_Kazanc', alpha=0.5)
plt.title('Adet vs Toplam Kazanç İlişkisi')
plt.xlabel('Sipariş Adedi')
plt.ylabel('Toplam Kazanç (TL)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('03_scatter_quantity_revenue.png')
plt.close()

# Korelasyon hesapla
correlation = df['Adet'].corr(df['Toplam_Kazanc'])
print(f"Adet ve Toplam Kazanç arasındaki korelasyon: {correlation:.6f}")

# Birim fiyat ile toplam kazanç arasındaki ilişki
df.plot(kind='scatter', x='Birim_Fiyat', y='Toplam_Kazanc',
        alpha=0.5, color='green')
plt.title('Birim Fiyat vs Toplam Kazanç İlişkisi')
plt.xlabel('Birim Fiyat (TL)')
plt.ylabel('Toplam Kazanç (TL)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('04_scatter_price_revenue.png')
plt.close()

correlation2 = df['Birim_Fiyat'].corr(df['Toplam_Kazanc'])
print(f"Birim Fiyat ve Toplam Kazanç arasındaki korelasyon: {correlation2:.6f}")
print("[OK] Scatter plot'lar olusturuldu\n")

# =============================================================================
# 3. HISTOGRAM (Frekans Dağılımı)
# =============================================================================
"""
Histogram, bir değişkenin frekans dağılımını gösterir.
kind='hist' parametresi kullanılır.
Sadece tek bir kolon gereklidir.
"""

print("3. HISTOGRAM (Frekans Dağılımı)")
print("-" * 70)

# Toplam kazancın dağılımı
df['Toplam_Kazanc'].plot(kind='hist', bins=15, edgecolor='black')
plt.title('Toplam Kazanç Dağılımı')
plt.xlabel('Toplam Kazanç (TL)')
plt.ylabel('Frekans')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('05_histogram_revenue.png')
plt.close()

# Sipariş adetlerinin dağılımı
df['Adet'].plot(kind='hist', bins=4, edgecolor='black', color='coral')
plt.title('Sipariş Adet Dağılımı')
plt.xlabel('Adet')
plt.ylabel('Frekans')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('06_histogram_quantity.png')
plt.close()

# Birim fiyat dağılımı
df['Birim_Fiyat'].plot(kind='hist', bins=10, edgecolor='black', color='purple')
plt.title('Birim Fiyat Dağılımı')
plt.xlabel('Birim Fiyat (TL)')
plt.ylabel('Frekans')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('07_histogram_unit_price.png')
plt.close()

print("[OK] Histogram'lar olusturuldu\n")

# =============================================================================
# ÖZET İSTATİSTİKLER
# =============================================================================
print("="*70)
print("ÖZET İSTATİSTİKLER")
print("="*70)
print(df[['Adet', 'Birim_Fiyat', 'Toplam_Kazanc']].describe())
print("\n[BASARILI] Tum grafikler basariyla olusturuldu ve kaydedildi!")
