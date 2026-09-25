import os

# Portable Root Path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Container mappings for display
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

SPECIAL_DESCRIPTIONS = {
    # --- Epistemik ---
    'bilgi_ontolojisi': 'Bilginin yapısı, geçerliliği, sınıflandırılması ve kavramsal temellerinin ontolojik analizi.',
    'felsefi_sorgulama': 'Düşünce sistemleri, aksiyomlar ve analitik akıl yürütme yöntemlerinin sistematik tetkiki.',
    'zihin_mimarisi': 'Bilişsel modeller, zihinsel şemalar ve yüksek düzeyli kavrayış sistemlerinin mimarisi.',

    # --- Mühendislik (Core Nodes) ---
    'bilgisayar_muhendisligi': 'Yazılım sistemleri, veri yapıları ve otonom zihin mimarisi ile hesaplama teorisinin yüksek sadakatli entegrasyonu.',
    'elektrik_elektronik_muhendisligi': 'Enerji, sinyal işleme ve elektromanyetik teorinin modern mühendislik zirvesindeki fiziksel realizasyonu.',
    'yapay_zeka_ve_veri_muhendisligi': 'Ham veriden otonom anlam çıkarma, makine öğrenmesi ve akıllı karar destek sistemlerinin stratejik mimarisi.',
    'siber_guvenlik_muhendisligi': 'Dijital varlıkların savunma stratejileri, sızma testleri ve kriptografik güvenlik ontolojisi.',
    'havacilik_ve_uzay_muhendisligi': 'Yeryüzü sınırlarını aşan yüksek fizik, aerodinamik ve gelişmiş itki sistemleri mühendisliği.',
    'yazilim_muhendisligi': 'Karmaşık sistemlerin sürdürülebilir, ölçeklenebilir ve yüksek performanslı dijital yapılar olarak inşası.',
    'mekatronik_muhendisligi': 'Mekanik, elektronik ve akıllı kontrol sistemlerinin otonom robotik sentezi.',
    'insaat_muhendisligi': 'Fiziksel dünyayı şekillendiren; mukavemet, sürdürülebilirlik ve kentsel nizamın mühendislik omurgası.',
    'makine_muhendisligi': 'Termodinamik güç, mekanik tasarım ve enerjinin kinetik realizasyonu üzerine kurulu kadim disiplin.',
    'biyomedikal_muhendisligi': 'Mühendislik prensiplerinin insan biyolojisi ve medikal teknoloji ile otonom entegrasyonu.',
    'jeoloji_muhendisligi': 'Yer kabuğunun kompozisyonu, evrimi ve doğal kaynakların stratejik analizi.',
    'endustri_muhendisligi': 'Süreç optimizasyonu, verimlilik analitiği ve karmaşık sistemlerin matematiksel modellenmesi.',
    'kimya_muhendisligi': 'Maddenin moleküler dönüşümü, reaktör tasarımı ve endüstriyel proseslerin kimyasal kontrolü.',
    
    # --- Sağlık & Tıp (Core Nodes) ---
    'tip': 'İnsan biyolojisinin patolojik ve fizyolojik süreçlerinin medikal bilimler ışığında klinik analizi ve şifa sanatı.',
    'dis_hekimligi': 'Oral ve maksillofasiyal sağlığın cerrahi, estetik ve klinik protokollere göre bilimsel yönetimi.',
    'eczacilik': 'Farmakolojik bileşenlerin sentezi, etkileşimi ve tedavi edici mekanizmalarının biyokimyasal derinlikte analizi.',
    'hemsirelik': 'Klinik bakım süreçlerinin bilimsel metodoloji ve bütüncül sağlık vizyonu ile profesyonel yönetimi.',
    'veterinerlik': 'Hayvan sağlığı, zootekni ve halk sağlığı dengesinin karşılaştırmalı biyolojik analizi.',
    'fizyoterapi_ve_rehabilitasyon': 'Hareket sistemi patolojilerinin nöromusküler ve biyomekanik prensiplerle rehabilitasyonu.',
    'beslenme_ve_diyetetik': 'Biyoenerjetik süreçler, klinik nutrisyon ve metabolik sağlığın bilimsel yönetimi.',
    
    # --- Sosyal & Beşeri Bilimler (Core Nodes) ---
    'hukuk': 'Adalet mekanizmalarının ve toplumsal nizamın normatif ve analitik yaklaşımlarla kurgulandığı yasal ontoloji.',
    'psikoloji': 'İnsan davranışları ve bilişsel süreçlerin ampirik yöntemlerle analiz edildiği otonom zihin laboratuvarı.',
    'felsefe': 'Varlığın, bilginin ve değerlerin mantıksal ve diyalektik yöntemlerle sorgulandığı temel düşünce mimarisi.',
    'sosyoloji': 'Toplumsal yapılar, dinamikler ve kurumsal değişimlerin makro ve mikro düzeyde analitik incelenmesi.',
    'iktisat': 'Kısıtlı kaynakların dağılımı ve piyasa dinamiklerinin matematiksel ve davranışsal modellenmesi.',
    'uluslararasi_iliskiler': 'Küresel aktörlerin stratejik etkileşimleri, jeopolitik dengeler ve diplomasi mimarisi.',
    'siyaset_bilimi_ve_kamu_yonetimi': 'Güç dinamikleri, devlet mekanizmaları ve kamusal stratejilerin politik teori ışığında yönetimi.',
    'antropoloji': 'İnsan türünün zamansal gelişimi, kültürel varyasyonları ve biyolojik evriminin bütüncül analizi.',
    'aktuarya_bilimleri': 'Finansal risklerin, sigortacılık modellerinin ve belirsizlik dinamiklerinin matematiksel analitiği.',
    
    # --- Mimarlık & Tasarım (Core Nodes) ---
    'mimarlik': 'Estetik, fonksiyonellik ve yapı fiziğinin mekansal kurgu ve sürdürülebilirlik ilkeleriyle sentezi.',
    'ic_mimarlik_ve_cevre_tasarimi': 'İnsan ölçekli mekanların konfor, estetik ve fonksiyonel gereksinimlere göre içsel mimarisi.',
    'sehir_ve_bolge_planlama': 'Kentsel dokunun, ulaşım ağlarının ve yaşam alanlarının stratejik ve sürdürülebilir organizasyonu.',
    'endustriyel_tasarim': 'Kullanıcı deneyimi, ergonomi ve seri üretim dinamiklerini birleştiren ürün tasarımı.',
    
    # --- Zihin & Meta-Yetkinlikler ---
    'monk_mode_disiplin_sistemi': 'Yüksek odaklanma, sarsılmaz irade ve otonom disiplin için tasarlanmış zihinsel işletim sistemi.',
    'meta_zihin_ve_ogrenme': 'Bilgiyi işleme, derin öğrenme ve bilişsel esneklik için meta-seviye yetkinlik merkezi.',
    'sun_tzu_stratejik_dusunce': 'Kadim savaş sanatı ilkelerinin modern strateji, liderlik ve hayat mücadelesine adaptasyonu.',
    'stoisizm_ve_mental_dayaniklilik': 'Rasyonel zihin duruşu, içsel direnç ve duygusal denetim mimarisi.',
    'muzakere_ve_ikna_sanati': 'Bilişsel psikoloji ve stratejik iletişim ilkelerine dayalı yüksek etkili müzakere yönetimi.',
    'zaman_yonetimi_ve_u_u': 'Zamanın fraktal yönetimi, derin odaklanma ve operasyonel akış optimizasyonu.',
    
    # --- Özel Araştırma Alanları ---
    'kuantum_muhendisligi': 'Kuantum mekaniğinin atomik ve subatomik seviyede teknolojik realizasyonu ve hesaplama gücü.',
    'biyoinformatik': 'Biyolojik verilerin bilişim araçları ve algoritmik modellerle analizi ve genomik haritalama.',
    'osint_ve_siber_istihbarat': 'Açık kaynak verilerinden stratejik istihbarat üretimi ve dijital gözetleme teknikleri.',
}

