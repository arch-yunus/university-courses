import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONTAINERS = {
    'epistemik': '👁️ Epistemik Vizyon & Felsefe',
    'meta_muhendislik': '🛠️ Mühendislik & İleri Teknoloji',
    'mimarlik_ve_tasarim': '🏛️ Mimarlık, Tasarım & Şehircilik',
    'guzel_sanatlar': '🖼️ Güzel Sanatlar & Estetik',
    'saglik': '🩺 Sağlık Bilimleri & Tıp',
    'ogretmenlik': '🎓 Eğitim Fakültesi & Pedagoji',
    'spor_bilimleri': '🏅 Spor Bilimleri & Performans',
    'sosyal_ve_beseri_bilimler': '⚖️ Sosyal, Beşeri & İdari Bilimler',
    'temel_bilimler': '🧪 Temel Fen Bilimleri',
    'edebiyat_ve_diller': '📚 Filoloji, Dil & Edebiyat',
    'iletisim': '📡 İletişim & Medya Bilimleri',
    'turizm_ve_gastronomi': '🏨 Turizm, Otelcilik & Gastronomi',
    'tarim_ve_ziraat_bilimleri': '🌱 Tarım, Ziraat & Doğa Bilimleri',
    'askeri_bilimler_ve_savunma_teknolojileri': '⚔️ Savunma Sanayii & Güvenlik Stratejileri',
    'hukuk_bilimi': '⚖️ Adalet & Hukuk Bilimleri',
    'ilahiyat_ve_din': '📚 Theology, Comparative Religion & Philosophy',
    'on_lisans_programlari': '📋 Mesleki Yüksekokul (Ön Lisans)',
    'ozel_arastirma_alanlari': '🔬 Disiplinlerarası & Özel Araştırma',
    'kariyer_ve_sertifikasyonlar': '🚀 Kariyer, Portfolyo & Sertifika',
    'meta_yetkinlikler_ve_gelisim': '🧠 Meta-Zihin & Kişisel Disiplin',
    'genel': '📂 Genel Arşiv & Ortak Alanlar'
}

def format_dept_name(d):
    dept_name = d.replace('_', ' ').title()
    dept_name = (dept_name
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
    return dept_name

def generate_summary():
    total_count = 0
    total_tiers = 0
    
    summary_md = "# 🗂️ Evrensel Akademik Müfredat ve Bilgi İndeksi\n\n"
    summary_md += "Bu dosya otomatik olarak oluşturulmuştur. Tüm sektörler uluslararası akademik standartlara ve küresel profesyonel gerekliliklere göre gruplandırılmıştır.\n\n"
    
    body_content = ""
    for folder, title in CONTAINERS.items():
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        items = os.listdir(container_path)
        depts = [d for d in items if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')]
        depts.sort()
        if not depts:
            continue
            
        container_section = f"## {title} ({len(depts)} Alan)\n\n"
        container_section += "| Bölüm / Alan | Konum | Standart Kademeler |\n"
        container_section += "| :--- | :--- | :---: |\n"
        
        for d in depts:
            dept_name = format_dept_name(d)
            link = f"[{d}]({folder}/{d}/)"
            dept_path = os.path.join(container_path, d)
            tiers = [t for t in os.listdir(dept_path) if os.path.isdir(os.path.join(dept_path, t)) and t.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_'))]
            tier_badge = f"`00-06 ({len(tiers)} Kademe)`"
            container_section += f"| **{dept_name}** | {link} | {tier_badge} |\n"
            total_count += 1
            total_tiers += len(tiers)
        
        container_section += "\n"
        body_content += container_section

    summary_md += f"**Toplam Kapsam:** {total_count} Akademik ve Profesyonel Alan ({total_tiers} Standartlaştırılmış Kademe / 7-Kademeli Elit Yapı)\n\n"
    summary_md += body_content

    with open(os.path.join(ROOT_DIR, 'SUMMARY.md'), 'w', encoding='utf-8') as f:
        f.write(summary_md)
    print(f"SUMMARY.md updated successfully with {total_count} areas and {total_tiers} tiers.")

if __name__ == "__main__":
    generate_summary()
