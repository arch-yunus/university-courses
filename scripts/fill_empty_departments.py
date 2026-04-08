# -*- coding: utf-8 -*-
"""
fill_empty_departments.py
Her boş/eksik README'li bölüm ve alt klasörü için uygun README.md dosyaları oluşturur.
"""

import os

ROOT = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"

# ─────────────────────────────────────────────────────────────────────────────
# BÖLÜM TANIMLARI
# Her kayıt: (klasör_adı, emoji, başlık, kısa_açıklama, temel_dersler, araçlar, kariyer)
# ─────────────────────────────────────────────────────────────────────────────

DEPARTMENTS = {
    "alman_dili_ve_edebiyati": {
        "emoji": "🇩🇪",
        "title": "Alman Dili ve Edebiyatı",
        "desc": "Almanca dil yapısı, edebiyat tarihi, kültürel çalışmalar ve çeviri becerileri.",
        "dersler": [
            "Alman Dil Bilgisi (Gramer I-II-III)",
            "Alman Edebiyatı Tarihi (Orta Çağ – Günümüz)",
            "Çeviri Teknikleri (Almanca-Türkçe)",
            "Almanca Akademik Yazım",
            "Alman Kültürü ve Medeniyeti",
            "Karşılaştırmalı Edebiyat",
            "Sözlü İletişim ve Sunum Becerileri",
            "Yeni Alman Edebiyatı",
        ],
        "araclar": [
            ("Sözlük / Referans", "DUDEN, Langenscheidt, LEO Online"),
            ("Gramer Analiz", "Tiger Corpus, GermaNet"),
            ("Çeviri", "DeepL, SDL Trados, memoQ"),
            ("Akademik", "JSTOR, dblp, ZDB"),
        ],
        "kariyer": [
            "Almanca Öğretmeni / Akademisyen",
            "Çevirmen / Tercüman (Hukuk, Teknik, Edebi)",
            "Uluslararası İlişkiler Uzmanı",
            "Kültür Elçisi / Diplomatik Personel",
            "Editör / Yayıncılık",
            "Turizm Rehberi (Almanca)",
        ],
        "trendler": [
            "Yapay Zekâ Destekli Çeviri Sistemleri",
            "Dijital Beşerî Bilimler (Digital Humanities)",
            "Post-kolonyal Alman Edebiyatı Araştırmaları",
            "Çok Dilli Doğal Dil İşleme (NLP)",
        ],
    },
    "arap_dili_ve_edebiyati": {
        "emoji": "🌙",
        "title": "Arap Dili ve Edebiyatı",
        "desc": "Arap dili grameri, klasik ve modern Arap edebiyatı, İslam medeniyeti ve Kur'an dili.",
        "dersler": [
            "Arap Dil Bilgisi (Sarf ve Nahiv I-IV)",
            "Klasik Arap Edebiyatı",
            "Modern Arap Edebiyatı",
            "Kur'ân Dili ve Üslubu",
            "Çeviri Teknikleri (Arapça-Türkçe)",
            "Arap Kültürü ve Medeniyeti",
            "Arap Belağati (Beyan, Meani, Bedi)",
            "Mukayeseli Edebiyat",
        ],
        "araclar": [
            ("Sözlük / Referans", "Lisan al-Arab, Al-Munjid, ArabiCorpus"),
            ("Dil Analiz", "Quranic Arabic Corpus, BAMA"),
            ("Çeviri", "Araçlar: ATA, Trados (Arapça desteği)"),
            ("Akademik", "Al-Maktaba Al-Shamela, JSTOR"),
        ],
        "kariyer": [
            "Arapça Öğretmeni / Akademisyen",
            "Çevirmen / Mütercim",
            "Diplomat / Dışişleri Uzmanı",
            "İslam Araştırmacısı / Akademisyen",
            "Uluslararası Kuruluş Uzmanı (BM, OIC)",
            "Medya / Gazetecilik (Arapça Yayın)",
        ],
        "trendler": [
            "Arap NLP ve Yapay Zekâ Uygulamaları",
            "Dijital Arşivleme ve Klasik Metin Analizi",
            "Post-kolonyal Arap Edebiyatı",
            "İkidilli Eğitim Modelleri",
        ],
    },
    "fransiz_dili_ve_edebiyati": {
        "emoji": "🇫🇷",
        "title": "Fransız Dili ve Edebiyatı",
        "desc": "Fransız dili, klasik ve çağdaş Fransız edebiyatı, Frankofon kültür ve çeviri.",
        "dersler": [
            "Fransızca Dil Bilgisi (Gramer I-IV)",
            "Fransız Edebiyatı Tarihi (17. yy – Günümüz)",
            "Frankofon Edebiyat",
            "Çeviri Teknikleri (Fransızca-Türkçe)",
            "Fransız Kültürü ve Medeniyeti",
            "Akademik Yazım ve Araştırma",
            "Karşılaştırmalı Edebiyat",
            "Sözlü Dil ve Sunum Becerileri",
        ],
        "araclar": [
            ("Sözlük / Referans", "Le Petit Robert, Larousse, CRISCO"),
            ("Gramer / Analiz", "Frantext, TreeTagger"),
            ("Çeviri", "SDL Trados, memoQ, WordFast"),
            ("Akademik", "Cairn.info, Persée, Gallica (BnF)"),
        ],
        "kariyer": [
            "Fransızca Öğretmeni / Akademisyen",
            "Çevirmen / Editör",
            "Diplomatik Personel / Konsolosluk",
            "Kültür Elçisi (Alliance Française)",
            "Uluslararası İlişkiler Uzmanı",
            "Turizm Rehberi (Fransızca)",
        ],
        "trendler": [
            "Frankofon Diaspora Edebiyatı",
            "Dijital Beşerî Bilimler",
            "NLP ve Fransızca Dil Modelleri (CamemBERT)",
            "Kültürel Miras Dijitalleştirme",
        ],
    },
    "gastronomi_ve_mutfak_sanatlari": {
        "emoji": "🍽️",
        "title": "Gastronomi ve Mutfak Sanatları",
        "desc": "Mutfak teknolojisi, gıda kültürü, şeflik sanatı, gastronomi yönetimi ve beslenme.",
        "dersler": [
            "Temel Mutfak Teknikleri",
            "Pastacılık ve Fırıncılık",
            "Türk Mutfak Kültürü",
            "Dünya Mutfakları",
            "Menü Planlama ve Maliyet Analizi",
            "Gıda Güvenliği ve Hijyen (HACCP)",
            "Gastronomi Yönetimi",
            "Oenoloji ve İçecek Yönetimi",
        ],
        "araclar": [
            ("Mutfak Ekipman", "Sous Vide, Salamander, Combi Oven"),
            ("Yazılım", "Gastrofix, Oracle MICROS, FoodCost Pro"),
            ("Sertifikasyon", "HACCP, ServSafe, ISO 22000"),
            ("Ar-Ge", "Modernist Cuisine Teknikleri, Molecular Gastronomy"),
        ],
        "kariyer": [
            "Executive Chef / Mutfak Şefi",
            "Pastane Şefi (Pâtissier)",
            "Restoran / Otel F&B Yöneticisi",
            "Gastronomi Danışmanı",
            "Gıda Yazarı / Blogger",
            "Ürün Geliştirme Uzmanı (FMCG)",
        ],
        "trendler": [
            "Plant-Based ve Sürdürülebilir Mutfak",
            "Fermentasyon ve Probiyotik Odaklı Gastronomi",
            "Dijital Menü ve AI Destekli Tarif Geliştirme",
            "Dark Kitchen ve Cloud Restaurant Modelleri",
        ],
    },
    "gazetecilik": {
        "emoji": "📰",
        "title": "Gazetecilik",
        "desc": "Haber yazımı, medya etiği, gazetecilik tarihi, dijital medya ve araştırmacı gazetecilik.",
        "dersler": [
            "Haber Yazımı ve Editörlük",
            "Gazetecilik Tarihi ve Etiği",
            "Araştırmacı Gazetecilik",
            "Fotoğraf ve Görsel Habercilik",
            "Dijital ve Çevrimiçi Gazetecilik",
            "Medya Ekonomisi ve İşletmeciliği",
            "Radyo ve Televizyon Haberciliği",
            "Veri Gazeteciliği",
        ],
        "araclar": [
            ("İçerik Üretim", "Adobe Premiere, Audacity, DaVinci Resolve"),
            ("Veri Analiz", "Datawrapper, Flourish, QGIS"),
            ("CMS", "WordPress, Arc Publishing, Drupal"),
            ("Kaynak Doğrulama", "InVID, TinEye, BellingCat araçları"),
        ],
        "kariyer": [
            "Muhabir / Editör",
            "Veri Gazetecisi",
            "Dijital Medya Yöneticisi",
            "Medya Danışmanı / Halkla İlişkiler",
            "Belgesel Yapımcısı",
            "Araştırmacı Gazeteci (Investigative)",
        ],
        "trendler": [
            "Yapay Zekâ ile Otomasyon Gazetecilik",
            "Newsletter ve Bağımsız Medya Modelleri",
            "Dezenformasyon ile Mücadele Teknolojileri",
            "Mobil Gazetecilik (MoJo)",
        ],
    },
    "halkla_iliskiler_ve_reklamcilik": {
        "emoji": "📣",
        "title": "Halkla İlişkiler ve Reklamcılık",
        "desc": "Kurumsal iletişim, marka yönetimi, reklam stratejileri, dijital pazarlama ve kriz iletişimi.",
        "dersler": [
            "Halkla İlişkiler Teorisi ve Uygulaması",
            "Reklam Teorisi ve Yaratıcılık",
            "Marka Yönetimi",
            "Kurumsal İletişim",
            "Dijital Pazarlama ve Sosyal Medya",
            "Kriz İletişimi Yönetimi",
            "Medya Planlaması",
            "İletişim Araştırmaları ve Analizi",
        ],
        "araclar": [
            ("Sosyal Medya", "Hootsuite, Buffer, Sprout Social"),
            ("Analitik", "Google Analytics 4, Semrush, Brandwatch"),
            ("Tasarım", "Adobe Creative Suite, Canva Pro"),
            ("CRM", "HubSpot, Salesforce Marketing Cloud"),
        ],
        "kariyer": [
            "Halkla İlişkiler Uzmanı / Müdürü",
            "Marka ve Pazarlama Yöneticisi",
            "Dijital Pazarlama Uzmanı",
            "Kurumsal İletişim Direktörü",
            "Sosyal Medya Yöneticisi",
            "Reklam Ajansı Yaratıcı Direktörü",
        ],
        "trendler": [
            "Influencer Marketing ve Mikro-Influencer Stratejileri",
            "AI Destekli İçerik Üretimi",
            "Programatik Reklam ve Kitle Hedefleme",
            "Kurumsal ESG İletişimi ve Sürdürülebilirlik",
        ],
    },
    "ilahiyat": {
        "emoji": "🕌",
        "title": "İlahiyat",
        "desc": "İslam ilahiyatı, Kur'an-ı Kerim bilimleri, hadis, fıkıh, kelam, tasavvuf ve din felsefesi.",
        "dersler": [
            "Kur'an-ı Kerim Tilâveti ve Tecvid",
            "Tefsir Usulü ve Tefsir",
            "Hadis Usulü ve Hadis",
            "Fıkıh Usulü ve İslam Hukuku",
            "Kelam (İslam Akait Bilimi)",
            "Tasavvuf Tarihi ve Düşüncesi",
            "İslam Tarihi ve Medeniyeti",
            "Din Felsefesi ve Karşılaştırmalı Dinler",
        ],
        "araclar": [
            ("Dini Veritabanı", "Al-Shamela, Kütüb-i Sitte Online"),
            ("Arapça Metin", "Quranic Arabic Corpus, Zekr"),
            ("Akademik", "ISAM (İslam Araştırmaları Merkezi), DergiPark"),
            ("Referans", "DIA (Diyanet İslam Ansiklopedisi)"),
        ],
        "kariyer": [
            "Din Görevlisi (İmam-Hatip)",
            "Akademisyen / İlahiyat Doktoru",
            "Din Eğitimi Uzmanı",
            "Diyanet İşleri Uzmanı",
            "Kur'an Kursu Öğreticisi",
            "Manevi Danışman / Rehber",
        ],
        "trendler": [
            "Dijital İlahiyat ve Online Din Eğitimi",
            "Çağdaş İslam Düşüncesi ve Yorum",
            "Sosyal Medyada Din Anlatımı",
            "Dinlerarası Diyalog Çalışmaları",
        ],
    },
    "ingiliz_dili_ve_edebiyati": {
        "emoji": "🇬🇧",
        "title": "İngiliz Dili ve Edebiyatı",
        "desc": "İngiliz ve Amerikan edebiyatı, dilbilim, çeviri teknikleri ve akademik İngilizce.",
        "dersler": [
            "İngilizce Dil Bilgisi ve Üslup",
            "İngiliz Edebiyatı Tarihi (Shakespeare'den Bugüne)",
            "Amerikan Edebiyatı",
            "Postkolonyal ve Dünya İngilizcesi Edebiyatı",
            "Çeviri Teorisi ve Uygulaması",
            "Dilbilim: Dil Yapısı ve İşlevi",
            "Akademik Yazım ve Araştırma",
            "Karşılaştırmalı Edebiyat",
        ],
        "araclar": [
            ("Sözlük / Referans", "Oxford English Dictionary, Merriam-Webster"),
            ("Corpus", "British National Corpus, COCA"),
            ("Çeviri", "SDL Trados, memoQ, Wordfast"),
            ("Akademik", "JSTOR, Project MUSE, Literature Online"),
        ],
        "kariyer": [
            "İngilizce Öğretmeni / Akademisyen",
            "Çevirmen / Editör (Edebi, Teknik)",
            "İçerik Yazarı / Copywriter",
            "Uluslararası İlişkiler Uzmanı",
            "Diplomatik Personel / Konsolosluk",
            "Yayınevi Editörü",
        ],
        "trendler": [
            "Yapay Zekâ ve NLP ile İngilizce Öğretimi",
            "Dijital Beşerî Bilimler",
            "Post-kolonyal ve Kimlik Edebiyatı",
            "Küresel İngilizce (World Englishes) Araştırmaları",
        ],
    },
    "konaklama_isletmeciligi": {
        "emoji": "🏨",
        "title": "Konaklama İşletmeciliği",
        "desc": "Otel yönetimi, konaklama operasyonları, misafir ilişkileri ve turizm işletme sistemleri.",
        "dersler": [
            "Otel İşletmeciliğine Giriş",
            "Ön Büro Yönetimi",
            "Yiyecek-İçecek Yönetimi",
            "Konaklama Pazarlaması",
            "Muhasebe ve Maliyet Kontrolü (Hospitality)",
            "Misafir İlişkileri ve CRM",
            "Turizm Hukuku",
            "Sürdürülebilir Turizm",
        ],
        "araclar": [
            ("PMS", "Opera PMS, Protel, RMS Cloud"),
            ("Kanal Yönetimi", "SiteMinder, Cloudbeds, OTA Insight"),
            ("Analitik", "RevPAR hesaplama, STR Report, Duetto"),
            ("CRM", "Salesforce Hospitality, Revinate"),
        ],
        "kariyer": [
            "Otel Genel Müdürü",
            "Ön Büro ve Misafir İlişkileri Direktörü",
            "Revenue Manager",
            "F&B (Yiyecek-İçecek) Müdürü",
            "Turizm Danışmanı",
            "Otelcilik Girişimcisi",
        ],
        "trendler": [
            "Akıllı Otel Teknolojileri (IoT, AI Concierge)",
            "Sürdürülebilir ve Eko-Yeşil Konaklama",
            "Deneyim Ekonomisi ve Kişiselleştirme",
            "Dijital Check-in / Contactless Teknolojiler",
        ],
    },
    "mutercim_ve_tercumanlik": {
        "emoji": "🌐",
        "title": "Mütercim ve Tercümanlık",
        "desc": "Yazılı ve sözlü çeviri, konferans tercümanlığı, terminoloji yönetimi ve çeviri teknolojisi.",
        "dersler": [
            "Çeviri Teorisi ve Yöntemleri",
            "Edebi Çeviri",
            "Teknik ve Uzmanlaşmış Çeviri (Hukuk, Tıp, Teknik)",
            "Konsekutif ve Simultane Tercümanlık",
            "Terminoloji ve Sözlük Bilimi",
            "Bilgisayar Destekli Çeviri (CAT Araçları)",
            "Yerelleştirme (Localization)",
            "Çeviri Kalite Güvencesi",
        ],
        "araclar": [
            ("CAT Araçları", "SDL Trados Studio, memoQ, OmegaT"),
            ("Terminoloji", "TermBase, MultiTerm, Termium"),
            ("MT / NMT", "DeepL, ModernMT, eTranslation (EU)"),
            ("Yorumlama", "Interprefy, KUDO, Zoom Interpretation"),
        ],
        "kariyer": [
            "Serbest Çevirmen",
            "Konferans Tercümanı",
            "Yerelleştirme Uzmanı",
            "Terminolog",
            "Çeviri Proje Yöneticisi",
            "Yeminli Tercüman (Mahkeme vb.)",
        ],
        "trendler": [
            "Yapay Zekâ ile Makine Çevirisi Kalitesi",
            "Post-Editing ve İnsan-Makine İş Birliği",
            "Video Oyun Yerelleştirme",
            "İşaret Dili Çevirmenliği",
        ],
    },
    "radyo_televizyon_ve_sinema": {
        "emoji": "🎬",
        "title": "Radyo, Televizyon ve Sinema",
        "desc": "Film yapımcılığı, yayıncılık, sinema tarihi, senaryo yazımı ve görsel-işitsel medya.",
        "dersler": [
            "Sinema Tarihi ve Kuramı",
            "Senaryo Yazımı",
            "Film Yönetmenliği ve Yapım",
            "Görüntü Yönetmenliği / Sinematografi",
            "Film Müziği ve Ses Tasarımı",
            "Post-Prodüksiyon ve Kurgu",
            "Televizyon Programcılığı ve Yapım",
            "Animasyon ve Dijital Medya",
        ],
        "araclar": [
            ("Kurgu", "Adobe Premiere Pro, DaVinci Resolve, Avid Media Composer"),
            ("VFX / CG", "Adobe After Effects, Blender, Nuke"),
            ("Ses", "Pro Tools, Logic Pro, Audacity"),
            ("Senaryo", "Final Draft, Highland 2, WriterDuet"),
        ],
        "kariyer": [
            "Film Yönetmeni / Yapımcı",
            "Senarist",
            "Görüntü Yönetmeni (DoP)",
            "Televizyon Program Yapımcısı",
            "Kurgu Sanatçısı",
            "YouTube / Dijital İçerik Yapımcısı",
        ],
        "trendler": [
            "Streaming Platformları ve Özgün İçerik (Netflix, Disney+)",
            "AI ile Yapay Zekâ Destekli Senaryo ve VFX",
            "Dikey Video ve Kısa Form İçerik (TikTok, Reels)",
            "Sanal Üretim (LED Volume / Unreal Engine)",
        ],
    },
    "rehberlik_ve_psikolojik_danismanlik": {
        "emoji": "🧠",
        "title": "Rehberlik ve Psikolojik Danışmanlık",
        "desc": "Psikolojik danışmanlık teorileri, bireysel ve grup terapisi, okul rehberliği ve kariyer danışmanlığı.",
        "dersler": [
            "Psikolojik Danışmanlık Teorileri",
            "Psikolojik Değerlendirme ve Test",
            "Bireysel ve Grup Psikolojik Danışma",
            "Okul Psikolojik Danışmanlığı",
            "Kariyer Danışmanlığı",
            "Crisis Intervention (Kriz Müdahalesi)",
            "Çocuk ve Ergen Psikolojisi",
            "Araştırma Yöntemleri (Psikoloji)",
        ],
        "araclar": [
            ("Ölçme", "MMPI-2, Beck BDI, Raven Matrisler, WISC-IV"),
            ("Terapi Yöntemleri", "CBT, EMDR, DBT, ACT"),
            ("Platform", "TheraNest, SimplePractice, Woebot (AI)"),
            ("Veri Analiz", "SPSS, R (psych paket)"),
        ],
        "kariyer": [
            "Okul Psikolojik Danışmanı",
            "Klinik Psikolog (Lisansüstü ile)",
            "İK Uzmanı / Kariyer Danışmanı",
            "Eğitim Psikoloğu",
            "Online Terapi Platformu Uzmanı",
            "Araştırmacı / Akademisyen",
        ],
        "trendler": [
            "Teleterapi ve Dijital Akıl Sağlığı Platformları",
            "Yapay Zekâ Destekli Ruh Sağlığı Tarama",
            "Travma Bilinçli Bakım (Trauma-Informed Care)",
            "Pozitif Psikoloji ve Dayanıklılık Programları",
        ],
    },
    "rus_dili_ve_edebiyati": {
        "emoji": "🇷🇺",
        "title": "Rus Dili ve Edebiyatı",
        "desc": "Rus dili grameri, Rus edebiyatı tarihi, Slavistik, çeviri ve Rus kültürü.",
        "dersler": [
            "Rusça Dil Bilgisi (Fonetik, Morfoloji, Sözdizimi)",
            "Rus Edebiyatı Tarihi (Puşkin'den Tolstoy'a)",
            "Modern Sovyet ve Post-Sovyet Edebiyatı",
            "Çeviri Teknikleri (Rusça-Türkçe)",
            "Rus Kültürü ve Medeniyeti",
            "Slavistik Araştırmalar",
            "Akademik Rusça Yazım",
            "Karşılaştırmalı Edebiyat",
        ],
        "araclar": [
            ("Sözlük", "Ozhegov, Ushakov, Multitran"),
            ("Corpus", "Russian National Corpus (RNC)"),
            ("Çeviri", "PROMT, SDL Trados (Rusça desteği)"),
            ("Akademik", "eLIBRARY.ru, Cyberleninka"),
        ],
        "kariyer": [
            "Rusça Öğretmeni / Akademisyen",
            "Çevirmen / Diplomat",
            "Enerji Sektörü Uzmanı (Rusya İlişkileri)",
            "Turizm Rehberi (Rusça)",
            "Uluslararası Ticaret Uzmanı",
            "Medya / Gazetecilik (Rusça)",
        ],
        "trendler": [
            "Post-Sovyet Edebiyatı ve Kimlik Çalışmaları",
            "Dijital Beşerî Bilimler (Rus korpus çalışmaları)",
            "Eurasian Studies ve Jeopolitik Araştırma",
            "Rusça NLP Modelleri (ruBERT)",
        ],
    },
    "turizm_isletmeciligi": {
        "emoji": "✈️",
        "title": "Turizm İşletmeciliği",
        "desc": "Turizm sektörü yönetimi, seyahat acenteciliği, destinasyon yönetimi ve turizm politikası.",
        "dersler": [
            "Turizmde Girişimcilik ve İşletmecilik",
            "Seyahat Acenteciliği ve Tur Operatörlüğü",
            "Destinasyon Yönetimi ve Pazarlama",
            "Turizm Ekonomisi",
            "Otelcilik ve Konaklama Yönetimi",
            "Turizm Hukuku ve Mevzuatı",
            "Sürdürülebilir Turizm",
            "Kongre ve Etkinlik Turizmi (MICE)",
        ],
        "araclar": [
            ("GDS", "Amadeus, Sabre, Galileo"),
            ("OTA / Rezervasyon", "Booking.com Manager, Expedia Partner, Airbnb"),
            ("Analitik", "Siteminder, OTA Insight, STR Global"),
            ("Yönetim", "TourCMS, Rezdy, Checkfront"),
        ],
        "kariyer": [
            "Tur Operatörü / Seyahat Acentesi Yöneticisi",
            "Destinasyon Yönetim Örgütü (DMO) Uzmanı",
            "Otel Genel Müdürü",
            "MICE Etkinlik Yöneticisi",
            "Turizm Politikası Analisti",
            "Girişimci / Turizm Startup Kurucusu",
        ],
        "trendler": [
            "Dijital Turizm ve Metaverse Seyahat",
            "Sürdürülebilir ve Sorumlu Turizm",
            "AI Destekli Seyahat Planlaması",
            "Sağlık Turizmi ve Medikal Travel",
        ],
    },
    "turizm_rehberligi": {
        "emoji": "🗺️",
        "title": "Turizm Rehberliği",
        "desc": "Profesyonel tur rehberliği, Türkiye tarihi ve kültürü, müzecilik ve turist ilişkileri.",
        "dersler": [
            "Türkiye Tarihi ve Uygarlıkları",
            "Türk Sanatı ve Mimarisi",
            "Turizm Rehberliği Teknikleri",
            "Yabancı Dil (İngilizce / Almanca / Rusça)",
            "Müzecilik ve Kültürel Miras",
            "Turizm Mevzuatı ve Etik",
            "İletişim Becerileri ve Sunum",
            "Coğrafya ve Doğal Miras",
        ],
        "araclar": [
            ("Lisanslama", "TUREB (Türkiye Rehberler Birliği) sistemi"),
            ("Uygulama", "izi.TRAVEL, GPSmyCity, Google Arts & Culture"),
            ("Dil", "Google Translate, DeepL, SayHi"),
            ("Tur Yönetimi", "TourCMS, Rezdy, EzTix"),
        ],
        "kariyer": [
            "Profesyonel Turist Rehberi (Türkiye Kartı)",
            "Kültürel Miras Uzmanı",
            "Müze Rehberi",
            "Özel Tur Şirketi Kurucusu",
            "Turizm Danışmanı",
            "Dijital Turizm İçerik Üreticisi",
        ],
        "trendler": [
            "Dijital Tur Rehberliği (VR/AR Turlar)",
            "Sorumlu Turizm ve Eko-Rehberlik",
            "Kültürel İklim ve UNESCO Süreçleri",
            "Sosyal Medya ile Hedef Kitleye Ulaşım",
        ],
    },
    "turk_dili_ve_edebiyati": {
        "emoji": "📜",
        "title": "Türk Dili ve Edebiyatı",
        "desc": "Türk dili grameri, klasik ve modern Türk edebiyatı, Türkoloji ve dil tarihi.",
        "dersler": [
            "Eski Türkçe (Köktürk, Uygur Dönemi)",
            "Orta Türkçe (Karahanlı, Harezm, Çağatay)",
            "Osmanlı Türkçesi",
            "Türkiye Türkçesi Dil Bilgisi",
            "Türk Halk Edebiyatı",
            "Divan Edebiyatı",
            "Tanzimat'tan Günümüze Türk Edebiyatı",
            "Türk Dili Tarihi ve Diyalektoloji",
        ],
        "araclar": [
            ("Sözlük", "TDK Sözlüğü (sözlük.gov.tr), Nişanyan Sözlük"),
            ("Corpus", "Turkish National Corpus, Sketch Engine Turkish"),
            ("Akademik", "DergiPark, ASOS İndeks, TÜBİTAK ULAKBİM"),
            ("Osmanlıca", "Osmanlıca-Türkçe Sözlük, OSAD"),
        ],
        "kariyer": [
            "Türkçe Öğretmeni",
            "Akademisyen / Türkolog",
            "Editör / Yazar",
            "Yayınevi Redaktörü",
            "Devlet Kurumlarında Dil Uzmanı (TDK vb.)",
            "Çevirmen",
        ],
        "trendler": [
            "Dijital Türkoloji ve Metin Arşivleme",
            "Türkçe NLP Modelleri (BERTurk)",
            "Osmanlı Arşivlerinin Dijitalleştirilmesi",
            "Kültürel Miras ve Dil Koruma",
        ],
    },
    "yeni_medya_ve_iletisim": {
        "emoji": "💡",
        "title": "Yeni Medya ve İletişim",
        "desc": "Dijital medya, sosyal ağlar, yapay zekâ ile iletişim, kullanıcı deneyimi ve dijital haber alma.",
        "dersler": [
            "Yeni Medya Kuramları",
            "Sosyal Medya İletişimi",
            "Dijital Gazetecilik",
            "İnternet Kültürü ve Kimlik",
            "Veri Gazeteciliği ve İnfografik",
            "İletişim Araştırma Yöntemleri",
            "Siber Güvenlik ve Dijital Etik",
            "Kullanıcı Deneyimi (UX) Temelleri",
        ],
        "araclar": [
            ("Analitik", "Google Analytics 4, Meta Insights, Hootsuite"),
            ("Tasarım", "Figma, Adobe XD, Canva"),
            ("Podcast / Video", "Descript, Riverside.fm, Streamyard"),
            ("Veri viz.", "Datawrapper, Flourish, Tableau Public"),
        ],
        "kariyer": [
            "Dijital İletişim Uzmanı",
            "Sosyal Medya Stratejisti",
            "UX / Dijital İçerik Tasarımcısı",
            "Veri Gazetecisi",
            "Online Platform Editörü",
            "Dijital Marka Yöneticisi",
        ],
        "trendler": [
            "Yapay Zekâ ile İçerik Üretimi ve Dezenformasyon",
            "Web 3.0 ve Merkeziyetsiz Medya",
            "Podcast ve Sesli İçerik Yükselişi",
            "XR (AR/VR/MR) ile Sürükleyici İletişim",
        ],
    },
    "yiyecek_icecek_isletmeciligi": {
        "emoji": "🍴",
        "title": "Yiyecek-İçecek İşletmeciliği",
        "desc": "Restoran yönetimi, bar ve kafe operasyonları, maliyet kontrolü, menü mühendisliği ve F&B girişimciliği.",
        "dersler": [
            "Yiyecek-İçecek İşletmeciliğine Giriş",
            "Menü Planlama ve Mühendisliği",
            "Maliyet Kontrolü (Food Cost, Labour Cost)",
            "Bar ve İçecek Yönetimi",
            "Mutfak Organizasyonu ve Üretim",
            "Gıda Güvenliği ve HACCP",
            "Pazarlama ve Müşteri Deneyimi",
            "Girişimcilik ve Restoran Açma",
        ],
        "araclar": [
            ("POS / Yönetim", "Oracle MICROS, Lightspeed, Toast POS"),
            ("Teslimat", "Yemeksepeti Partner Panel, Getir Yemek, UberEats"),
            ("Maliyet", "FoodCost Pro, Apicbase, Meez"),
            ("Pazarlama", "Google My Business, TripAdvisor, Yelp"),
        ],
        "kariyer": [
            "Restoran / Kafe Genel Müdürü",
            "F&B Direktörü (Otel / Zincir)",
            "Girişimci (Dark Kitchen, Franchise)",
            "Menü Mühendisi / Konsültan",
            "Gıda Güvenliği Uzmanı",
            "Gastronomi Blog / İçerik Üreticisi",
        ],
        "trendler": [
            "Dark Kitchen ve Ghost Restaurant Modeli",
            "Plant-Based Menu Trendleri",
            "Dijital Menü ve QR Sistemleri",
            "AI ile Dinamik Fiyatlandırma ve Stok Yönetimi",
        ],
    },
}

