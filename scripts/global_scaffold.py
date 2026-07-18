import os
import shutil

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"
TEMPLATE_FILE = os.path.join(ROOT_DIR, 'templates', 'COURSE_TEMPLATE.md')

# These are the standard subdirectories (Expanded to 00-06)
SUBDIR_DEFS = {
    "00_Akademik_Hazirlik_ve_Dil": {
        "label": "00 — Akademik Hazırlık ve Dil",
        "desc": "Hazırlık sınıfı müfredatı, yabancı dil yeterlilik çalışmaları ve akademik oryantasyon.",
    },
    "01_Temel_Bilimler_ve_Giris": {
        "label": "01 — Temel Bilimler ve Giriş",
        "desc": "Bölüme giriş niteliğindeki temel ders notları, genel kavramlar ve başlangıç kaynakları.",
    },
    "02_Alan_Dersleri": {
        "label": "02 — Alan Dersleri",
        "desc": "Bölümün özgül ve zorunlu alan derslerine ait notlar, ödevler ve kaynaklar.",
    },
    "03_Secmeli_ve_Ileri_Uygulama": {
        "label": "03 — Seçmeli & İleri Uygulama",
        "desc": "Seçmeli dersler, derinlemesine uygulama projeleri ve uzmanlaşma çalışmaları.",
    },
    "04_Arastirma_ve_Bitirme": {
        "label": "04 — Araştırma ve Bitirme",
        "desc": "Bitirme projeleri, staj raporları, seminer çalışmaları ve akademik araştırma notları.",
    },
    "05_Lisansustu_ve_Akademik_Kariyer": {
        "label": "05 — Lisansüstü ve Akademik Kariyer",
        "desc": "Yüksek lisans ve doktora çalışmaları, akademik yayın notları ve tez hazırlık dökümanları.",
    },
    "06_Sertifikasyon_ve_Endustriyel_Standartlar": {
        "label": "06 — Sertifikasyon ve Endüstriyel Standartlar",
        "desc": "Mesleki yeterlilik sınavları, uluslararası sertifikalar ve endüstri standartları dökümantasyonu.",
    },
}

# All current container folders
CONTAINERS = [
    'edebiyat_ve_diller',
    'hukuk_bilimi',
    'ilahiyat_ve_din',
    'iletisim',
    'meta_muhendislik',
    'mimarlik_ve_tasarim',
    'ogretmenlik',
    'saglik',
    'sosyal_ve_beseri_bilimler',
    'temel_bilimler',
    'turizm_ve_gastronomi',
    'ozel_arastirma_alanlari',
    'guzel_sanatlar',
    'spor_bilimleri',
    'on_lisans_programlari',
    'kariyer_ve_sertifikasyonlar',
    'meta_yetkinlikler_ve_gelisim',
    'tarim_ve_ziraat_bilimleri',
    'askeri_bilimler_ve_savunma_teknolojileri',
    'genel',
    'epistemik'
]


def get_dept_readme_content(dept_name):
    title = dept_name.replace('_', ' ').title()
    return f"""# {title}

Bu klasör **{title}** alanına ait akademik notlar, araştırmalar, lisansüstü çalışmalar ve sektörel standartlar içindir.

---

## 📂 Çekirdek Ders Ağacı
Akademik ve profesyonel sistem entegrasyonu kapsamında bu bölüm için önerilen ve standartlaştırılmış klasör yapısı:

- [00 — Akademik Hazırlık ve Dil](00_Akademik_Hazirlik_ve_Dil/)
- [01 — Temel Bilimler ve Seminerler](01_Temel_Bilimler_ve_Giris/)
- [02 — Alan Dersleri ve Pratik](02_Alan_Dersleri/)
- [03 — Seçmeli, İleri ve Uzmanlık Dersleri](03_Secmeli_ve_Ileri_Uygulama/)
- [04 — Bitirme, Araştırma ve Çapraz Projeler](04_Arastirma_ve_Bitirme/)
- [05 — Lisansüstü ve Akademik Kariyer](05_Lisansustu_ve_Akademik_Kariyer/)
- [06 — Sertifikasyon ve Endüstriyel Standartlar](06_Sertifikasyon_ve_Endustriyel_Standartlar/)

> [!TIP]
> Yeni bir ders veya çalışma eklerken ana dizindeki `DERS_SABLONU.md` dosyasını kopyalayarak ilgili alt klasörün içine koyabilir ve kolayca kendi dökümantasyonunuzu oluşturabilirsiniz!
"""

