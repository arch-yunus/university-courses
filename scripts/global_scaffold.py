import os
import shutil

# Portable Root Path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# These are the standard subdirectories (00-06)
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
    'epistemik',
    'meta_muhendislik',
    'mimarlik_ve_tasarim',
    'guzel_sanatlar',
    'saglik',
    'ogretmenlik',
    'spor_bilimleri',
    'sosyal_ve_beseri_bilimler',
    'temel_bilimler',
    'edebiyat_ve_diller',
    'iletisim',
    'turizm_ve_gastronomi',
    'tarim_ve_ziraat_bilimleri',
    'hukuk_bilimi',
    'ilahiyat_ve_din',
    'on_lisans_programlari',
    'ozel_arastirma_alanlari',
    'kariyer_ve_sertifikasyonlar',
    'meta_yetkinlikler_ve_gelisim',
    'askeri_bilimler_ve_savunma_teknolojileri',
    'genel'
]

def format_title(name):
    title = name.replace('_', ' ').title()
    title = (title
             .replace('Muhendisligi', 'Mühendisliği')
             .replace('Insaat', 'İnşaat')
             .replace('Isletme', 'İşletme')
             .replace('Ulasim', 'Ulaşım')
             .replace('Bilisim', 'Bilişim')
             .replace('Sagligi', 'Sağlığı')
             .replace('Egitimi', 'Eğitimi')
             .replace('Ogretmenligi', 'Öğretmenliği')
             .replace('Programciligi', 'Programcılığı')
             .replace('Iktisat', 'İktisat')
             .replace('Iletisim', 'İletişim'))
    return title

def get_dept_readme_content(dept_name):
    title = format_title(dept_name)
    return f"""# {title}

Bu klasör **{title}** alanına ait akademik notlar, araştırmalar, lisansüstü çalışmalar ve sektörel standartlar içindir.

---

## 📂 Çekirdek Ders Ağacı
Akademik ve profesyonel sistem entegrasyonu kapsamında bu bölüm için standartlaştırılmış klasör yapısı:

- [00 — Akademik Hazırlık ve Dil](00_Akademik_Hazirlik_ve_Dil/)
- [01 — Temel Bilimler ve Seminerler](01_Temel_Bilimler_ve_Giris/)
- [02 — Alan Dersleri ve Pratik](02_Alan_Dersleri/)
- [03 — Seçmeli, İleri ve Uzmanlık Dersleri](03_Secmeli_ve_Ileri_Uygulama/)
- [04 — Bitirme, Araştırma ve Çapraz Projeler](04_Arastirma_ve_Bitirme/)
- [05 — Lisansüstü ve Akademik Kariyer](05_Lisansustu_ve_Akademik_Kariyer/)
- [06 — Sertifikasyon ve Endüstriyel Standartlar](06_Sertifikasyon_ve_Endustriyel_Standartlar/)

> [!TIP]
> Yeni bir ders veya çalışma eklerken `templates/COURSE_TEMPLATE.md` dosyasını referans alarak dökümantasyonunuzu oluşturabilirsiniz.
"""

def get_subdir_readme_content(dept_name, sub_key):
    dept_title = format_title(dept_name)
    sub = SUBDIR_DEFS[sub_key]
    return f"""# 📂 {sub['label']} — {dept_title}

## 📖 Açıklama
{sub['desc']}

---

## 📝 Bu Klasöre Nasıl Katkı Yapılır?
1. `templates/COURSE_TEMPLATE.md` dosyasını şablon olarak kullanın
2. İlgili ders/proje dosyalarını `DERS_ADI.md` formatında ekleyin
3. İçeriği kuramsal notlar, kaynaklar ve kod/örneklerle zenginleştirin
4. Pull Request açarak sisteme katkıda bulunun

> [!NOTE]
> Bu klasör **{dept_title}** alanının **{sub['label']}** katmanına aittir.
"""

def scaffold_department(dept_path, dept_name):
    readme_path = os.path.join(dept_path, 'README.md')
    if not os.path.exists(readme_path) or os.path.getsize(readme_path) == 0:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(get_dept_readme_content(dept_name))

    for sub_key in SUBDIR_DEFS.keys():
        sub_path = os.path.join(dept_path, sub_key)
        os.makedirs(sub_path, exist_ok=True)
        sub_readme = os.path.join(sub_path, 'README.md')
        if not os.path.exists(sub_readme) or os.path.getsize(sub_readme) == 0:
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
    
    print(f"\nDone! Scaffolded/Verified {count} departments across {len(CONTAINERS)} containers.")

if __name__ == "__main__":
    main()
