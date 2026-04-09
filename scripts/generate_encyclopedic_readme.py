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
### *Medrese-i Modern: Küresel Bilim ve Kadim Mirasın Sinerjisi* 🌐💎🌙🚀

[![Kurucu](https://img.shields.io/badge/KURUCU-Bahattin%20Yunus-black?style=for-the-badge&logo=github&logoColor=gold)](https://github.com/bahattinyunus)
[![Versiyon](https://img.shields.io/badge/VERSİYON-v2025.Elite-00A9E0?style=for-the-badge&logo=target)](./)
[![Kapsam](https://img.shields.io/badge/KAPSAM-385_Bölüm-D4AF37?style=for-the-badge&logo=rocket)](./SUMMARY.md)
[![Düşünce](https://img.shields.io/badge/DÜŞÜNCE-İlim--Amel--İhlas-18453B?style=for-the-badge&logo=openai&logoColor=white)](./)

---

## 📜 AOS Manifestosu: Hakikat Arayışı ve Teknik Üstünlük

> **"İlim, Çin'de de olsa ona talip olun."**

AOS, modern bilimsel tarafsızlık ile kadim medeniyet mirasımızın yüksek disiplinini birleştiren bir "Bilgi Kalesi"dir. Bu sistem; Selçuklu'nun geometrik hassasiyetini, Osmanlı'nın nizam idealini ve modern mühendisliğin otonom gücünü tek bir potada eritir. **Bilim bir keşif süreci, mühendislik ise bu keşfi insanlığın hizmetine sunma sanatıdır.**

---

</div>

## 🕌 Miras ve Vizyon: El-Cezeri'den Geleceğe

AOS ekosistemi, hakikati arayan ve teknik mükemmelliği hedefleyen bir zihin yapısı üzerine inşa edilmiştir:

| ✍️ Düstur | 👤 Kaynak | 🏛️ AOS Prensibi |
| :--- | :--- | :--- |
| **"Eyleme dökülmeyen ilim, yerinde sayan bir gölge gibidir."** | *El-Cezeri (Sibernetiğin Babası)* | **Aktif Mühendislik & Üretim** |
| **"Hiç bilenlerle bilmeyenler bir olur mu?"** | *Zümer Suresi, 9* | **Entelektüel Üstünlük** |
| **"Amacı olmayan ilim, ruhsuz bir bedendir."** | *İbn Sina (Avicenna)* | **Hikmet Odaklı Tasarım** |
| **"Stratejisi olmayan güç, kendi kendini yok eder."** | *Fatih Sultan Mehmet* | **Stratejik Seferberlik** |
| **"Gökleri ve yeri araştırın; o büyük nizamı keşfedin."** | *Kadim İlim Geleneği* | **Evrensel Merak & Bilim** |

---

<div align="center">

## ⚙️ Çelik Çerçeve: Ultimate 7-Tier Mimari
*"Nizam, kaosun en büyük galibidir."*

Her branş, rastgele bir yığın değil; **7 katmanlı profesyonel bir nizam (Systemum)** üzerine kuruludur:

**`00`** Hazırlık **`01`** Teori **`02`** Çekirdek **`03`** Uzmanlık **`04`** Üretim **`05`** Akademi **`06`** Standart

---

</div>

## 💎 Neden Bu Sistem?
-   **Evrensel Kapsayıcılık:** Kuantum fiziğinden İslam Hukukuna, BCI mühendisliğinden Osmanlı mimarisine kadar 385 alan.
-   **Stratejik Entegrasyon:** Çin'in teknoloji vizyonu ve YÖK standartlarının, yerli ve milli bir stratejiyle harmanlanması.
-   **Karakter İnşası:** Teknik bilgiyle beraber Stoacı dayanıklılık ve İslam ahlakının (Meta-Yetkinlikler) birleşimi.

---

## 📚 Ansiklopedik Bölüm Dizini (385 Alan)

AOS ekosistemi, bilginin bir "Hazine" (Kenz) olarak korunduğu 385 benzersiz odadan oluşur.

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

## 🛠️ Profesyonel Enstrümantasyon (V.2025)
> "Kılıç, elin uzantısı; kalem ise aklın dilidir."

- **Core Intelligence:** Gemini 2.0 / Claude 3.5 Sonnet / GPT-o1
- **Development & IDE:** Cursor / Windsurf
- **Research Engine:** Perplexity Pro
- **Architecture:** 7-Tier Standardized Scaffolding

---

## ⚖️ Lisans
Bu proje **MIT Lisansı** ile korunmaktadır.

<div align="center">

**Prepared By:** Bahattin Yunus Çetin  
*Engineer & Academic System Architect*

[Linkedin](https://linkedin.com/in/bahattinyunuscetin) | [GitHub](https://github.com/bahattinyunus)

---
*"İlim, müminin yitik malıdır; nerede bulursa alsın."*  
**Hayırlı İlimler Dileğiyle.**
</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"README.md updated with 385 areas and Islamic/Heritage depth. Total: {total_count}")

if __name__ == "__main__":
    generate_encyclopedic_readme()
