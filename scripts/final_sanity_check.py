import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUDE_DIRS = {'.git', '.vs', '.github', 'scripts', 'assets', 'templates'}

def final_sanity_check():
    errors = []
    dept_count = 0
    tier_count = 0
    container_count = 0
    
    for container in sorted(os.listdir(ROOT_DIR)):
        c_path = os.path.join(ROOT_DIR, container)
        if not os.path.isdir(c_path) or container in EXCLUDE_DIRS:
            continue
            
        container_count += 1
        for dept in sorted(os.listdir(c_path)):
            d_path = os.path.join(c_path, dept)
            if not os.path.isdir(d_path):
                continue
            
            dept_count += 1
            # Check main README
            if not os.path.exists(os.path.join(d_path, "README.md")):
                errors.append(f"Missing README: {container}/{dept}")
            
            # Check Tiers 00-06
            for i in range(7):
                tier_found = False
                for t_dir in os.listdir(d_path):
                    if t_dir.startswith(f"0{i}_"):
                        tier_found = True
                        tier_count += 1
                        # Check tier README
                        if not os.path.exists(os.path.join(d_path, t_dir, "README.md")):
                            errors.append(f"Missing Tier README: {container}/{dept}/{t_dir}")
                if not tier_found:
                    errors.append(f"Missing Tier Directory 0{i}: {container}/{dept}")

    print("==================================================")
    print("           REPOSITORY INTEGRITY REPORT            ")
    print("==================================================")
    print(f"Containers Verified  : {container_count}")
    print(f"Departments Verified : {dept_count}")
    print(f"Tiers (00-06) Verified: {tier_count}")
    print("--------------------------------------------------")
    
    if not errors:
        print("[SUCCESS] ALL CLEAR: Every node is present and has a valid README.")
        print("==================================================")
        return True
    else:
        print(f"[FAILED] FOUND {len(errors)} ANOMALIES:")
        for e in errors[:20]:
            print(f"  - {e}")
        print("==================================================")
        return False

if __name__ == "__main__":
    success = final_sanity_check()
    if not success:
        exit(1)
