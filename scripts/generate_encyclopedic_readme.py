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

![MZ-OS Hero Banner](assets/aos_hero_banner.png)

# 🏛️ MEDRESETÜ’Z-ZEHRA OPERATING SYSTEM (MZ-OS)
### *A Rigorous Multidisciplinary Knowledge Ontology for the AI Era* 🌐💎🚀

[![Versiyon](https://img.shields.io/badge/VERSION-v2025.Elite-00A9E0?style=for-the-badge&logo=target)](./)
[![Kapsam](https://img.shields.io/badge/SCOPE-385_Unique_Areas-D4AF37?style=for-the-badge&logo=rocket)](./SUMMARY.md)
[![Standard](https://img.shields.io/badge/STANDARD-7--Tier_Hierarchy-black?style=for-the-badge&logo=gitbook)](./)
[![Heritage](https://img.shields.io/badge/HERITAGE-Medresetü’z--Zehra-18453B?style=for-the-badge&logo=openai&logoColor=white)](./)

---

## 🏗️ Technical Magnitude & Methodology
**Medresetü’z-Zehra Operating System (MZ-OS)** is a high-density academic ecosystem designed to harmonize diverse knowledge streams into a single, standardized framework. Leading with **Scientific Neutrality** and **Empirical Rigor**, the system categorizes 385 unique disciplines into a unified 7-tier architecture.

> [!NOTE]
> **Methodology:** We utilize a strictly academic approach where science and engineering are the primary methods of inquiry. All curriculum structures (YÖK & MoE China) are integrated with professional objectivity.

---

</div>

## ⚙️ The Elite 7-Tier Architecture (00-06)
Every single discipline in this 385-area ontology is scaffolded into a rigorous, industry-standard hierarchy:

| Tier | Category | Objective |
| :--- | :--- | :--- |
| **`00`** | **Academic Prep** | Language proficiency and foundational orientation. |
| **`01`** | **Basic Sciences** | The theoretical and numerical bedrock of the field. |
| **`02`** | **Core Modules** | Essential technical expertise and required courses. |
| **`03`** | **Advanced App** | Elective specializations and master-level practice. |
| **`04`** | **Research & Dev** | Capstone projects, theses, and original output. |
| **`05`** | **Graduate Path** | Master & PhD level academic trajectories. |
| **`06`** | **Global Std** | Certifications and industrial professional benchmarks. |

---

## 🕌 Philosophical Foundations: The "Soul" of MZ-OS
*"Vicdanın ziyası ulûm-u diniye, aklın nuru fünun-u medeniyedir."*

While MZ-OS uses modern scientific methodologies as its **Method**, it derives its **Inspiration** and **Ethical Soul** from the Medresetü’z-Zehra vision—the harmonization of the heart and the mind.

| ✍️ Düstur | 🏛️ MZ-OS Principle |
| :--- | :--- |
| **"Knowledge without action is a shadow."** | **Active Production & Engineering** |
| **"Faith and Science must coexist for Truth."** | **Multidisciplinary Integrity** |
| **"Strive to know the Great Order of existence."** | **Empirical Inquiry & Rigor** |

---

## 📚 Encyclopedic Index (385 Disciplines)

Grouped into 20 strategic containers, each area provides a standardized path for mastery.

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
        section += "| Bölüm / Alan | Academic Focus / Mission |\n"
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

## 🛠️ Professional Instrumentation (V.2025)
- **Core Intelligence:** Gemini 2.0 / Claude 3.5 Sonnet / GPT-o1
- **Development & IDE:** Cursor / Windsurf
- **Research Engine:** Perplexity Pro Pro
- **Architecture:** 7-Tier Standardized Scaffolding

## ⚖️ License
This project is protected under the **MIT License**.

<div align="center">

**Prepared By:** Bahattin Yunus Çetin  
*Engineer & MZ-OS Architect*

[Linkedin](https://linkedin.com/in/bahattinyunuscetin) | [GitHub](https://github.com/bahattinyunus)

---
*"İlim, müminin yitik malıdır; nerede bulursa alsın."*
</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"README.md updated with Science-First balance. Total: {total_count}")

if __name__ == "__main__":
    generate_encyclopedic_readme()
