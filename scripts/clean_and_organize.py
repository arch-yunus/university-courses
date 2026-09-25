import os
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def clean_dept_names():
    # Mapping substring patterns to target clean names
    dept_renames = {
        'sosyal_ve_beseri_bilimler': {
            'akt': 'aktuarya_bilimleri'
        },
        'on_lisans_programlari': {
            'bbi_ve_aromatik_bitkiler': 'tibbi_ve_aromatik_bitkiler'
        },
        'meta_yetkinlikler_ve_gelisim': {
            'zakere_ve_ikna_sanati': 'muzakere_ve_ikna_sanati',
            'sun_tzu_stratejik_d': 'sun_tzu_stratejik_dusunce',
            'stoisizm_ve_mental_dayanikl': 'stoisizm_ve_mental_dayaniklilik'
        }
    }

    for container, mapping in dept_renames.items():
        c_path = os.path.join(ROOT_DIR, container)
        if not os.path.exists(c_path):
            continue
        for d in os.listdir(c_path):
            dp = os.path.join(c_path, d)
            if not os.path.isdir(dp):
                continue
            for pattern, target in mapping.items():
                if pattern in d:
                    target_path = os.path.join(c_path, target)
                    if dp != target_path:
                        print(f"[RENAME DEPT] {dp} -> {target_path}")
                        if os.path.exists(target_path):
                            # merge
                            for item in os.listdir(dp):
                                s_item = os.path.join(dp, item)
                                d_item = os.path.join(target_path, item)
                                if not os.path.exists(d_item):
                                    shutil.move(s_item, d_item)
                            shutil.rmtree(dp)
                        else:
                            os.rename(dp, target_path)

def clean_inner_dirs():
    tier_fixes = [
        ('meta_muhendislik', 'bilgisayar_muhendisligi', '02_Alan_Dersleri', 'Veritaban', 'Veritabani_Yonetim_Sistemleri'),
        ('meta_muhendislik', 'fizik_muhendisligi', '02_Alan_Dersleri', 'Kuantum_Mekani', 'Kuantum_Mekanigine_Giris'),
        ('meta_muhendislik', 'fizik_muhendisligi', '02_Alan_Dersleri', 'Kat', 'Katihal_Fizigi'),
        ('meta_muhendislik', 'fizik_muhendisligi', '02_Alan_Dersleri', 'kleer_Fizik', 'Nukleer_Fizik_Prensipleri'),
    ]

    for container, dept, tier, pattern, target in tier_fixes:
        tier_path = os.path.join(ROOT_DIR, container, dept, tier)
        if not os.path.exists(tier_path):
            continue
        for item in os.listdir(tier_path):
            if pattern in item:
                src = os.path.join(tier_path, item)
                dst = os.path.join(tier_path, target)
                if src != dst and os.path.exists(src):
                    print(f"[RENAME TIER INNER] {src} -> {dst}")
                    if os.path.exists(dst):
                        shutil.rmtree(src)
                    else:
                        os.rename(src, dst)

