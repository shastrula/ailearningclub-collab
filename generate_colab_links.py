#!/usr/bin/env python3
import os
import json
from pathlib import Path

REPO_URL = "https://github.com/shastrula/ailearningclub-collab/blob/main"
COLAB_BASE = "https://colab.research.google.com/github/shastrula/ailearningclub-collab/blob/main"

def generate_colab_link(course_id, mod_name):
    """Generate Colab link for a notebook"""
    return f"{COLAB_BASE}/{course_id}/{mod_name}.ipynb"

def add_colab_section(md_path, course_id, mod_name):
    """Add Colab link section to markdown file"""
    with open(md_path, 'r') as f:
        content = f.read()
    
    # Skip if already has colab link
    if "Open in Colab" in content or "colab.research.google.com" in content:
        return
    
    colab_url = generate_colab_link(course_id, mod_name)
    colab_section = f"\n\n## Run in Google Colab\n\n[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})\n"
    
    with open(md_path, 'a') as f:
        f.write(colab_section)

def main():
    root = Path(".")
    updated = 0
    
    for course_dir in sorted(root.iterdir()):
        if not course_dir.is_dir() or course_dir.name in ['code', '.git', '__pycache__']:
            continue
        
        course_id = course_dir.name
        
        for md_file in sorted(course_dir.glob("mod-*.md")):
            mod_name = md_file.stem
            add_colab_section(md_file, course_id, mod_name)
            updated += 1
            print(f"✓ {course_id}/{mod_name}")
    
    print(f"\n✅ Added Colab links to {updated} modules")

if __name__ == "__main__":
    main()
