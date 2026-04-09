import os

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

CONTAINERS = {
    'meta_muhendislik': '🛠️ Mühendislik Bilimleri',
    'mimarlik_ve_tasarim': '🏛️ Mimarlık ve Tasarım',
    'guzel_sanatlar': '🖼️ Güzel Sanatlar',
    'saglik': '🩺 Sağlık Bilimleri',
    'ogretmenlik': '🎓 Eğitim ve Öğretmenlik',
    'spor_bilimleri': '🏅 Spor Bilimleri',
    'sosyal_ve_beseri_bilimler': '⚖️ Sosyal ve Beşeri Bilimler',
    'temel_bilimler': '🧪 Temel Bilimler',
    'edebiyat_ve_diller': '📚 Edebiyat ve Diller',
    'iletisim': '📡 İletişim Bilimleri',
    'turizm_ve_gastronomi': '🏨 Turizm ve Gastronomi',
    'tarim_ve_ziraat_bilimleri': '🌱 Tarım ve Ziraat Bilimleri',
    'askeri_bilimler_ve_savunma_teknolojileri': '⚔️ Askeri Bilimler ve Savunma',
    'hukuk_bilimi': '⚖️ Hukuk',
    'ilahiyat_ve_din': '🕌 İlahiyat ve Din',
    'on_lisans_programlari': '📋 Ön Lisans Programları',
    'ozel_arastirma_alanlari': '🔬 Özel Araştırma Alanları',
    'kariyer_ve_sertifikasyonlar': '🚀 Kariyer ve Sertifikasyonlar',
    'meta_yetkinlikler_ve_gelisim': '🧠 Meta-Yetkinlikler ve Gelişim',
    'genel': '📂 Genel ve Ortak Alanlar'
}

SPECIAL_DESCRIPTIONS = {
    # Engineering
    'elektrik_elektronik_muhendisligi': 'Enerji üretimi, iletimi ve elektronik devre tasarımı üzerine odaklanan temel mühendislik branşı.',
    'beyin_bilgisayar_arayuzu_bci_muhendisligi': 'Nöral sinyallerin dijital sistemlere aktarımı ve insan-makine etkileşimi üzerine ileri araştırma.',
    'yapay_zeka_ve_verii_muhendisligi': 'Büyük veri analizi, makine öğrenmesi ve otonom sistemlerin algoritma tasarımı.',
    'siber_guvenlik_muhendisligi': 'Dijital varlıkların korunması, sızma testleri ve güvenli sistem mimarileri geliştirme.',
    'yuksek_guclu_yariiletken_bilimi_ve_muhendisligi': 'Yeni nesil enerji elektroniği ve yarı iletken komponent teknolojileri üretimi.',
    'dusuk_irtifa_teknolojisi_ve_iha': 'Dronelar ve alçak irtifa hava araçlarının aerodinamik ve sistem tasarımı.',
    
    # China Export Specials
    'geleneksel_cin_tibbi': 'Binlerce yıllık kadim Çin tıp öğretileri ve bitkisel tedavi metodolojileri.',
    'kahve_bilimi_ve_muhendisligi': 'Kahve bitkisinin üretiminden işleme teknolojilerine ve kimyasal analizine kadar tüm süreçler.',
    'futbol_bilimi': 'Futbolun teknik, taktik, biyomekanik ve yönetimsel boyutlarının akademik analizi.',
    'tutun_bilimi': 'Tütün bitkisinin yetiştirilmesi, endüstriyel işlenmesi ve kalite kontrol süreçleri.',
    'ipek_muhendisligi_ve_serikultur': 'İpek böcekçiliği ve tekstil mühendisliğinin ipek üretimi özelindeki kesişimi.',
    
    # Meta Skills
    'monk_mode_disiplin_sistemi': 'Yüksek odaklanma, dijital detoks ve kişisel hedeflere tam adanmışlık disiplini.',
    'sun_tzu_stratejik_dunce': 'Antik savaş stratejilerinin modern iş ve yaşam yönetimine uygulanması.',
    'stoisizm_ve_mental_dayaniklilik': 'Stoacı fıkırlerin modern stres yönetimi ve sarsılmaz bir zihin yapısı için uygulanması.',
    
    # Defense
    'komuta_kontrol_ve_strateji': 'Askeri operasyonların yönetimi, karar destek sistemleri ve stratejik planlama.',
    'siber_savunma_ve_elektronik_harp': 'Dijital cephede savunma ve radar/sinyal sistemlerinde üstünlük sağlama yöntemleri.',
}

