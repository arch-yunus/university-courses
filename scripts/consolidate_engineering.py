import os
import shutil

ROOT_DIR = r"g:\Diğer bilgisayarlar\Dizüstü Bilgisayarım\github repolarım\engineering-courses"
MUH_DIR = os.path.join(ROOT_DIR, "meta_muhendislik")

# Merge Map: Source -> Target
MERGE_MAP = {
    "insaat_teknolojisi_muhendisligi": "insaat_muhendisligi",
    "tekstil_teknolojisi_muhendisligi": "tekstil_muhendisligi",
    "rayli_sistemler_sinyalizasyon_ve_kontrol": "rayli_sistemler_muhendisligi",
    "akilli_gorsel_muhendislik": "akilli_gorsel_isitsel_muhendislik",
}

def consolidate():
    for src, dst in MERGE_MAP.items():
        src_path = os.path.join(MUH_DIR, src)
        dst_path = os.path.join(MUH_DIR, dst)
        
        if os.path.exists(src_path):
            if not os.path.exists(dst_path):
                print(f"Renaming {src} to {dst}")
                os.rename(src_path, dst_path)
            else:
                print(f"Merging {src} into {dst}")
                # Move subdirectories if they don't exist in target
                for item in os.listdir(src_path):
                    s_item = os.path.join(src_path, item)
                    d_item = os.path.join(dst_path, item)
                    if os.path.isdir(s_item):
                        if not os.path.exists(d_item):
                            shutil.move(s_item, dst_path)
                        else:
                            # If it exists, we could merge contents or skip
                            # For simplicity in this scaffolding, we move unique ones
                            pass
                shutil.rmtree(src_path)

def fix_readme_titles():
    for folder in os.listdir(MUH_DIR):
        folder_path = os.path.join(MUH_DIR, folder)
        if os.path.isdir(folder_path):
            readme_path = os.path.join(folder_path, "README.md")
            if os.path.exists(readme_path):
                # Professional Turkish Title Generation
                title = folder.replace('_', ' ').title()
                # Specific overrides for Turkish characters
                title = title.replace('Muhendisligi', 'Mühendisliği')
                title = title.replace('Insaat', 'İnşaat')
                title = title.replace('Isletme', 'İşletme')
                title = title.replace('Ulasim', 'Ulaşım')
                title = title.replace('Havacilik', 'Havacılık')
                title = title.replace('Yapay Zeka', 'Yapay Zeka')
                title = title.replace('Bilisim', 'Bilişim')
                title = title.replace('Biyomedikal', 'Biyomedikal') # No change needed but for completeness
                title = title.replace('Tekstil', 'Tekstil')
                title = title.replace('Ucak', 'Uçak')
                title = title.replace('Gemi Insaati', 'Gemi İnşaatı')
                title = title.replace('Nukleer', 'Nükleer')
                title = title.replace('Jeofizik', 'Jeofizik')
                title = title.replace('Rayli', 'Raylı')
                title = title.replace('Sinai', 'Sınai')
                title = title.replace('Ipek', 'İpek')
                title = title.replace('Iha', 'İHA')
                title = title.replace('Lojistik', 'Lojistik')
                title = title.replace('Turizm', 'Turizm')
                
                with open(readme_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                if lines and lines[0].startswith('#'):
                    lines[0] = f"# {title}\n"
                    with open(readme_path, 'w', encoding='utf-8') as f:
                        f.writelines(lines)
                print(f"Updated title for {folder} -> {title}")

if __name__ == "__main__":
    consolidate()
    fix_readme_titles()