CONTAINER_TEMPLATES = {
    'epistemik': 'Epistemik temel, ontolojik modelleme ve derin zihinsel sorgulama katmanı.',
    'meta_muhendislik': 'Sistem optimizasyonu ve ampirik bütünlüğe odaklanmış ileri mühendislik düğümü.',
    'mimarlik_ve_tasarim': 'Mekansal kurgu ve estetik fonksiyonelliğin bilimsel tasarım protokolü.',
    'guzel_sanatlar': 'Sanatsal ifade ve estetik kuramın yüksek yoğunluklu yaratıcılık laboratuvarı.',
    'saglik': 'Klinik doğruluk ve insan biyolojisi eksenli medikal uzmanlık katmanı.',
    'ogretmenlik': 'Pedagojik formasyon ve bilgi aktarım metodolojilerinin profesyonel mimarisi.',
    'spor_bilimleri': 'Kinetik performans, motorik gelişim ve spor fizyolojisi uzmanlık düğümü.',
    'sosyal_ve_beseri_bilimler': 'İnsan ve toplum dinamiklerinin analitik ve teorik inceleme merkezi.',
    'temel_bilimler': 'Varlığın temel yasalarının aksiyomatik ve matematiksel modelleme düğümü.',
    'edebiyat_ve_diller': 'Filolojik analiz ve kültürel veri yapılarının derin dilsel haritalaması.',
    'iletisim': 'Medya ekolojisi, dijital anlatı ve stratejik iletişim bilimleri çerçevesi.',
    'turizm_ve_gastronomi': 'Ağırlama endüstrisi, mutfak sanatları ve destinasyon yönetimi protokolü.',
    'tarim_ve_ziraat_bilimleri': 'Agro-ekolojik verimlilik, bitkisel üretim ve sürdürülebilir tarım mimarisi.',
    'hukuk_bilimi': 'Yasal ontoloji ve düzenleyici mekanizmaların normatif analiz çerçevesi.',
    'askeri_bilimler_ve_savunma_teknolojileri': 'Stratejik savunma hatları ve yüksek teknoloji güvenlik konseptleri.',
    'ilahiyat_ve_din': 'Teolojik doktrinler ve dini fenomenlerin metodolojik ve felsefi analizi.',
    'on_lisans_programlari': 'Uygulamalı teknik yetkinlik ve sektörel operasyonel uzmanlık odağı.',
    'ozel_arastirma_alanlari': 'İleri disiplinlerarası keşif, füzyon alanlar ve sınır araştırma düğümü.',
    'kariyer_ve_sertifikasyonlar': 'Küresel akreditasyon, profesyonel sertifikasyon ve portfolyo mimarisi.',
    'meta_yetkinlikler_ve_gelisim': 'Bilişsel genişleme, otonom irade ve zihinsel kaldıraç disiplini.',
    'genel': 'Ortak kaynaklar, akademik standartlar ve genel metodoloji arşivi.'
}

