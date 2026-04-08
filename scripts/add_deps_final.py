import os
import shutil

root_dir = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"
template_file = os.path.join(root_dir, 'templates', 'COURSE_TEMPLATE.md')

directories_to_scaffold = [
    '01_Temel_Bilimler_ve_Giris',
    '02_Alan_Dersleri',
    '03_Secmeli_ve_Ileri_Uygulama',
    '04_Arastirma_ve_Bitirme'
]

readme_append_text = """

---

## 📂 Çekirdek Ders Ağacı
Akademik sistem entegrasyonu kapsamında bu bölüm için önerilen ve standartlaştırılmış ders/çalışma klasörleri:

- [01 Temel Bilimler ve Seminerler](01_Temel_Bilimler_ve_Giris/)
- [02 Alan Dersleri ve Pratik](02_Alan_Dersleri/)
- [03 Seçmeli, İleri ve Uzmanlık Dersleri](03_Secmeli_ve_Ileri_Uygulama/)
- [04 Bitirme, Araştırma ve Çapraz Projeler](04_Arastirma_ve_Bitirme/)

> [!TIP]
> Yeni bir ders eklerken ana dizindeki `DERS_SABLONU.md` dosyasını kopyalayarak ilgili alt klasörün içine koyabilir ve kolayca kendi not şablonunuzu oluşturabilirsiniz!
"""

# YÖK final liste - tüm eksik bölümler (kapsamlı)
missing_deps = [
    # Mühendislik
    ('biyomuhendislik', 'Biyomühendislik'),
    ('siber_guvenlik_muhendisligi', 'Siber Güvenlik Mühendisliği'),
    ('insaat_teknolojisi_muhendisligi', 'İnşaat Teknolojisi Mühendisliği'),
    ('tekstil_teknolojisi_muhendisligi', 'Tekstil Teknolojisi Mühendisliği'),
    ('tarim_makineleri_ve_teknolojileri_muhendisligi', 'Tarım Makineleri ve Teknolojileri Mühendisliği'),
    ('geomatik_muhendisligi', 'Geomatik Mühendisliği'),
    ('biyokimya_muhendisligi', 'Biyokimya Mühendisliği'),
    # Tasarım & Sanat
    ('endustriyel_tasarim', 'Endüstriyel Tasarım'),
    ('grafik_tasarimi', 'Grafik Tasarımı'),
    ('tekstil_ve_moda_tasarimi', 'Tekstil ve Moda Tasarımı'),
    ('kuyumculuk_ve_mucevher_tasarimi', 'Kuyumculuk ve Mücevher Tasarımı'),
    ('seramik_ve_cam_tasarimi', 'Seramik ve Cam Tasarımı'),
    # Sağlık & Sosyal Hizmet
    ('cocuk_gelisimi', 'Çocuk Gelişimi'),
    ('saglik_bilgisi_ogretmenligi', 'Sağlık Bilgisi Öğretmenliği'),
    ('ameliyathane_hizmetleri', 'Ameliyathane Hizmetleri'),
    ('anestezi_ve_reanimasyon', 'Anestezi ve Reanimasyon'),
    ('tibbi_goruntuleme_teknikleri', 'Tıbbi Görüntüleme Teknikleri'),
    ('tibbi_laboratuvar_teknikleri', 'Tıbbi Laboratuvar Teknikleri'),
    ('ozurluluk_calismalari', 'Özürlülük Çalışmaları'),
    # İİBF & İşletme
    ('muhasebe_ve_finans_yonetimi', 'Muhasebe ve Finans Yönetimi'),
    ('sigortacilik_ve_risk_yonetimi', 'Sigortacılık ve Risk Yönetimi'),
    ('dis_ticaret', 'Dış Ticaret'),
    ('enerji_yonetimi', 'Enerji Yönetimi'),
    ('girişimcilik', 'Girişimcilik'),
    # Turizm & Ağırlama
    ('turizm_rehberligi', 'Turizm Rehberliği'),
    ('yiyecek_icecek_isletmeciligi', 'Yiyecek İçecek İşletmeciliği'),
    # Eğitim
    ('muzik_ogretmenligi', 'Müzik Öğretmenliği'),
    ('resim_is_ogretmenligi', 'Resim-İş Öğretmenliği'),
    ('beden_egitimi_ve_spor_bilimleri', 'Beden Eğitimi ve Spor Bilimleri'),
    # Fen & Sosyal Bilimler
    ('kimya_bolumu', 'Kimya Bölümü'),  # pure chemistry (not engineering)
    ('biyoistatistik', 'Biyoistatistik'),
    ('jeoloji', 'Jeoloji'),
    ('cografya_bolumu', 'Coğrafya Bölümü'),
    # Dil & Edebiyat
    ('fransiz_dili_ve_edebiyati', 'Fransız Dili ve Edebiyatı'),
    ('alman_dili_ve_edebiyati', 'Alman Dili ve Edebiyatı'),
    ('arap_dili_ve_edebiyati', 'Arap Dili ve Edebiyatı'),
    ('rus_dili_ve_edebiyati', 'Rus Dili ve Edebiyatı'),
    # Diğer Bölümler
    ('sinema_ve_televizyon', 'Sinema ve Televizyon'),
    ('tiyatro_oyunculuk', 'Tiyatro Oyunculuk'),
    ('fotoğrafcilik_ve_video', 'Fotoğrafçılık ve Video'),
    ('basin_yayin', 'Basın Yayın'),
]

def scaffold_dir(target_dir):
    for struct_dir in directories_to_scaffold:
        dpath = os.path.join(target_dir, struct_dir)
        if not os.path.exists(dpath):
            os.makedirs(dpath)
    if os.path.exists(template_file):
        dest_template = os.path.join(target_dir, 'DERS_SABLONU.md')
        if not os.path.exists(dest_template):
            shutil.copy2(template_file, dest_template)
    readme_path = os.path.join(target_dir, 'README.md')
    if not os.path.exists(readme_path):
        readme_path = os.path.join(target_dir, 'readme.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if "## 📂 Çekirdek Ders Ağacı" not in content:
            with open(readme_path, 'a', encoding='utf-8') as f:
                f.write(readme_append_text)

for dep_slug, dep_display in missing_deps:
    dep_path = os.path.join(root_dir, dep_slug)
    if not os.path.exists(dep_path):
        os.makedirs(dep_path)
        readme_content = f"# {dep_display}\n\nBu klasör **{dep_display}** bölümüne ait akademik notlar, araştırmalar ve dökümanlar içindir.\n"
        with open(os.path.join(dep_path, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(readme_content)
        scaffold_dir(dep_path)
        print(f"Created + scaffolded: {dep_slug}")
    else:
        print(f"Already exists: {dep_slug}")

print(f"\nToplam {len(missing_deps)} bölüm işlendi.")
