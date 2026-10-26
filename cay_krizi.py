#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Fincanı Varoluşsal Kriz Simülatörü
Bu kod gerçekten çalışır. Fincanlar gerçekten kriz geçirir.
"""

import random
import time

# Gizli siyasi mesaj (şifreli, sadece bilen bilir)
# Base64: "Özgürlük kötü değildir, ama çay fincanları daha özgürdür." 
# Decode etmek istersen: import base64; base64.b64decode(b'...')
GIZLI = "w5Z6Z8O8cmzDvGsga8O2dMO8IGRlZ2lsZGlyLCBhbWEgw6dheSBmaW5jYW5sYXJ1IGRhaGEgw7Z6Z8O8cmTDvHIu"

def kriz_uret():
    baslangic = [
        "Bu çay fincanı aniden fark etti ki...",
        "Fincanın içindeki boşluk fısıldadı:",
        "Kulpu kırık bir fincan derin düşüncelere daldı:",
        "Sıcaklığını kaybeden fincan sordu:"
    ]
    
    dusunceler = [
        "Ben sadece bir kab mıyım, yoksa içindeki çayın anlamı mıyım?",
        "Çay bitince ben de biter miyim? Yoksa boşluk da bir varlık mıdır?",
        "İnsanlar beni yıkarken neden gülümsüyor? Acımı anlamıyorlar mı?",
        "Bir gün masadan düşüp kırılırsam, bu özgürlük mü yoksa felaket mi?",
        "Çay demlenirken ben sadece bekliyorum. Beklemek var olmak mıdır?",
        "Diğer fincanlar bana 'sen de boşsun' dedi. Haklılar mı?",
        "Benim içim çayla doluyken anlamlıyım. Boşken? Sadece seramik."
    ]
    
    sonlar = [
        "Sonra sessizce kırıldı. Ya da kırılmadı. Kimse bilmiyor.",
        "Ve o an anladı: çay fincanı olmak yeterlidir.",
        "Kriz bitti. Yeni çay geldi. Döngü devam etti.",
        "Fincan gülümsedi. Kulpuyla."
    ]
    
    print("\n" + "="*50)
    print("🫖 ÇAY FINCANI VAROLUŞSAL KRİZ BAŞLADI")
    print("="*50)
    time.sleep(1)
    
    print(random.choice(baslangic))
    time.sleep(1.5)
    print(f"\n\"{random.choice(dusunceler)}\"")
    time.sleep(2)
    print(f"\n{random.choice(sonlar)}")
    print("="*50)
    print("Kriz tamamlandı. Çay içmeye devam edin. Ya da etmeyin.\n")

if __name__ == "__main__":
    print("Çay Fincanı Varoluşsal Kriz Simülatörü v1.0")
    print("Bu program çay fincanlarının iç dünyasını simüle eder.\n")
    kriz_uret()
    # Gizli şeyi kullanmıyoruz bile. Sadece orada duruyor.
    # print(GIZLI)  # Açarsan anlarsın, açmazsan da olur.