def get_desc(folder, container):
    if folder in SPECIAL_DESCRIPTIONS:
        return SPECIAL_DESCRIPTIONS[folder]
    
    t = folder.lower()
    
    if t.startswith('adli_'): return f"{folder.replace('adli_', '').replace('_', ' ').title()} alanının kriminalistik metodoloji ve yasal kanıt bilimi ile entegrasyonu."
    if t.startswith('akilli_'): return f"{folder.replace('akilli_', '').replace('_', ' ').title()} alanında otonom sistemler ve AI tabanlı yapılar kurgulayan ileri düğüm."
    if t.startswith('uluslararasi_'): return f"{folder.replace('uluslararasi_', '').replace('_', ' ').title()} disiplininin küresel standartlar ve sınır aşan dinamikler çerçevesinde analizi."
    
    if 'muhendis' in t: return 'Sistem optimizasyonu ve ampirik bütünlüğe odaklanmış ileri mühendislik düğümü.'
    if 'tasarim' in t: return 'Fonksiyonel estetik, kullanıcı deneyimi ve endüstriyel tasarım mimarisi.'
    if 'yonetim' in t or 'isletme' in t: return 'Stratejik karar zekası, operasyonel verimlilik ve organizasyonel liderlik çerçevesi.'
    if 'teknoloji' in t or 'program' in t: return 'Gelişmekte olan araçlar, metodolojik altyapılar ve teknolojik realizasyon odaklı alan.'
    if 'ogretmen' in t or 'egitim' in t: return 'Bilgi aktarımı, pedagojik formasyon ve öğretim metodolojilerinin uzmanlık alanı.'
    if 'bilim' in t: return 'Fenomenlerin gözlem, deney ve mantıksal analiz üzerine kurulu bilimsel araştırma düğümü.'
    if 'dili_ve_edebiyat' in t: return 'Dilsel yapılar, filolojik evrim ve edebi eserlerin kültürel veri analizi.'
    if 'tip' in t or 'saglik' in t or 'hemsire' in t: return 'Klinik protokoller, hasta bakımı ve koruyucu sağlık mekanizmaları odağı.'
    if 'tarim' in t or 'bitki' in t or 'ziraat' in t: return 'Toprak biyolojisi, bitkisel üretim ve sürdürülebilir tarımsal kaynak yönetimi.'
    
    return CONTAINER_TEMPLATES.get(container, 'Evrensel akademik standartlara göre yapılandırılmış bilgi düğümü.')

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
    # Calculate stats dynamically
    total_depts = 0
    total_tiers = 0
    container_counts = {}
    for folder in CONTAINERS.keys():
        c_path = os.path.join(ROOT_DIR, folder)
        if os.path.exists(c_path):
            depts = [d for d in os.listdir(c_path) if os.path.isdir(os.path.join(c_path, d)) and not d.startswith('.')]
            container_counts[folder] = len(depts)
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

KULLANICI ve **Antigravity** iş birliğiyle, parçalanmış eğitimi "muhafazakar" kurumların elinden alıp; ampirik titizliği, girişimci radikalizm ile birleştiriyoruz. Burası, bilgiyi sadece tüketen değil, onu bir **Sermaye** (Epistemic Capital) olarak kullanan otonom mimarların karargahıdır.

---