# Alt klasör başlıkları ve açıklamaları
SUBDIR_DEFS = {
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
}

DERS_SABLONU = """# 📝 Ders Notu Şablonu

## Ders Bilgileri
| Alan | Bilgi |
|------|-------|
| Ders Adı | *(buraya yaz)* |
| Öğretim Görevlisi | *(buraya yaz)* |
| Dönem | 20xx-20xx / Güz veya Bahar |
| Kredi | *(buraya yaz)* |

## 🎯 Dersin Amacı
*(Kısa açıklama)*

## 📚 Kaynaklar
- *(Kitap / Makale 1)*
- *(Kitap / Makale 2)*

## 📝 Notlar

### Hafta 1
...

### Hafta 2
...

## ✅ Katkı
Bu dosya kişisel not amaçlıdır. Paylaşmak için repository'e PR açabilirsin.
"""


def make_department_readme(dep_key: str, info: dict) -> str:
    emoji = info["emoji"]
    title = info["title"]
    desc = info["desc"]
    dersler = info["dersler"]
    araclar = info["araclar"]
    kariyer = info["kariyer"]
    trendler = info["trendler"]

    dersler_md = "\n".join(f"- **{d}**" for d in dersler)
    araclar_rows = "\n".join(f"| {a[0]} | {a[1]} |" for a in araclar)
    kariyer_md = "\n".join(f"- **{k}**" for k in kariyer)
    trendler_md = "\n".join(f"- **{t}**" for t in trendler)

    return f"""# {emoji} {title}

## 🎯 Amaç
{desc}

---

## 📚 Temel Dersler
{dersler_md}

---

## 🔧 Kullanılan Araçlar ve Teknolojiler
| Alan | Araçlar / Teknolojiler |
|------|------------------------|
{araclar_rows}

---

## 🚀 Kariyer Alanları
{kariyer_md}

---

## 📊 Gelecek Trendler
{trendler_md}

---

## 📂 Ders Ağacı
- [01 Temel Bilimler ve Giriş](01_Temel_Bilimler_ve_Giris/)
- [02 Alan Dersleri](02_Alan_Dersleri/)
- [03 Seçmeli & İleri Uygulama](03_Secmeli_ve_Ileri_Uygulama/)
- [04 Araştırma ve Bitirme](04_Arastirma_ve_Bitirme/)

> [!TIP]
> Yeni bir ders eklerken `DERS_SABLONU.md` dosyasını kopyalayarak ilgili alt klasörün içine koy!
"""


