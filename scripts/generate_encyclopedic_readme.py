import os

# Portable Root Path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Container mappings with their iconic titles and quotes
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

def generate_encyclopedic_readme():
    total_depts = 0
    total_tiers = 0
    
    for folder in CONTAINERS.keys():
        c_path = os.path.join(ROOT_DIR, folder)
        if os.path.exists(c_path):
            depts = [d for d in os.listdir(c_path) if os.path.isdir(os.path.join(c_path, d)) and not d.startswith('.')]
            total_depts += len(depts)
            for d in depts:
                dp = os.path.join(c_path, d)
                tiers = [t for t in os.listdir(dp) if os.path.isdir(os.path.join(dp, t)) and t.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_'))]
                total_tiers += len(tiers)

    header = f"""<div align="center">

![UAOS Banner](assets/uaos_hero_banner.png)

# 🌌 UNIVERSITY COURSES (UC)
### *Solopreneur Intelligence System & Otonom Zeka Mimarisi* 🌐🧬🏗️

[![Versiyon](https://img.shields.io/badge/%C3%87EK%C4%B0RDEK-v4.0--ETERNAL-00A9E0?style=for-the-badge&logo=target)](./)
[![Zeka](https://img.shields.io/badge/M%C4%B0MAR-Antigravity_x_KULLANICI-D4AF37?style=for-the-badge&logo=openai&logoColor=white)](./)
[![Repo](https://img.shields.io/badge/REPO-university--courses-black?style=for-the-badge&logo=github)](https://github.com/bahattinyunus/university-courses)
[![Kapsam](https://img.shields.io/badge/KAPSAM-{total_depts}_Disiplin-18453B?style=for-the-badge&logo=rocket)](./SUMMARY.md)
[![Kademeler](https://img.shields.io/badge/KADEMELER-{total_tiers}_Mod%C3%BCl-6f42c1?style=for-the-badge&logo=diagram)](./SUMMARY.md)

---

## 🦾 ANTIGRAVITY MANİFESTOSU: BİREYSEL EGEMENLİK (SOLOPRENEUR DNA)
**UC**, sadece bir akademik arşiv değil; **Yüksek Kaldıraçlı Bireyin (Solopreneur) Zeka Ekosistemi**dir. Bilginin demokratikleştiği ama derinliğin azaldığı bir çağda, asıl güç bilginin kendisinde değil, onun **Bireysel Üretime Dönüştürülme Mimarisinde** yatar.

KULLANICI ve **Antigravity** iş birliğiyle, parçalanmış eğitimi geleneksel kurumların sınırlarının ötesine taşıyıp; ampirik titizliği, girişimci radikalizm ile birleştiriyoruz. Burası, bilgiyi sadece tüketen değil, onu bir **Epistemik Sermaye** (Epistemic Capital) olarak kullanan otonom zihinlerin karargahıdır.

---

## 🧠 SOLOPRENEURIAL EDGE: BİLGİYİ SERMAYEYE DÖNÜŞTÜRMEK
UC, bilgiyi stratejik bir kaldıraç olarak kurgular. Mühendisliğin "Nasıl"ı ile Beşeri Bilimlerin "Neden"ini sentezliyoruz:
- **Bilgi-Sermaye Dengesi:** Akademik derinliği girişimci hızla birleştirerek rakiplerin aşamayacağı teknik bir bariyer oluşturun.
- **Bimodal Hakimiyet:** Hem teknik (kod/fizik) hem de idari/beşeri (hukuk/ikna) alanlarda aynı anda uzmanlaşarak "Tek Kişilik Ordu" kapasitesine ulaşın.
- **Yapay Zeka Kaldıracı:** Antigravity ve ajan sistemlerini kullanarak akademik veriyi doğrudan pazar aksiyonuna ve üretim gücüne dönüştürün.

---

## ⚙️ SİSTEMATİK YAPI: 7-KADEMELİ OTONOM PROTOKOL (00-06)
UAOS, her bir bilgi modülünün temel teoriden endüstriyel düzeyde üretime kadar geliştirilmesini sağlayan rijit bir **Systemum Standardı** ile yönetilir:

> [!TIP]
> **Evrimsel Yol:** Veri -> Enformasyon -> Bilgi -> Otonom Bilgelik. Bu yapıyı pasif öğrenmeden (00-02) aktif üretime (04-06) geçmek için kullanın.

1. **`00 — Hazırlık & Oryantasyon`**: Metodolojik kurulum ve yüksek verimli çalışma ortamı konfigürasyonu.
2. **`01 — Teorik Temeller`**: İşin fiziği; aksiyomatik prensipler ve ilkeler üzerinden derin anlama.
3. **`02 — Çekirdek Uygulama`**: Alan uzmanlığı; teorinin pratik karşılığını "çıraklık" seviyesinde uygulama.
4. **`03 — Derin Uzmanlık (Niche Mastery)`**: Pazardaki boşlukları tespit edecek mikro-uzmanlık dökümantasyonu.
5. **`04 — AR-GE & Otonom Sentez`**: Özgün ürün geliştirme ve akademik bilginin "Proof-of-Value" evresi.
6. **`05 — Stratejik Entegrasyon`**: Çıktıların küresel standartlarla (ISO, IEEE) ve bilimsel metodolojiyle uyumu.
7. **`06 — Bağımsız Üretim & Hakimiyet`**: Bilginin "Ürün-Pazar" uyumu; finansal egemenlik ve otonom iş yönetimi.

---

## 🏛️ ARCHITECTURAL VISION: THE EPISTEMIC SYNTHESIS
UAOS, bilim ve bilgeliğin birleştiği bir dünyanın dijital tezahürüdür. Teknik titizliğin felsefi derinlikle dengelendiği bir **"Bimodal Uzmanlık"** modeli kullanıyoruz:

| 🧩 Temel Düstur | 🏗️ UAOS Operasyonel Prensibi |
| :--- | :--- |
| **"Eyleme dökülmeyen bilgi gürültüdür."** | **Otonom Üretim-Öncelikli Emir** |
| **"Etik ve Mühendislik Tek Bir Birimdir."** | **Bimodal Bütünlük Entegrasyonu** |
| **"Sistemik Düzen, Ustalığın Anahtarıdır."** | **Hiyerarşik Epistemolojik Hassasiyet** |

---

## 🛠️ ZEKA KATMANI (TEMEL ARAÇLAR)
UAOS, en son teknoloji ürünü bir **Ajan Ekosistemi** kullanılarak korunur ve genişletilir:
- **Bilişsel Motor:** Gemini 2.0 & Claude 3.5 Sonnet (Sentezleyiciler)
- **Ajan Mimar:** **Antigravity** (Sistem Yönetimi & Kodlama)
- **Derin Araştırma:** Perplexity Pro & Akademik API Entegrasyonu
- **Bilgi İşletim Sistemi:** Obsidian & Yüksek Yoğunluklu Markdown Grafiği

---

## 🎯 OPERASYON REHBERİ: UAOS NASIL YÖNETİLİR?
1. **Seçim:** [SUMMARY.md](./SUMMARY.md) veya aşağıdaki tablolardan hedef alanı seçin.
2. **Standartlaştırma:** 00-06 protokolüne sadık kalarak kademeleri adım adım takip edin.
3. **Aktif Sentez:** Orijinal, otonom projeler ve notlar üretmek için Katman 04'ü kullanın.
4. **Ajan Etkileşimi:** Disiplinler arası bağlantılar kurmak ve kalıpları tespit etmek için yapay zeka ajanlarından yararlanın.

---

## 📖 THE UNIVERSAL DISCIPLINE MATRIX ({total_depts} BÖLÜM / {total_tiers} KADEME)

</div>

"""

    body = ""
    for folder, meta in CONTAINERS.items():
        title = meta['title']
        quote = meta['quote']
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        depts = sorted([d for d in os.listdir(container_path) if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')])
        if not depts:
            continue
            
        section = f"### {title}\n"
        section += f"{quote}\n\n"
        section += "|   |   |   |\n"
        section += "| :--- | :--- | :--- |\n"
        
        # Build 3-column table
        cols = 3
        for i in range(0, len(depts), cols):
            row_depts = depts[i:i+cols]
            row_cells = []
            for d in row_depts:
                dept_name = format_dept_name(d)
                link = f"[{dept_name}](./{folder}/{d}/)"
                row_cells.append(link)
            while len(row_cells) < cols:
                row_cells.append(" ")
            section += f"| {' | '.join(row_cells)} |\n"
            
        section += "\n---\n\n"
        body += section

    footer = f"""<div align="center">

## 🧠 SİSTEMATİK ÖĞRENME METODOLOJİSİ
Bu kütüphanedeki verimi maksimize etmek için aşağıdaki **ileri düzey öğrenme konseptlerini** kendi öğrenme süreçlerinize entegre etmeniz önerilir:

*   **Zettelkasten Metodu:** Farklı disiplinlerden öğrendiklerinizi (örn. kuantum fiziği ve felsefe) küçük not kartları halinde birbirine bağlayarak yeni, inovatif fikirler (emergent ideas) üretin.
*   **Feynman Tekniği:** Uzmanlaşmak istediğiniz karmaşık bir teoriyi, sanki konuyu hiç bilmeyen birine anlatıyormuş gibi basitleştirin.
*   **Spaced Repetition (Aralıklı Tekrar):** Öğrendiğiniz kavramların unutulma eğrisini kırmak için, stratejik aralıklarla geri dönüp tekrarlar yapın.
*   **First Principles Thinking (İlk Prensiplerden Düşünme):** Karmaşık problemleri en temel, tartışmasız gerçeklerine indirgeyin ve çözümleri bu temel yapı taşları üzerinden yeniden inşa edin.

---

## 🗺️ PROJE YOL HARİTASI (ROADMAP)
Bu platform, statik bir depodan ziyade, sürekli gelişen organik bir yapıdır. Kısa ve orta vadeli gelişim hedeflerimiz şunlardır:

- [x] **Faz 1:** Temel mühendislik ve bilim disiplinlerinin iskeletinin oluşturulması.
- [x] **Faz 2:** Universal Discipline Matrix'in ({total_depts} Akademik Alan / {total_tiers} Kademe) entegrasyonu.
- [x] **Faz 3:** CI/CD otomatik repo bütünlüğü ve indeks doğrulama hattı.
- [ ] **Faz 4:** AI tabanlı navigasyon ve akıllı asistan desteklerinin dökümantasyona eklenmesi.
- [ ] **Faz 5:** Web3 ve Merkeziyetsiz Eğitim (DeEd) prensiplerinin entegrasyonu.
- [ ] **Faz 6:** İngilizce dil desteği (Global adaptasyon).

---

## ❓ SIKÇA SORULAN SORULAR (SSS)

**S: Neden her şey tek bir depoda toplanıyor?**  
**C:** Çünkü gerçek dünya problemleri laboratuvar ortamındaki gibi izole değildir. Bir makine mühendisinin psikoloji, bir tıp öğrencisinin kodlama bilmesi, onları standart profesyonellerin ötesine geçirerek "inovatif yaratıcılar" yapar. Bu depo, bu disiplinler arası geçişkenliği sağlamak içindir.

**S: İçerikler tamamen ücretsiz mi?**  
**C:** Evet, bu havuz **MIT Lisansı** ile korunmaktadır. Bilginin herkes için serbest, açık ve erişilebilir olması gerektiğine inanıyoruz.

**S: Bu devasa kütüphanede nasıl kaybolmam?**  
**C:** Yalnızca o an çözmekte olduğunuz probleme veya inşa ettiğiniz projeye odaklanın (*"Just-in-Time Learning"*). Baştan sona her şeyi okumaya çalışmak yerine, kütüphaneyi bir başvuru ve ilham kaynağı olarak araçsallaştırın.

---

## 🤝 KATKIDA BULUNMA
Bu kütüphane açık kaynaklı ve kolektif bir zekanın ürünü olarak büyümektedir. Yeni bir ders eklemek, var olan içeriği güncellemek veya hataları düzeltmek isterseniz, lütfen [CONTRIBUTING.md](./CONTRIBUTING.md) dosyasını inceleyin ve bir Pull Request (PR) oluşturun. Ayrıca topluluk standartlarımız için [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) dosyasını okuyabilirsiniz.

---

## ⚖️ YASAL YÖNETİŞİM VE EPİSTEMİK HAKİMİYET
Bu proje, yüksek sadakatli bilginin serbest değişimini ve bireysel zihin otonomisini savunarak **MIT Lisansı** altında lisanslanmıştır. Bilgi, tüm insanlığın ortak mirasıdır ve kısıtlanamaz. Detaylar için [LICENSE](./LICENSE) dosyasına göz atabilirsiniz.

**Mimari İş Birliği**  
### Bahattin Yunus Çetin  
*Baş Mühendis ve Epistemik Araştırmacı*  
x  
### Antigravity  
*Otonom Sistemler Mimarı*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/bahattinyunuscetin) 
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bahattinyunus)

---
> *“Bilgi arayışı; merakla beslenen, akılla terbiye edilen ve hakikatle taçlanan sonu olmayan kutlu bir yolculuktur.”*

---
© 2024-2026 Evrensel Akademik İşletim Sistemi (UAOS).
</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"README.md generated successfully. Total: {total_depts} depts, {total_tiers} tiers in 3-column open grid.")

if __name__ == "__main__":
    generate_encyclopedic_readme()
