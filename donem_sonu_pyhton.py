# =====================================================
# PYTHON PROGRAMLAMA DÖNEM ÖDEVİ
# AKILLI MÜŞTERİ YÖNETİM VE ANALİZ SİSTEMİ
# Ortam: Google Colab
# =====================================================

# -----------------------------------------------------
# KÜTÜPHANELER
# -----------------------------------------------------

import random          # Random Kütüphanesi Kullanımı
import math            # Math Kütüphanesi Kullanımı
import datetime        # Datetime Kütüphanesi Kullanımı

# =====================================================
# 1. KISIM
# Veri Yapıları ve Temel Mantık
# =====================================================

# -----------------------------------------------------
# Değişkenler ve Veri Tipleri
# -----------------------------------------------------

ad_soyad = "Ahmet Yılmaz"        # String Kullanımı
aylik_ucret = 650.75             # Float Kullanımı
sadakat_ayi = 30                 # Integer Kullanımı
aktif_mi = True                  # Boolean Kullanımı

# -----------------------------------------------------
# Liste Kullanımı
# -----------------------------------------------------

hizmetler = [
    "İnternet",
    "TV+",
    "Mobil Hat",
    "Bulut Depolama",
    "Müşteri Destek Paketi"
]   # Liste Kullanımı

# -----------------------------------------------------
# Dictionary Kullanımı
# -----------------------------------------------------

musteri = {
    "ad_soyad": ad_soyad,
    "aylik_ucret": aylik_ucret,
    "sadakat_ayi": sadakat_ayi,
    "aktif_mi": aktif_mi,
    "hizmetler": hizmetler
}   # Dictionary Kullanımı

# -----------------------------------------------------
# If-Else Kullanımı
# -----------------------------------------------------

print("===== 1. KISIM =====")

if aylik_ucret > 500 or sadakat_ayi > 24:   # Koşullu İfade Kullanımı
    print("VIP Müşteri: İndirim Tanımla")
else:
    print("Standart Müşteri")

# -----------------------------------------------------
# String Operasyonları
# -----------------------------------------------------

buyuk_harf_isim = ad_soyad.upper()   # String Metodu Kullanımı

print("Büyük Harfli İsim:", buyuk_harf_isim)

# -----------------------------------------------------
# Random Customer ID Oluşturma
# -----------------------------------------------------

rastgele_sayi = random.randint(1000, 9999)   # Random Kullanımı

customerID = "IST-2026-" + str(rastgele_sayi)

print("Customer ID:", customerID)

# -----------------------------------------------------
# Müşteri Bilgilerini Yazdırma
# -----------------------------------------------------

print("\nMüşteri Bilgileri:")

print(musteri)

# =====================================================
# 2. KISIM
# Fonksiyonlar, Döngüler ve Kütüphaneler
# =====================================================

# -----------------------------------------------------
# Müşteri Listesi Oluşturma
# -----------------------------------------------------

musteriler_listesi = [

    {
        "ad": "Ahmet",
        "aylik_ucret": 450,
        "sadakat_ayi": 10,
        "aktif_mi": True
    },

    {
        "ad": "Ayşe",
        "aylik_ucret": 700,
        "sadakat_ayi": 40,
        "aktif_mi": True
    },

    {
        "ad": "Mehmet",
        "aylik_ucret": 300,
        "sadakat_ayi": 5,
        "aktif_mi": False
    },

    {
        "ad": "Zeynep",
        "aylik_ucret": 900,
        "sadakat_ayi": 50,
        "aktif_mi": True
    },

    {
        "ad": "Can",
        "aylik_ucret": 250,
        "sadakat_ayi": 3,
        "aktif_mi": False
    }

]   # Liste ve Dictionary Kullanımı

# -----------------------------------------------------
# Fonksiyon Tanımlama
# -----------------------------------------------------

def tutar_hesapla(aylik_ucret):   # Fonksiyon Kullanımı

    kdvli_tutar = aylik_ucret * 1.20   # Matematiksel İşlem

    return kdvli_tutar   # Return Kullanımı

# -----------------------------------------------------
# Döngü Kullanımı
# -----------------------------------------------------

print("\n===== 2. KISIM =====")

print("\n===== FATURA BİLGİLERİ =====")

for musteri in musteriler_listesi:   # For Döngüsü Kullanımı

    toplam_tutar = tutar_hesapla(musteri["aylik_ucret"])   # Fonksiyon Çağırma

    yuvarlanmis_tutar = math.ceil(toplam_tutar)   # Math Kütüphanesi Kullanımı

    print("\nMüşteri Adı:", musteri["ad"])

    print("KDV Dahil Tutar:", yuvarlanmis_tutar, "TL")

    # -------------------------------------------------
    # Churn Risk Analizi
    # -------------------------------------------------

    if musteri["sadakat_ayi"] < 12 or musteri["aktif_mi"] == False:
        print("Churn Riski Var")
    else:
        print("Müşteri Aktif")

# -----------------------------------------------------
# Tarih Bilgisi
# -----------------------------------------------------

bugun = datetime.datetime.now()   # Datetime Kullanımı

print("\nFatura Tarihi:", bugun.strftime("%d/%m/%Y"))

# -----------------------------------------------------
# Set Kullanımı
# -----------------------------------------------------

tum_hizmetler = [

    "İnternet",
    "TV+",
    "Mobil Hat",
    "İnternet",
    "Bulut Depolama",
    "TV+",
    "Mobil Hat"

]   # Tekrarlı Liste

benzersiz_hizmetler = set(tum_hizmetler)   # Set Kullanımı

print("\nBenzersiz Hizmetler:")

print(benzersiz_hizmetler)

# =====================================================
# KRİTİK SORU CEVAPLARI
# =====================================================

print("\n===== KRİTİK SORU 1 =====")

print("""
Müşteri bilgilerini sözlük (dictionary) içinde saklamayı tercih ettik.
Çünkü sözlük yapısında verilere anahtar isimleriyle kolayca erişebiliriz.
Örneğin 'ad_soyad' veya 'aylik_ucret' gibi alanlara doğrudan ulaşılabilir.

Liste kullanılsaydı verilere sadece sıra numarasıyla erişmek gerekecekti.
Bu durum kodun okunabilirliğini azaltırdı.
Dictionary yapısı daha düzenli ve anlaşılırdır.
""")

print("===== KRİTİK SORU 2 =====")

print("""
For döngüsü ile müşteri listesi tek tek gezildi.
Sadakat süresi 12 aydan az olan veya aktif olmayan müşteriler
'Churn Riski Var' olarak işaretlendi.

Çünkü kısa süreli veya pasif müşterilerin şirketten ayrılma ihtimali daha yüksektir.
Bu analiz sayesinde riskli müşteriler önceden tespit edilebilir.
""")
