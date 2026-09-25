#!/usr/bin/env python3
"""
Evrensel Akademik İşletim Sistemi (UAOS) - Repository Management Suite
"""
import os
import sys
import argparse
from pathlib import Path

# Add scripts directory to sys.path
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPTS_DIR)
sys.path.insert(0, SCRIPTS_DIR)

from final_sanity_check import final_sanity_check
from generate_summary import generate_summary
from generate_encyclopedic_readme import generate_encyclopedic_readme

def print_repo_stats():
    md_count = 0
    pdf_count = 0
    dirs_count = 0
    container_count = 0
    dept_count = 0
    tier_count = 0
    
    EXCLUDE = {'.git', '.vs', '.github', 'scripts', 'assets', 'templates'}
    
    for c in sorted(os.listdir(ROOT_DIR)):
        cp = os.path.join(ROOT_DIR, c)
        if os.path.isdir(cp) and c not in EXCLUDE:
            container_count += 1
            depts = [d for d in os.listdir(cp) if os.path.isdir(os.path.join(cp, d))]
            dept_count += len(depts)
            for d in depts:
                dp = os.path.join(cp, d)
                tiers = [t for t in os.listdir(dp) if os.path.isdir(os.path.join(dp, t)) and t.startswith(('00_', '01_', '02_', '03_', '04_', '05_', '06_'))]
                tier_count += len(tiers)

    for root, dirs, files in os.walk(ROOT_DIR):
        if '.git' in root or '.vs' in root:
            continue
        dirs_count += len(dirs)
        for f in files:
            if f.endswith('.md'):
                md_count += 1
            elif f.endswith('.pdf'):
                pdf_count += 1

    print("==================================================")
    print("      UAOS / UNIVERSITY COURSES REPO STATS        ")
    print("==================================================")
    print(f"Total Containers        : {container_count}")
    print(f"Total Academic Depts    : {dept_count}")
    print(f"Total Standard Tiers    : {tier_count}")
    print(f"Total Markdown Files    : {md_count}")
    print(f"Total PDF Files         : {pdf_count}")
    print(f"Total Directories       : {dirs_count}")
    print("==================================================")

def main():
    parser = argparse.ArgumentParser(description="UAOS Repository Management Suite")
    parser.add_argument("--stats", action="store_true", help="Display repository statistics")
    parser.add_argument("--verify", action="store_true", help="Run repository sanity checks")
    parser.add_argument("--build-readme", action="store_true", help="Generate README.md")
    parser.add_argument("--build-summary", action="store_true", help="Generate SUMMARY.md")
    parser.add_argument("--build-all", action="store_true", help="Run verification and regenerate both README and SUMMARY")

    args = parser.parse_args()

    if len(sys.argv) == 1 or args.build_all:
        print("[1/3] Running verification...")
        if not final_sanity_check():
            print("[ERROR] Integrity check failed. Aborting build.")
            sys.exit(1)
        print("[2/3] Generating SUMMARY.md...")
        generate_summary()
        print("[3/3] Generating README.md...")
        generate_encyclopedic_readme()
        print_repo_stats()
        print("\n[SUCCESS] Full repository verification and build completed successfully!")
        return

    if args.stats:
        print_repo_stats()
    if args.verify:
        final_sanity_check()
    if args.build_summary:
        generate_summary()
    if args.build_readme:
        generate_encyclopedic_readme()

if __name__ == "__main__":
    main()
