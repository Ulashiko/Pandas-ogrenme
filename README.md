# Pandas Ogrenme Notlari

Python Pandas kutuphanesini ogrenirken olusturulan notlar, ornek kodlar ve veri analizi alistirmalari.

## Proje Yapisi

```text
pd-learn/
|-- (0)pd-start/
|   `-- main.py
|-- (1)pd-series/
|   `-- main.py
|-- (2)pd-dataframe/
|   |-- data.csv
|   `-- main.py
|-- (3)pd-loc_iloc/
|   `-- main.py
|-- (4)pd-json-load/
|   |-- calisanlar_export.json
|   |-- calisanlar_table.json
|   |-- main.py
|   |-- README.md
|   `-- veriler.json
|-- (5)pd-analyzing-data/
|   |-- data.csv
|   |-- main.py
|   `-- README.md
|-- (6)pd-cleaning-data/
|   |-- f1_data.csv
|   |-- README.md
|   |-- (6)(1)pd-cleaning-empty-cells/
|   |   |-- main.py
|   |   `-- README.md
|   |-- (6)(2)pd-cleaning-wrong-format/
|   |   |-- main.py
|   |   `-- README.md
|   |-- (6)(3)pd-cleaning-wrong-data/
|   |   |-- main.py
|   |   `-- README.md
|   `-- (6)(4)pd-cleaning-duplicates/
|       |-- main.py
|       `-- README.md
|-- (7)pd-correlations/
|   |-- main.py
|   |-- README.md
|   `-- workout_data.csv
|-- (8)pd-plotting/
|   |-- main.py
|   `-- README.md
|-- kahve_satis_verisi.csv
`-- README.md
```

## Konular

1. Baslangic: temel pandas kurulumu ve ilk script yapisi
2. Series: liste ile `pd.Series` olusturma ve index mantigi
3. DataFrame: sozlukten `pd.DataFrame` olusturma, CSV okuma
4. Loc/Iloc: satir ve sutun secimi
5. JSON Load: JSON veri okuma ve donusturme ornekleri
6. Analyzing Data: ozet istatistikler ve veri kesfi
7. Cleaning Data:
	- Bos hucreleri temizleme
	- Yanlis format duzeltme
	- Hatali veri duzeltme
	- Duplicate kayit temizleme
8. Correlations: kolonlar arasi iliski analizi
9. Plotting: plot(), scatter, histogram ile veri gorsellestirme

## Gereksinimler

```text
python >= 3.12
pandas
matplotlib
```

## Kurulum

```bash
pip install pandas matplotlib
```

## Calistirma

Asagidaki komutlarla istedigin bolumu calistirabilirsin:

```bash
python "(0)pd-start/main.py"
python "(1)pd-series/main.py"
python "(2)pd-dataframe/main.py"
python "(3)pd-loc_iloc/main.py"
python "(4)pd-json-load/main.py"
python "(5)pd-analyzing-data/main.py"
python "(6)pd-cleaning-data/(6)(1)pd-cleaning-empty-cells/main.py"
python "(6)pd-cleaning-data/(6)(2)pd-cleaning-wrong-format/main.py"
python "(6)pd-cleaning-data/(6)(3)pd-cleaning-wrong-data/main.py"
python "(6)pd-cleaning-data/(6)(4)pd-cleaning-duplicates/main.py"
python "(7)pd-correlations/main.py"
python "(8)pd-plotting/main.py"
```

## Kaynaklar

- [Pandas Resmi Dokumantasyonu](https://pandas.pydata.org/docs/)
- [W3Schools Pandas Tutorial](https://www.w3schools.com/python/pandas/)
