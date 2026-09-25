import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONTAINERS = {
    'epistemik': {
        'title': '👁️ Epistemik Vizyon & Felsefe',
        'quote': '> *“Bilgi bir ışıktır; onu arayan zihin karanlıkta kalmaz. Hakikatin peşinde olmak en yüce ibadettir.”* — **El-Bîrûnî**'
    },
    'meta_muhendislik': {
        'title': '🛠️ Mühendislik & İleri Teknoloji',
        'quote': '> *“Bilim insanları var olan dünyayı inceler; mühendisler ise daha önce hiç var olmamış dünyaları yaratır.”* — **Theodore von Kármán**'
    },
    'mimarlik_ve_tasarim': {
        'title': '🏛️ Mimarlık, Tasarım & Şehircilik',
        'quote': '> *“Mimarlık, taşın ve ışığın sessiz şiiridir; mekân ise insan ruhunun biçim bulmuş halidir.”* — **Mimar Sinan**'
    },
    'guzel_sanatlar': {
        'title': '🖼️ Güzel Sanatlar & Estetik',
        'quote': '> *“Sanat, doğanın gizemlerini keşfetme ve görünmeyeni görünür kılma çabasıdır.”* — **Leonardo da Vinci**'
    },
    'saglik': {
        'title': '🩺 Sağlık Bilimleri & Tıp',
        'quote': '> *“Şifanın esası bedenin ve ruhun ahengini kavramaktır; tıp, insanın doğayla uyum sanatıdır.”* — **İbn-i Sînâ (Avicenna)**'
    },
    'ogretmenlik': {
        'title': '🎓 Eğitim Fakültesi & Pedagoji',
        'quote': '> *“Bana bir harf öğretenin kırk yıl kölesi olurum; zira akılları inşa edenler medeniyetin hakiki mimarlarıdır.”* — **Hz. Ali**'
    },
    'spor_bilimleri': {
        'title': '🏅 Spor Bilimleri & Performans',
        'quote': '> *“Bedenin terbiyesi zihnin keskinliğidir; disiplin, arzu ile başarı arasındaki köprüdür.”* — **Platon**'
    },
    'sosyal_ve_beseri_bilimler': {
        'title': '⚖️ Sosyal, Beşeri & İdari Bilimler',
        'quote': '> *“Coğrafya kaderdir; lakin toplumların yükselişi ve çöküşü adalet, asabiyet ve üretim dengesine bağlıdır.”* — **İbn-i Haldun**'
    },
    'temel_bilimler': {
        'title': '🧪 Temel Fen Bilimleri',
        'quote': '> *“Evrenin kitabı matematik dilinde yazılmıştır; onun harfleri üçgenler, daireler ve geometrik formlardır.”* — **Galileo Galilei**'
    },
    'edebiyat_ve_diller': {
        'title': '📚 Filoloji, Dil & Edebiyat',
        'quote': '> *“Dilimin sınırları, dünyamın sınırlarıdır; kelimeler düşüncenin yaşayan heykelleridir.”* — **Ludwig Wittgenstein**'
    },
    'iletisim': {
        'title': '📡 İletişim & Medya Bilimleri',
        'quote': '> *“Ortam, mesajın ta kendisidir; insan iletişim kurduğu ve anlam ürettiği ölçüde var olur.”* — **Marshall McLuhan**'
    },
    'turizm_ve_gastronomi': {
        'title': '🏨 Turizm, Otelcilik & Gastronomi',
        'quote': '> *“Dünyayı gezmek zihindeki sınırları kaldırır; lezzet ve misafirperverlik ise insanlığın ortak lisanıdır.”* — **Evliya Çelebi**'
    },
    'tarim_ve_ziraat_bilimleri': {
        'title': '🌱 Tarım, Ziraat & Doğa Bilimleri',
        'quote': '> *“Toprak berekettir; tohumu sabır, emek ve ilimle işleyen milletin hakiki efendisidir.”* — **Mustafa Kemal Atatürk**'
    },
    'askeri_bilimler_ve_savunma_teknolojileri': {
        'title': '⚔️ Askeri Bilimler ve Savunma',
        'quote': '> *“En büyük zafer, savaşmadan kazanılan zaferdir; strateji kuvvetten, akıl silahtan üstündür.”* — **Sun Tzu**'
    },
    'hukuk_bilimi': {
        'title': '⚖️ Adalet & Hukuk Bilimleri',
        'quote': '> *“Adalet mülkün temelidir; hukukun bittiği yerde tiranlık, karmaşa ve haksızlık başlar.”* — **John Locke**'
    },
    'ilahiyat_ve_din': {
        'title': '📚 İlahiyat, Karşılaştırmalı Din & Felsefe',
        'quote': '> *“İlim ilim bilmektir, ilim kendin bilmektir; sen kendini bilmezsin, ya nice okumaktır.”* — **Yunus Emre**'
    },
    'on_lisans_programlari': {
        'title': '📋 Mesleki Yüksekokul (Ön Lisans Programları)',
        'quote': '> *“Uygulamaya dökülmeyen bilgi bir yüktür; maharet ve teknik ustalık teorinin can damarıdır.”* — **El-Cezerî**'
    },
    'ozel_arastirma_alanlari': {
        'title': '🔬 Özel Araştırma & Disiplinlerarası Alanlar',
        'quote': '> *“Geleceği tahmin etmenin en emin yolu, onu bizzat inşa etmektir.”* — **Alan Kay**'
    },
    'kariyer_ve_sertifikasyonlar': {
        'title': '🚀 Kariyer, Portfolyo & Sertifikasyonlar',
        'quote': '> *“Şans, yalnızca hazırlıklı ve yetkin zihinlere güler; profesyonel ustalık kesintisiz inşa edilir.”* — **Louis Pasteur**'
    },
    'meta_yetkinlikler_ve_gelisim': {
        'title': '🧠 Meta-Yetkinlikler ve Gelişim',
        'quote': '> *“Düşünceleriniz ne ise hayatınız da odur; kendi zihnini yöneten, tüm dünyaya yön verir.”* — **Marcus Aurelius**'
    },
    'genel': {
        'title': '📂 Genel ve Ortak Alanlar',
        'quote': '> *“Bütün büyük işler, küçük ve disiplinli adımların kararlılıkla bir araya gelmesiyle gerçekleşir.”* — **Vincent van Gogh**'
    }
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
    summary_md += "> *“Öğrenmek akıntıya karşı kürek çekmek gibidir; durursanız gerilersiniz.”* — **Çin Atasözü**\n\n"
    summary_md += "Bu dosya otomatik olarak oluşturulmuştur. Tüm sektörler uluslararası akademik standartlara ve küresel profesyonel gerekliliklere göre gruplandırılmıştır.\n\n"
    
    body_content = ""
    for folder, meta in CONTAINERS.items():
        title = meta['title']
        quote = meta['quote']
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        items = os.listdir(container_path)
        depts = [d for d in items if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')]
        depts.sort()
        if not depts:
            continue
            
        container_section = f"## {title} ({len(depts)} Alan)\n\n"
        container_section += f"{quote}\n\n"
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