def make_subdir_readme(dep_key: str, dept_title: str, subdir_key: str) -> str:
    sub = SUBDIR_DEFS[subdir_key]
    return f"""# 📂 {sub['label']} — {dept_title}

## 📖 Açıklama
{sub['desc']}

---

## 📝 Bu Klasöre Nasıl Katkı Yapılır?
1. `DERS_SABLONU.md` (üst dizindeki) dosyasını bu klasöre kopyala
2. Dosyayı `DERS_ADI.md` olarak yeniden adlandır
3. İçini ders notları, ödevler ve kaynaklarla doldur
4. Pull Request aç veya doğrudan push et

> [!NOTE]
> Bu klasör **{dept_title}** bölümünün **{sub['label']}** dönemine aittir.
"""


def run():
    total_parent = 0
    total_sub = 0
    total_sablonu = 0

    for dep_key, info in DEPARTMENTS.items():
        dep_path = os.path.join(ROOT, dep_key)
        if not os.path.isdir(dep_path):
            print("[SKIP] Dir bulunamadi: " + dep_key)
            continue

        # 1) Ana README.md
        parent_readme = os.path.join(dep_path, "README.md")
        content = make_department_readme(dep_key, info)
        with open(parent_readme, "w", encoding="utf-8") as f:
            f.write(content)
        total_parent += 1
        print("[OK] " + dep_key + "/README.md")

        # 2) DERS_SABLONU.md
        sablonu_path = os.path.join(dep_path, "DERS_SABLONU.md")
        if not os.path.exists(sablonu_path):
            with open(sablonu_path, "w", encoding="utf-8") as f:
                f.write(DERS_SABLONU)
            total_sablonu += 1
            print("[OK] " + dep_key + "/DERS_SABLONU.md")

        # 3) Alt klasör README'leri
        for subdir_key, sub_info in SUBDIR_DEFS.items():
            subdir_path = os.path.join(dep_path, subdir_key)
            if not os.path.isdir(subdir_path):
                os.makedirs(subdir_path, exist_ok=True)
            sub_readme = os.path.join(subdir_path, "README.md")
            sub_content = make_subdir_readme(dep_key, info["title"], subdir_key)
            with open(sub_readme, "w", encoding="utf-8") as f:
                f.write(sub_content)
            total_sub += 1

        print("  -> 4 alt klasor README tamamlandi: " + dep_key)

    print("")
    print("=== TAMAMLANDI ===")
    print("Ana README: " + str(total_parent))
    print("Alt klasor README: " + str(total_sub))
    print("DERS_SABLONU: " + str(total_sablonu))


if __name__ == "__main__":
    run()