def get_subdir_readme_content(dept_name, sub_key):
    dept_title = dept_name.replace('_', ' ').title()
    sub = SUBDIR_DEFS[sub_key]
    return f"""# 📂 {sub['label']} — {dept_title}

## 📖 Açıklama
{sub['desc']}

---

## 📝 Bu Klasöre Nasıl Katkı Yapılır?
1. `DERS_SABLONU.md` (üst dizindeki) dosyasını bu klasöre kopyala
2. Dosyayı `DERS_ADI.md` (veya ilgili sertifika/tez adı) olarak yeniden adlandır
3. İçini içeriklerle doldur
4. Pull Request aç veya doğrudan push et

> [!NOTE]
> Bu klasör **{dept_title}** alanının **{sub['label']}** katmanına aittir.
"""

def scaffold_department(dept_path, dept_name):
    # 1. Ensure Department README (Overwrite or append if missing new tiers)
    readme_path = os.path.join(dept_path, 'README.md')
    needs_rewrite = False
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if "05 — Lisansüstü" not in content and "05_Lisansustu_ve_Akademik_Kariyer" not in content:
                needs_rewrite = True
    else:
        content = ""
        needs_rewrite = True
        
    if needs_rewrite:
        if len(content.strip()) > 50:
            tree_content = f"""
---

## 📂 Çekirdek Ders Ağacı
Akademik ve profesyonel sistem entegrasyonu kapsamında bu bölüm için önerilen ve standartlaştırılmış klasör yapısı:

- [00 — Akademik Hazırlık ve Dil](00_Akademik_Hazirlik_ve_Dil/)
- [01 — Temel Bilimler ve Seminerler](01_Temel_Bilimler_ve_Giris/)
- [02 — Alan Dersleri ve Pratik](02_Alan_Dersleri/)
- [03 — Seçmeli, İleri ve Uzmanlık Dersleri](03_Secmeli_ve_Ileri_Uygulama/)
- [04 — Bitirme, Araştırma ve Çapraz Projeler](04_Arastirma_ve_Bitirme/)
- [05 — Lisansüstü ve Akademik Kariyer](05_Lisansustu_ve_Akademik_Kariyer/)
- [06 — Sertifikasyon ve Endüstriyel Standartlar](06_Sertifikasyon_ve_Endustriyel_Standartlar/)

> [!TIP]
> Yeni bir ders veya çalışma eklerken ana dizindeki `DERS_SABLONU.md` dosyasını kopyalayarak ilgili alt klasörün içine koyabilir ve kolayca kendi dökümantasyonunuzu oluşturabilirsiniz!
"""
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content.rstrip() + "\n\n" + tree_content.lstrip())
        else:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(get_dept_readme_content(dept_name))

    
    # 2. Copy DERS_SABLONU.md if available
    if os.path.exists(TEMPLATE_FILE):
        dest_template = os.path.join(dept_path, 'DERS_SABLONU.md')
        if not os.path.exists(dest_template):
            shutil.copy2(TEMPLATE_FILE, dest_template)
    
    # 3. Create Subdirs and their READMEs
    for sub_key in SUBDIR_DEFS.keys():
        sub_path = os.path.join(dept_path, sub_key)
        os.makedirs(sub_path, exist_ok=True)
        sub_readme = os.path.join(sub_path, 'README.md')
        if not os.path.exists(sub_readme):
            with open(sub_readme, 'w', encoding='utf-8') as f:
                f.write(get_subdir_readme_content(dept_name, sub_key))

def main():
    count = 0
    for container in CONTAINERS:
        container_path = os.path.join(ROOT_DIR, container)
        if not os.path.exists(container_path):
            continue
            
        print(f"Processing container: {container}")
        for item in os.listdir(container_path):
            item_path = os.path.join(container_path, item)
            if os.path.isdir(item_path) and not item.startswith('.') and item != 'README.md':
                scaffold_department(item_path, item)
                count += 1
                if count % 10 == 0:
                    print(f"  Processed {count} departments/areas...")
    
    print(f"\nDone! Scaffolded/Upgraded {count} departments in total with the Elite 7-tier (00-06) structure.")

if __name__ == "__main__":
    main()
