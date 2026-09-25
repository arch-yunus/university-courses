import os

# Portable Root Path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Container mappings with their iconic titles and rich multi-quotes
CONTAINERS = {
    'epistemik': {
        'title': '👁️ Epistemik Vizyon & Bilgi Felsefesi',
        'quotes': [
            '“Bilgi bir ışıktır; onu samimiyetle arayan zihin karanlıkta kalmaz. Hakikatin peşinde olmak en yüce insanlık görevidir.” — **El-Bîrûnî**',
            '“Bütün insanlar doğal olarak bilmek isterler. Bilgelik, ilk ilkelerin ve nedenlerin bilimidir.” — **Aristoteles**',
            '“Kendini bilmek, tüm bilgeliğin başlangıcıdır.” — **Sokrates**'
        ]
    },
    'meta_muhendislik': {
        'title': '🛠️ Mühendislik & İleri Teknoloji Bilimleri',
        'quotes': [
            '“Bilim insanları var olan dünyayı inceler; mühendisler ise daha önce hiç var olmamış dünyaları yaratır.” — **Theodore von Kármán**',
            '“Bir makine insan emeğini hafifletmiyorsa ve zihni özgürleştirmiyorsa, sadece karmaşık bir demir yığınıdır.” — **Nikola Tesla**',
            '“Mühendislik, bilimi insanlığın refahı için gerçeğe dönüştürme sanatıdır.” — **Neil Armstrong**'
        ]
    },
    'mimarlik_ve_tasarim': {
        'title': '🏛️ Mimarlık, Tasarım & Mekânsal Şehircilik',
        'quotes': [
            '“Mimarlık, taşın ve ışığın sessiz şiiridir; mekân ise insan ruhunun biçim bulmuş halidir.” — **Mimar Sinan**',
            '“Biçim daima işlevi takip eder; bu doğanın en temel yasasıdır.” — **Louis Sullivan**',
            '“Bir binayı tasarlarken, geleceğin hatıralarını inşa edersiniz.” — **Juhani Pallasmaa**'
        ]
    },
    'guzel_sanatlar': {
        'title': '🖼️ Güzel Sanatlar, Estetik & Görsel Kültür',
        'quotes': [
            '“Sanat, doğanın gizemlerini keşfetme ve görünmeyeni görünür kılma çabasıdır.” — **Leonardo da Vinci**',
            '“Sanat, ruhlarımızdaki günlük hayatın tozunu silip süpürür.” — **Pablo Picasso**',
            '“Güzellik, hakikatin parıltısıdır.” — **Platon**'
        ]
    },
    'saglik': {
        'title': '🩺 Sağlık Bilimleri, Klinik Tıp & Yaşam',
        'quotes': [
            '“Şifanın esası bedenin ve ruhun ahengini kavramaktır; tıp, insanın doğayla uyum sanatıdır.” — **İbn-i Sînâ (Avicenna)**',
            '“Hastalık yoktur, hasta vardır; doğanın iyileştirici gücü hekimin en büyük yardımcısıdır.” — **Hipokrat**',
            '“Bedeninize iyi bakın; yaşamak zorunda olduğunuz yegâne eviniz orasıdır.” — **Jim Rohn**'
        ]
    },
    'ogretmenlik': {
        'title': '🎓 Eğitim Fakültesi, Pedagoji & Didaktik',
        'quotes': [
            '“Bana bir harf öğretenin kırk yıl kölesi olurum; zira akılları inşa edenler medeniyetin hakiki mimarlarıdır.” — **Hz. Ali**',
            '“Eğitim, dünyayı değiştirmek için kullanabileceğiniz en güçlü silahtır.” — **Nelson Mandela**',
            '“Öğretmek, iki kez öğrenmektir.” — **Joseph Joubert**'
        ]
    },
    'spor_bilimleri': {
        'title': '🏅 Spor Bilimleri, Kinetik & Fiziksel Performans',
        'quotes': [
            '“Bedenin terbiyesi zihnin keskinliğidir; disiplin, arzu ile başarı arasındaki köprüdür.” — **Platon**',
            '“Hiç kimse bedeninin ulaşabileceği potansiyeli görmeden yaşlanma hakkına sahip değildir.” — **Sokrates**',
            '“Zorluklar bedeni güçlendirir, tıpkı çalışma ve tefekkürün zihni güçlendirdiği gibi.” — **Seneca**'
        ]
    },
    'sosyal_ve_beseri_bilimler': {
        'title': '⚖️ Sosyal, Beşeri, İdari & Davranışsal Bilimler',
        'quotes': [
            '“Coğrafya kaderdir; lakin toplumların yükselişi ve çöküşü adalet, asabiyet ve üretim dengesine bağlıdır.” — **İbn-i Haldun**',
            '“Düşünüyorum, öyleyse varım.” — **René Descartes**',
            '“İncelenmemiş bir hayat, yaşanmaya değer değildir.” — **Sokrates**'
        ]
    },
    'temel_bilimler': {
        'title': '🧪 Temel Fen Bilimleri (Fizik, Kimya, Matematik)',
        'quotes': [
            '“Evrenin kitabı matematik dilinde yazılmıştır; onun harfleri üçgenler, daireler ve geometrik formlardır.” — **Galileo Galilei**',
            '“Doğanın sırlarını çözmek istiyorsanız; enerji, frekans ve titreşim cinsinden düşünün.” — **Nikola Tesla**',
            '“Matematik, insan aklının ulaştığı en yüce ve en soyut zaferdir.” — **Carl Friedrich Gauss**'
        ]
    },
    'edebiyat_ve_diller': {
        'title': '📚 Filoloji, Dilbilim & Dünya Edebiyatı',
        'quotes': [
            '“Dilimin sınırları, dünyamın sınırlarıdır; kelimeler düşüncenin yaşayan heykelleridir.” — **Ludwig Wittgenstein**',
            '“Bir dili bilmek bir insan olmaktır, iki dil bilmek iki insan olmaktır.” — **Johann Wolfgang von Goethe**',
            '“Kitaplar, zamanın dalgaları üzerinde yüzen ve nesilden nesle değer taşıyan düşünce gemileridir.” — **Francis Bacon**'
        ]
    },
    'iletisim': {
        'title': '📡 İletişim, Medya Ekolojisi & Dijital Anlatı',
        'quotes': [
            '“Ortam, mesajın ta kendisidir; insan iletişim kurduğu ve anlam ürettiği ölçüde var olur.” — **Marshall McLuhan**',
            '“İletişimdeki en büyük sorun, anlaşıldığı yanılsamasıdır.” — **George Bernard Shaw**',
            '“Doğru söz etkileyicidir, ama yerinde bir sükût hiçbir söze değişilmez.” — **Mark Twain**'
        ]
    },
    'turizm_ve_gastronomi': {
        'title': '🏨 Turizm, Ağırlama & Gastronomi Sanatı',
        'quotes': [
            '“Dünyayı gezmek zihindeki önyargıları kaldırır; lezzet ve misafirperverlik ise insanlığın ortak lisanıdır.” — **Evliya Çelebi**',
            '“Yemek yemek bir zorunluluktur, ancak akıllıca ve zevkle yemek bir sanattır.” — **François de La Rochefoucauld**',
            '“Yolculuk, sadece yeni manzaralar görmek değil; dünyaya yeni gözlerle bakabilmektir.” — **Marcel Proust**'
        ]
    },
    'tarim_ve_ziraat_bilimleri': {
        'title': '🌱 Tarım, Ziraat, Biyosistem & Doğa Bilimleri',
        'quotes': [
            '“Toprak berekettir; tohumu sabır, emek ve ilimle işleyen milletin hakiki efendisidir.” — **Mustafa Kemal Atatürk**',
            '“Toprak işlenmedikçe zenginlik vermez; doğanın yasalarına uymayan hiçbir sistem ayakta kalamaz.” — **Ksenophon**',
            '“Ektiğini biçmek sadece tarımın değil, evrensel adaletin de kanunudur.” — **Cicero**'
        ]
    },
    'askeri_bilimler_ve_savunma_teknolojileri': {
        'title': '⚔️ Savunma Sanayii, Harp Doktrini & Askeri Strateji',
        'quotes': [
            '“En büyük zafer, savaşmadan kazanılan zaferdir; strateji kuvvetten, akıl silahtan üstündür.” — **Sun Tzu**',
            '“Savaş, siyasetin başka araçlarla devamıdır; hazırlıklı olan milletler barışın teminatıdır.” — **Carl von Clausewitz**',
            '“Cesaret tehlike karşısında aklın sükunetini korumasıdır.” — **Plutarkhos**'
        ]
    },
    'hukuk_bilimi': {
        'title': '⚖️ Adalet, Hukuk Kuramı & Yasal Düzen',
        'quotes': [
            '“Adalet mülkün temelidir; hukukun bittiği yerde tiranlık, karmaşa ve haksızlık başlar.” — **John Locke**',
            '“Devletin nihai amacı özgürlüktür; adalet ise o özgürlüğün koruyucu kalkanıdır.” — **Baruch Spinoza**',
            '“Hukuk, aklın tutkulardan arınmış sesidir.” — **Aristoteles**'
        ]
    },
    'ilahiyat_ve_din': {
        'title': '📚 İlahiyat, Dinler Tarihi & Karşılaştırmalı Felsefe',
        'quotes': [
            '“İlim ilim bilmektir, ilim kendin bilmektir; sen kendini bilmezsin, ya nice okumaktır.” — **Yunus Emre**',
            '“Aklını kullanmayanların üzerine pislik yağar.” — **Yunus Suresi, 100**',
            '“Hakikat nereden gelirse gelsin onu kabul etmek gerekir; hakikatten daha değerli bir şey yoktur.” — **El-Kindî**'
        ]
    },
    'on_lisans_programlari': {
        'title': '📋 Mesleki Yüksekokul & Uygulamalı Teknik Disiplinler',
        'quotes': [
            '“Uygulamaya dökülmeyen bilgi bir yüktür; maharet ve teknik ustalık teorinin can damarıdır.” — **El-Cezerî**',
            '“Bir işi iyi yapmak, ona ruhunu ve emeğini katmak demektir.” — **Ahi Evran**',
            '“Bana anlatırsan unuturum, gösterirsen hatırlarım, yaptırırsan anlarım.” — **Konfüçyüs**'
        ]
    },
    'ozel_arastirma_alanlari': {
        'title': '🔬 Özel Araştırma, Füzyon & Sınır Disiplinler',
        'quotes': [
            '“Geleceği tahmin etmenin en emin yolu, onu bizzat icat etmektir.” — **Alan Kay**',
            '“Hayal gücü bilgiden daha önemlidir; çünkü bilgi sınırlıyken hayal gücü tüm dünyayı kucaklar.” — **Albert Einstein**',
            '“Sadece sınırları aşmayı göze alanlar, ne kadar ileri gidebileceklerini keşfedebilirler.” — **T. S. Eliot**'
        ]
    },
    'kariyer_ve_sertifikasyonlar': {
        'title': '🚀 Kariyer, Portfolyo, Standartlar & Sertifikasyon',
        'quotes': [
            '“Şans, yalnızca hazırlıklı ve yetkin zihinlere güler; profesyonel ustalık kesintisiz inşa edilir.” — **Louis Pasteur**',
            '“Kalite bir eylem değil, bir alışkanlıktır.” — **Will Durant (Aristoteles yorumu)**',
            '“Yaptığınız işi mükemmel yapın; öyle ki insanlar sizi görmezden gelemesin.” — **Steve Martin**'
        ]
    },
    'meta_yetkinlikler_ve_gelisim': {
        'title': '🧠 Meta-Zihin, Otonom İrade & Bilişsel Disiplin',
        'quotes': [
            '“Düşünceleriniz ne ise hayatınız da odur; kendi zihnini yöneten, tüm dünyaya yön verir.” — **Marcus Aurelius**',
            '“İnsanın en büyük zaferi, kendi nefsine ve zaaflarına karşı kazandığı zaferdir.” — **Platon**',
            '“Rüzgarın yönünü değiştiremezsiniz, ancak yelkenlerinizi hedefinize göre ayarlayabilirsiniz.” — **Epiktetos**'
        ]
    },
    'genel': {
        'title': '📂 Genel Metodoloji, Arşiv & Ortak Alanlar',
        'quotes': [
            '“Bütün büyük işler, küçük ve disiplinli adımların kararlılıkla bir araya gelmesiyle gerçekleşir.” — **Vincent van Gogh**',
            '“Damlayan su taşı deler; gücünden değil, sürekliliğinden.” — **Ovidius**',
            '“Yolculuğun kendisi varış noktasından daha öğreticidir.” — **Konfüçyüs**'
        ]
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
### *Evrensel Akademik İşletim Sistemi & Solopreneur Bilgi Mimarisi* 🌐🧬🏗️

[![Versiyon](https://img.shields.io/badge/%C3%87EK%C4%B0RDEK-v4.5--ULTIMATE-00A9E0?style=for-the-badge&logo=target)](./)
[![Mimar](https://img.shields.io/badge/M%C4%B0MAR-Yunus_%C3%87etin-D4AF37?style=for-the-badge&logo=codeforces&logoColor=white)](https://github.com/arch-yunus)
[![Repo](https://img.shields.io/badge/REPO-university--courses-black?style=for-the-badge&logo=github)](https://github.com/bahattinyunus/university-courses)
[![Kapsam](https://img.shields.io/badge/KAPSAM-{total_depts}_Disiplin-18453B?style=for-the-badge&logo=rocket)](./SUMMARY.md)
[![Kademeler](https://img.shields.io/badge/KADEMELER-{total_tiers}_Mod%C3%BCl-6f42c1?style=for-the-badge&logo=diagram)](./SUMMARY.md)

---

> *“Eğer daha uzağı görebildiysem, bu benden önceki devlerin omuzlarında durduğum içindir.”*  
> — **Sir Isaac Newton**

> *“İlim cesaret ister; cehaletin karanlığını sadece hakikatin sarsılmaz ışığı dağıtabilir.”*  
> — **El-Farabi**

> *“Basitlik, en üst düzeydeki gelişmişliktir.”*  
> — **Leonardo da Vinci**

---

## 📜 EVRENSEL AKIL VE BİREYSEL EGEMENLİK MANİFESTOSU

**University Courses (UC)**; sıradan bir ders notu arşivi veya pasif bir dokümantasyon havuzu değildir. **Yüksek Kaldıraçlı Bireyin (Solopreneur Polymath) Zihinsel Karargâhı ve Evrensel Bilgi İşletim Sistemi**dir.

Bilginin hızla çoğaldığı ama derinliğin ve sentez gücünün aşındığı modern çağda, asıl üstünlük bilginin miktarında değil; onun **bütüncül kavranışında, felsefi temellendirilişinde ve somut üretime dönüştürülme mimarisindedir.**

Eğitimi tek tip kalıpların ve hantal duvarların ötesine taşıyarak; **İslam Altın Çağı'nın polimatik dehasını, Rönesans'ın evrensel merakını ve modern bilişim çağının yüksek teknoloji disiplinini** tek bir epistemik çatı altında birleştiriyoruz.

---

## 🏛️ BÜYÜK DÜŞÜNÜRLER VE POLİMATLAR PANTEONU (THE POLYMATH PANTHEON)

> *“Bütün bilimler birbirine bağlıdır; biri tam kavranmadan diğeri hakkıyla anlaşılamaz.”* — **Roger Bacon**

### 1. 🧪 Bilim, Matematik ve Doğa Felsefesi
*   > *“Matematik, doğanın gizli kalmış armonisini insan aklına tercüme eden ilahi dildir.”* — **Leonhard Euler**
*   > *“Doğa kanunları öylesine kusursuz bir simetriye sahiptir ki, onları keşfetmek adeta bir ibadettir.”* — **Johannes Kepler**
*   > *“Fizikte önemli olan gerçeği bulmaktır, popüler olanı değil.”* — **Richard Feynman**
*   > *“Evren, matematiksel bir düşünceden ibarettir.”* — **Sir James Jeans**
*   > *“Bir kuramın güzelliği, onun doğruluğunun en güçlü kanıtıdır.”* — **Paul Dirac**

### 2. 👁️ Epistemoloji, Mantık ve Zihin Mimarisi
*   > *“Zihin doldurulacak bir kap değil, tutuşturulacak bir meşaledir.”* — **Plutarkhos**
*   > *“Mantık, aklı hataya düşmekten koruyan bir terazi ve hakikatin mihenk taşıdır.”* — **İbn-i Sînâ**
*   > *“Aklını kullanma cesaretini göster! (Sapere Aude!)”* — **Immanuel Kant**
*   > *“Şüphe etmek düşünmektir; düşünmek ise var olmaktır.”* — **René Descartes**
*   > *“Dilimin sınırları, zihnimin evrenidir.”* — **Ludwig Wittgenstein**

### 3. ⚙️ Mühendislik, Sibernetik ve Hesaplama Zekası
*   > *“Makineler düşünebilir mi sorusu, denizaltılar yüzebilir mi sorusu kadar anlamsızdır.”* — **Edsger W. Dijkstra**
*   > *“Geleceği tahmin etmeye çalışma; geleceği kodla ve inşa et.”* — **Alan Kay**
*   > *“Entelektüel bir problemi çözmenin ilk adımı, onu çözülebilir alt bileşenlerine ayırmaktır.”* — **Claude Shannon**
*   > *“Mükemmellik, eklenecek bir şey kalmadığında değil, çıkarılacak bir şey kalmadığında elde edilir.”* — **Antoine de Saint-Exupéry**
*   > *“Bilgisayar bilimi, teleskopun astronomiyle ilişkisi neyse bilgisayarlarla o kadar ilgilidir; asıl mesele hesaplamanın doğasıdır.”* — **Hal Abelson**

### 4. ⚔️ Strateji, İrade ve Bilişsel Disiplin (Stoic Mastery)
*   > *“Dış olayları kontrol edemezsin, ama kendi zihnini ve tepkilerini her an kontrol edebilirsin.”* — **Marcus Aurelius**
*   > *“Zorluklar olmasaydı, insanın büyüklüğü ve iradesi nasıl ortaya çıkardı?”* — **Epiktetos**
*   > *“Planlar hiçbir şeydir, lakin planlama her şeydir.”* — **Dwight D. Eisenhower**
*   > *“Stratejisi olmayan taktik, yenilgiden önceki son gürültüdür.”* — **Sun Tzu**
*   > *“Kendine hakim olan, tüm dünyaya hakim olur.”* — **Lao Tzu**

---

## 🧠 POLİMATİK YAKLAŞIM: BİLGİYİ EPİSTEMİK SERMAYEYE DÖNÜŞTÜRMEK

Modern dünyada uzmanlaşma daraldıkça, geniş disiplinleri birbirine bağlayan "T-Tipi" ve "Pi-Tipi" polimat zihinlerin değeri katlanarak artmaktadır:

*   **Bimodal Derinlik:** Mühendisliğin ve pozitif bilimlerin *"Nasıl"*ı ile felsefe, sosyoloji ve hukukun *"Neden"*ini aynı zihinde sentezleyin.
*   **İlk Prensiplerden Akıl Yürütme (First Principles):** Problemleri ezberlenmiş kalıplarla değil, doğanın en temel aksiyomlarına inerek çözün.
*   **Fraktal Öğrenme Çemberi:** Her yeni bilgi düğümünü, mevcut kavramsal ağınıza (mental model) bağlayarak kalıcı zihinsel sermaye inşa edin.

---

## ⚙️ SİSTEMATİK YAPI: 7-KADEMELİ STANDARTLAŞTIRILMIŞ PROTOKOL (00-06)

UAOS bünyesindeki her bir bilgi düğümü, çıraklıktan bağımsız üretim ustalığına kadar uzanan 7 kademeli bir omurga ile yönetilir:

> [!TIP]
> **Bilişsel Yolculuk:** `Veri ➔ Enformasyon ➔ Kuram ➔ Pratik ➔ İleri Uzmanlık ➔ AR-GE / Sentez ➔ Bağımsız Üretim`.

```mermaid
graph LR
    A["00: Hazırlık & Dil"] --> B["01: Teorik Temeller"]
    B --> C["02: Alan Dersleri"]
    C --> D["03: İleri Uzmanlık"]
    D --> E["04: AR-GE & Sentez"]
    E --> F["05: Akademik Kariyer"]
    F --> G["06: Standartlar & Hakimiyet"]
    style A fill:#00A9E0,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#D4AF37,stroke:#333,stroke-width:2px,color:#000
```

1. **`00 — Akademik Hazırlık ve Dil`**: Terminoloji, metodolojik kurulum ve küresel dil yetkinliği.
2. **`01 — Temel Bilimler ve Giriş`**: Aksiyomatik prensipler, doğa kanunları ve kuramsal omurga.
3. **`02 — Alan Dersleri ve Pratik`**: Disiplinin çekirdek müfredatı, laboratuvar ve problem çözümleri.
4. **`03 — Seçmeli & İleri Uzmanlık`**: Niş alanlar, derinleşme modülleri ve mikro-uzmanlıklar.
5. **`04 — Araştırma, AR-GE ve Sentez`**: Özgün projeler, açık kaynak kodlama ve Proof-of-Concept üretimi.
6. **`05 — Lisansüstü ve Akademik Kariyer`**: Literatür taraması, tez çalışmaları ve akademik yayın hazırlığı.
7. **`06 — Sertifikasyon ve Endüstriyel Standartlar`**: Uluslararası akreditasyonlar, ISO/IEEE normları ve sektörel yetkinlik.

---

## 📖 THE UNIVERSAL DISCIPLINE MATRIX ({total_depts} BÖLÜM / {total_tiers} KADEME)

Tüm akademik ve profesyonel disiplinler açık, doğrudan erişilebilir ve yapılandırılmış 3-sütunlu ızgarada listelenmiştir.

</div>

"""

    body = ""
    for folder, meta in CONTAINERS.items():
        title = meta['title']
        quotes = meta['quotes']
        container_path = os.path.join(ROOT_DIR, folder)
        if not os.path.exists(container_path):
            continue
            
        depts = sorted([d for d in os.listdir(container_path) if os.path.isdir(os.path.join(container_path, d)) and not d.startswith('.')])
        if not depts:
            continue
            
        section = f"### {title} ({len(depts)} Alan)\n\n"
        for q in quotes:
            section += f"> *{q}*\n\n"
        
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

## 🧠 SİSTEMATİK ÖĞRENME METODOLOJİLERİ
Bu kütüphanedeki verimi en üst düzeye çıkarmak için kanıtlanmış bilişsel metodolojileri uygulayın:

*   **Zettelkasten ve Bağlamsal Düşünce:** Notlarınızı izole depolamak yerine birbirine bağlayarak disiplinlerarası yeni fikirler üretin.
*   **Feynman Tekniği:** Bir konuyu gerçekten anlamak için, onu en temel diliyle ve analojilerle basitleştirerek açıklayın.
*   **Aralıklı Tekrar (Spaced Repetition):** Belleğin unutma eğrisini yenmek için bilgiyi düzenli aralıklarla geri çağırın.
*   **İlk Prensiplerden Çözümleme (First Principles):** Karmaşık sistemleri en temel doğrularına indirgeyip sıfırdan inşa edin.

---

## 🗺️ PROJE YOL HARİTASI (ROADMAP)

- [x] **Faz 1:** Temel mühendislik ve bilim disiplinlerinin 7-kademeli iskeletinin oluşturulması.
- [x] **Faz 2:** Universal Discipline Matrix ({total_depts} Akademik Alan / {total_tiers} Kademe) entegrasyonu.
- [x] **Faz 3:** CI/CD otomatik repo bütünlüğü ve indeks doğrulama test hattı.
- [ ] **Faz 4:** İnteraktif navigasyon araçları ve arama indeksleyicileri.
- [ ] **Faz 5:** Uluslararası çok dilli akademik genişleme.

---

## ❓ SIKÇA SORULAN SORULAR (SSS)

**S: Neden bu kadar geniş ve çok disiplinli bir yapı kuruldu?**  
**C:** Çünkü gerçek dünya ve çığır açan keşifler tek bir alana sıkışmış değildir. Tıbbı yapay zekayla, hukuku bilişimle, mühendisliği felsefeyle sentezleyebilen zihinler geleceği inşa edecektir.

**S: İçerikler tamamen açık kaynak ve ücretsiz mi?**  
**C:** Evet, tüm sistem **MIT Lisansı** altında korunmakta olup, bilgiye erişim evrensel bir insanlık hakkıdır.

---

## 🤝 KATKIDA BULUNMA
Bu kütüphane kolektif aklın ve açık bilimin bir tezahürü olarak büyümektedir. Katkı sağlamak için [CONTRIBUTING.md](./CONTRIBUTING.md) rehberini inceleyebilir ve Pull Request gönderebilirsiniz. Topluluk normları için [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) belgesine bakabilirsiniz.

---

## ⚖️ YASAL YÖNETİŞİM VE LİSANS
Bu proje **MIT Lisansı** altında lisanslanmıştır. Bilgi insanlığın ortak mirasıdır. Detaylar için [LICENSE](./LICENSE) dosyasına göz atabilirsiniz.

**Mimari ve Tasarım**  
### Bahattin Yunus Çetin  
*Yazılım Mühendisi & Araştırmacı*

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
        
    print(f"README.md generated successfully. Total: {total_depts} depts, {total_tiers} tiers in 3-column open grid with rich quotes.")

if __name__ == "__main__":
    generate_encyclopedic_readme()