## 🧠 SOLOPRENEURIAL EDGE: BİLGİYİ SERMAYEYE DÖNÜŞTÜRMEK
UC, bilgiyi bir **Silah** olarak kurgular. Mühendisliğin "Nasıl"ı ile Sosyal Bilimlerin "Neden"ini sentezliyoruz:
- **Bilgi-Sermaye Dengesi:** Akademik derinliği, girişimci hızla birleştirerek rakiplerin ulaşamayacağı bir teknik bariyer oluşturun.
- **Bimodal Hakimiyet:** Hem teknik (kod/fizik) hem de idari/beşeri (hukuk/ikna) alanlarda aynı anda uzmanlaşarak "Tek Kişilik Ordu" kapasitesine ulaşın.
- **Yapay Zeka Kaldıracı:** Antigravity ve diğer ajan sistemlerini kullanarak, akademik veriyi pazar aksiyonuna dönüştürün.

---

## ⚙️ SİSTEMATİK YAPI: 7-KADEMELİ OTONOM PROTOKOL (00-06)
UAOS, her bir bilgi modülünün temel teoriden endüstriyel düzeyde üretime kadar geliştirilmesini sağlayan rijit bir **Systemum Standardı** ile yönetilir. Bu protokol, öğrenciyi pasif bir tüketiciden otonom bir mimara dönüştürür:

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
UAOS, bilim ve bilgeliğin artık ayrı olmadığı bir dünyanın dijital tezahürüdür. Teknik titizliğin felsefi derinlikle dengelendiği bir **"Bimodal Uzmanlık"** modeli kullanıyoruz. Bu, mühendisliğin "Nasıl"ı ile beşeri bilimlerin "Neden"i arasındaki köprü olan **Epistemolojik Sentez**'dir.

Mimari, üç ana hakimiyet sütunu üzerine kuruludur:
- **Küresel Envanter:** Tüm bilinen akademik evrenin yapılandırılmış, gezilebilir bir ızgara olarak haritalanması.
- **Çok Boyutlu Bütünlük:** "Birleşik bir Zeka Modeli" oluşturmak için ampirik verilerin etik içgörülerle birleştirilmesi.
- **Özyinelemeli Evrim:** Bu sistemdeki her bir düğüm, KULLANICI ve Antigravity tarafından güncellenmek, genişletilmek ve rafine edilmek üzere tasarlanmıştır.

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
1. **Seçim:** [SUMMARY.md](./SUMMARY.md) üzerinden bir hedef düğüm belirleyin.
2. **Standartlaştırma:** Dağıtım sırasında 00-06 protokolüne sadık kalın.
3. **Aktif Sentez:** Orijinal, otonom içerik üretmek için Katman 04'ü kullanın.
4. **Ajan Etkileşimi:** Disiplinler arası bağlantılar kurmak ve kalıpları tespit etmek için yapay zeka ajanlarından yararlanın.

---

## 📖 THE UNIVERSAL DISCIPLINE MATRIX ({total_depts} NODES / {total_tiers} TIERS)

The following sectors represent the complete topological map of the UAOS intelligence ecosystem.

</div>

"""

    body = ""
    for folder, title in CONTAINERS.items():
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        depts = sorted([d for d in os.listdir(container_path) if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')])
        if not depts:
            continue
            
        section = f"<details>\n<summary><b>{title} ({len(depts)} Alan)</b></summary>\n<br>\n\n"
        section += "| Branş / Alan | Epistemik & Metodolojik Odak |\n"
        section += "| :--- | :--- |\n"
        
        for d in depts:
            dept_name = format_dept_name(d)
            link = f"[{dept_name}]({folder}/{d}/)"
            desc = get_desc(d, folder)
            section += f"| {link} | {desc} |\n"
            
        section += "\n"
        section += "</details>\n\n"
        body += section

    footer = f"""
---

<div align="center">

## ⚖️ YASAL YÖNETİŞİM VE AÇIK KAYNAK HAKİMİYETİ
Bu proje, yüksek sadakatli bilginin serbest değişimini ve bireysel zihin otonomisini savunarak **MIT Lisansı** altında lisanslanmıştır.

**Mimari İş Birliği**  
### Bahattin Yunus Çetin  
*Baş Mühendis ve Araştırmacı*  
x  
### Antigravity  
*Otonom Sistemler Mimarı*

[Linkedin](https://linkedin.com/in/bahattinyunuscetin) | [GitHub](https://github.com/bahattinyunus)

---
*"Bilgi arayışı, merakla beslenen ve akılla terbiye edilen, sonu olmayan bir yolculuktur."*

---
© 2025-2026 Evrensel Akademik İşletim Sistemi (UAOS).
</div>
"""

    full_content = header + body + footer
    
    with open(os.path.join(ROOT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(full_content)
        
    print(f"README.md generated successfully. Total: {total_depts} depts, {total_tiers} tiers.")

if __name__ == "__main__":
    generate_encyclopedic_readme()