def get_desc(folder, container):
    if folder in SPECIAL_DESCRIPTIONS:
        return SPECIAL_DESCRIPTIONS[folder]
    
    # Fallback logic
    t = folder.lower()
    if 'muhendis' in t or 'engineering' in t:
        return 'Modern mühendislik prensipleriyle ilgili sistemin tasarımı, analizi ve optimizasyonu.'
    if 'dili' in t or 'edebiyati' in t:
        return 'İlgili dilin dilbilgisi yapısı, edebiyat tarihi ve kültürel bağlamının akademik incelenmesi.'
    if 'onlisans' in t or container == 'on_lisans_programlari':
        return 'Belirli bir mesleğe yönelik uygulamalı teknik beceriler ve operasyonel yetkinlikler eğitimi.'
    if 'teknolojisi' in t:
        return 'Modern teknolojik araçların ve süreçlerin ilgili alan özelinde uygulanması ve yönetimi.'
    if 'yonetimi' in t:
        return 'Süreçlerin, kaynakların ve organizasyonların stratejik ve operasyonel olarak yönetilmesi.'
    
    return f"{folder.replace('_', ' ').capitalize()} alanında teorik ve pratik uzmanlık çalışmaları."

def generate_encyclopedic_readme():
    header = """<div align="center">

![AOS Hero Banner](assets/aos_hero_banner.png)

# 🏛️ AKADEMİK İŞLETİM SİSTEMİ (AOS)
### *Dünyanın En Kapsamlı Bilgi Ontolojisi — 385+ Uzmanlık Alanı* 🌐💎🚀

[![Kurucu](https://img.shields.io/badge/KURUCU-Bahattin%20Yunus-black?style=for-the-badge&logo=github&logoColor=gold)](https://github.com/bahattinyunus)
[![Versiyon](https://img.shields.io/badge/VERSİYON-v2025.Ultimate-B81D24?style=for-the-badge&logo=target)](./)
[![Kapsam](https://img.shields.io/badge/KAPSAM-385_Bölüm-0078D4?style=for-the-badge&logo=rocket)](./SUMMARY.md)
[![Mimari](https://img.shields.io/badge/MİMARİ-7--Tier_Elite-FFD700?style=for-the-badge&logo=openai&logoColor=black)](./)

---

> **"Bilgi, ancak bir sistem içinde sınıflandırıldığında bir silaha dönüşür. AOS; YÖK ve global stratejik müfredatları (China MoE) birleştiren, 385+ akademik branşı 7 katmanlı profesyonel hiyerarşide sunan bir 'Entelektüel İşletim Sistemi'dir."** 🚀🦾

---

</div>

## 🌌 Mimari: Ultimate 7-Tier (00-06) Scaffolding
Sistemdeki her bir bölüm, hazırlık eğitiminden profesyonel sertifikasyona kadar 7 temel katmanda standardize edilmiştir:

1.  **`00 — Akademik Hazırlık ve Dil`**: Dil yeterliliği ve oryantasyon.
2.  **`01 — Temel Bilimler ve Giriş`**: Bölümün teorik temelleri.
3.  **`02 — Alan Dersleri`**: Zorunlu ana branş dersleri.
4.  **`03 — Seçmeli & İleri Uygulama`**: Uzmanlaşma ve derinleşme.
5.  **`04 — Araştırma ve Bitirme`**: Tez, bitirme projeleri ve akademik çıktılar.
6.  **`05 — Lisansüstü ve Akademik Kariyer`**: Yüksek Lisans ve Doktora seviyesi.
7.  **`06 — Sertifikasyon ve Endüstriyel Standartlar`**: Küresel mesleki yeterlilikler.

---

## 📚 Ansiklopedik Bölüm Dizini (385 Alan)

Kategorilere tıklayarak içindeki bölümleri ve kısa açıklamalarını görebilirsiniz.

"""

    body = ""
    total_count = 0
    
    for folder, title in CONTAINERS.items():
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        depts = sorted([d for d in os.listdir(container_path) if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')])
        if not depts:
            continue
            
        section = f"<details>\n<summary><b>{title} ({len(depts)} Alan)</b></summary>\n<br>\n\n"
        section += "| Bölüm / Alan | Akademik Odak / Misyon |\n"
        section += "| :--- | :--- |\n"
        
        for d in depts:
            dept_name = d.replace('_', ' ').title()
            link = f"[{dept_name}]({folder}/{d}/)"
            desc = get_desc(d, folder)
            section += f"| {link} | {desc} |\n"
            total_count += 1
            
        section += "\n"
        section += "</details>\n\n"
        body += section

    footer = f"""
---

## 🧬 Küresel Stratejik Entegrasyon
Bu sistem sadece klasik bölümleri değil, dünyanın yükselen güçlerinin en stratejik branşlarını da içerir. Tüm detaylı yol haritaları ve dökümanlar ilgili klasörlerin altındadır.

## 🛠️ Solopreneur AI Araç Seti (V.2025)
- **Yazılım:** Cursor / Windsurf
- **Analiz:** Claude 3.5 Sonnet / Gemini 2.0
- **Araştırma:** Perplexity AI
- **Otomasyon:** n8n / Make.com

---

## ⚖️ Lisans
Bu proje **MIT Lisansı** ile korunmaktadır.

<div align="center">

**Hazırlayan:** Bahattin Yunus Çetin  
*Mühendis & Araştırmacı*

[Linkedin](https://linkedin.com/in/bahattinyunuscetin) | [GitHub](https://github.com/bahattinyunus)

</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"README.md updated with {total_count} areas and descriptions.")

if __name__ == "__main__":
    generate_encyclopedic_readme()
