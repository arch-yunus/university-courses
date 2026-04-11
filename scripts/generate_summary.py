import os

# Portable Root Path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
    'hukuk_bilimi': '⚖️ Hukuk',
    'ilahiyat_ve_din': '📚 Theology and Comparative Religion',
    'on_lisans_programlari': '📋 Ön Lisans Programları',
    'ozel_arastirma_alanlari': '🔬 Özel Araştırma Alanları',
    'kariyer_ve_sertifikasyonlar': '🚀 Kariyer ve Sertifikasyonlar',
    'meta_yetkinlikler_ve_gelisim': '🧠 Meta-Yetkinlikler ve Gelişim',
    'askeri_bilimler_ve_savunma_teknolojileri': '⚔️ Askeri Bilimler ve Savunma',
    'genel': '📂 Genel ve Ortak Alanlar'
}

def generate_summary():
    total_count = 0
    summary_md = "# 🗂️ Evrensel Akademik Müfredat ve Bilgi İndeksi\n\n"
    summary_md += "Bu dosya otomatik olarak oluşturulmuştur. Tüm sektörler uluslararası akademik standartlara ve küresel profesyonel gerekliliklere göre gruplandırılmıştır.\n\n"
    
    body_content = ""
    for folder, title in CONTAINERS.items():
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        container_section = f"## {title}\n\n"
        container_section += "| Bölüm / Alan | Yol |\n"
        container_section += "|--------------|-----|\n"
        
        items = os.listdir(container_path)
        depts = [d for d in items if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')]
        depts.sort()
        
        for d in depts:
            dept_name = d.replace('_', ' ').title()
            link = f"[{d}]({folder}/{d}/)"
            container_section += f"| {dept_name} | {link} |\n"
            total_count += 1
        
        container_section += "\n"
        body_content += container_section

    summary_md += f"**Toplam Kapsam:** {total_count} Akademik ve Profesyonel Alan (Global 7-Kademeli Elit Yapı)\n\n"
    summary_md += body_content

    with open(os.path.join(ROOT_DIR, 'SUMMARY.md'), 'w', encoding='utf-8') as f:
        f.write(summary_md)
    print(f"SUMMARY.md updated successfully with {total_count} areas.")

if __name__ == "__main__":
    generate_summary()