def consolidate_legacy_courses():
    # Consolidate yazilim_muhendisligi legacy items into 01 and 02 tiers
    ym_path = os.path.join(ROOT_DIR, 'meta_muhendislik', 'yazilim_muhendisligi')
    if os.path.exists(ym_path):
        tier_01 = os.path.join(ym_path, '01_Temel_Bilimler_ve_Giris')
        tier_02 = os.path.join(ym_path, '02_Alan_Dersleri')
        
        move_map_01 = ['algoritma', 'iktisat']
        move_map_02 = {
            'bicimsel_diller_otamata_teorisi': 'bicimsel_diller_ve_otomata_teorisi',
            'sistem_programlama': 'sistem_programlama',
            'yazlm_tasarm_mimarisi': 'yazilim_tasarim_mimarisi',
            'iletim_sistemleri': 'isletim_sistemleri',
            'betik_diller': 'betik_diller',
            'veri_tabani': 'veri_tabani_yonetimi'
        }
        
        for item in os.listdir(ym_path):
            item_path = os.path.join(ym_path, item)
            if not os.path.isdir(item_path) or item.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_')):
                continue
            
            if item in move_map_01:
                target = os.path.join(tier_01, item)
                print(f"[CONSOLIDATE YM -> 01] {item} -> {target}")
                if os.path.exists(target):
                    shutil.rmtree(target)
                shutil.move(item_path, target)
            else:
                for k, clean_target_name in move_map_02.items():
                    if k in item or item in k:
                        target = os.path.join(tier_02, clean_target_name)
                        print(f"[CONSOLIDATE YM -> 02] {item} -> {target}")
                        if os.path.exists(target):
                            shutil.rmtree(target)
                        shutil.move(item_path, target)
                        break

    # Consolidate elektronik_ve_haberlesme_muhendisligi legacy items into 02 tier
    ehm_path = os.path.join(ROOT_DIR, 'meta_muhendislik', 'elektronik_ve_haberlesme_muhendisligi')
    if os.path.exists(ehm_path):
        tier_02 = os.path.join(ehm_path, '02_Alan_Dersleri')
        ehm_clean_names = {
            'analog_elektronik': 'analog_elektronik',
            'antenler_ve_propagasyon': 'antenler_ve_propagasyon',
            'sayisal_isaret_isleme': 'sayisal_isaret_isleme',
            'iletisim_elektronigi': 'iletisim_elektronigi',
            'elektronik_devreler': 'elektronik_devreler',
            'elektrik_motorlar': 'elektrik_motorlari',
            'say': 'sayisal_tasarim',
            'analog_haberlesme': 'analog_haberlesme',
            'r': 'goruntu_isleme'
        }
        for item in os.listdir(ehm_path):
            item_path = os.path.join(ehm_path, item)
            if not os.path.isdir(item_path) or item.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_')):
                continue
            for pat, clean_name in ehm_clean_names.items():
                if pat in item:
                    target = os.path.join(tier_02, clean_name)
                    print(f"[CONSOLIDATE EHM -> 02] {item} -> {target}")
                    if os.path.exists(target):
                        shutil.rmtree(target)
                    shutil.move(item_path, target)
                    break

    # Consolidate muhendislik_ortak
    mo_path = os.path.join(ROOT_DIR, 'ozel_arastirma_alanlari', 'muhendislik_ortak')
    if os.path.exists(mo_path):
        tier_01 = os.path.join(mo_path, '01_Temel_Bilimler_ve_Giris')
        clean_map = {
            'fizik': 'fizik',
            'biyoloji': 'biyoloji',
            'kimya': 'kimya',
            'matematik': 'matematik',
            'mant': 'mantik'
        }
        for item in os.listdir(mo_path):
            item_path = os.path.join(mo_path, item)
            if not os.path.isdir(item_path) or item.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_')):
                continue
            for pat, clean_name in clean_map.items():
                if pat in item:
                    target = os.path.join(tier_01, clean_name)
                    print(f"[CONSOLIDATE MO -> 01] {item} -> {target}")
                    if os.path.exists(target):
                        shutil.rmtree(target)
                    shutil.move(item_path, target)
                    break

    # Consolidate other legacy folders:
    other_cleanup = [
        ('hukuk_bilimi', 'hukuk', '02_Alan_Dersleri', ['medeni_hukuk', 'kamu_hukuku', 'ticaret_hukuku', 'uluslararasi_hukuk']),
        ('ilahiyat_ve_din', 'ilahiyat', '02_Alan_Dersleri', ['temel_islam_bilimleri', 'islam_tarihi_ve_sanatlari']),
        ('mimarlik_ve_tasarim', 'mimarlik', '02_Alan_Dersleri', ['tasarim_studyolari', 'mimarlik_tarihi_ve_teorisi', 'yapi_teknolojisi_ve_malzeme', 'gorsel_iletisim_ve_anlatim', 'yapi_fizigi_ve_cevre', 'bilgisayar_destekli_tasarim']),
    ]
    for c, d, tier, sub_list in other_cleanup:
        base = os.path.join(ROOT_DIR, c, d)
        if os.path.exists(base):
            target_tier = os.path.join(base, tier)
            for sub in sub_list:
                sub_p = os.path.join(base, sub)
                if os.path.exists(sub_p):
                    dst = os.path.join(target_tier, sub)
                    print(f"[CONSOLIDATE {c}/{d} -> {tier}] {sub} -> {dst}")
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.move(sub_p, dst)

    # Remove unneeded duplicate sub-department folders in engineering parents
    eng_sub_removals = [
        ('meta_muhendislik', 'jeoloji_muhendisligi', ['hidroloji', 'jeofizik', 'maden', 'petrol']),
        ('meta_muhendislik', 'ziraat_muhendisligi', ['orman', 'su_urunleri']),
        ('meta_muhendislik', 'kimya_muhendisligi', ['deri', 'g']),
        ('meta_muhendislik', 'metalurji_ve_malzeme_muhendisligi', ['polimer']),
        ('meta_muhendislik', 'makine_muhendisligi', ['uzay', 'otomotiv']),
    ]
    for c, d, patterns in eng_sub_removals:
        base = os.path.join(ROOT_DIR, c, d)
        if os.path.exists(base):
            for item in os.listdir(base):
                item_p = os.path.join(base, item)
                if not os.path.isdir(item_p) or item.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_')):
                    continue
                for pat in patterns:
                    if pat in item:
                        print(f"[REMOVE LEGACY MERGED DIR] {item_p}")
                        shutil.rmtree(item_p)
                        break

def remove_redundant_files():
    # Remove redundant DERS_SABLONU.md in departments
    removed = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        if '.git' in root or 'templates' in root:
            continue
        for f in files:
            if f == 'DERS_SABLONU.md':
                fp = os.path.join(root, f)
                os.remove(fp)
                removed += 1
            elif f == 'readme.md' and root != ROOT_DIR and os.path.exists(os.path.join(root, 'README.md')):
                # Duplicate case-insensitive readme
                fp = os.path.join(root, f)
                try:
                    os.remove(fp)
                    removed += 1
                except:
                    pass
    print(f"[CLEANUP] Removed {removed} redundant template/duplicate files.")

if __name__ == '__main__':
    print("Starting clean and organize...")
    clean_dept_names()
    clean_inner_dirs()
    consolidate_legacy_courses()
    remove_redundant_files()
    print("Clean and organize completed successfully.")
