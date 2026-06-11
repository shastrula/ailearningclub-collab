#!/usr/bin/env python3
import json
import os
from pathlib import Path

def extract_code_cells(notebook_path):
    """Extract code cells from notebook"""
    try:
        with open(notebook_path, 'r') as f:
            nb = json.load(f)
        return [cell['source'] for cell in nb.get('cells', []) if cell['cell_type'] == 'code']
    except:
        return []

def embed_code_in_markdown(course_dir):
    """Embed notebook code into markdown modules"""
    course_path = Path(course_dir)
    
    for md_file in sorted(course_path.glob('mod-*.md')):
        mod_num = md_file.stem.replace('mod-', '')
        nb_file = course_path / f'mod-{mod_num}.ipynb'
        
        if not nb_file.exists():
            continue
        
        # Extract code cells
        code_cells = extract_code_cells(nb_file)
        if not code_cells:
            continue
        
        # Read markdown
        with open(md_file, 'r') as f:
            content = f.read()
        
        # Skip if code already embedded
        if '```python' in content and len(content) > 2000:
            continue
        
        # Build code section
        code_section = "\n## Code Examples\n\n"
        for i, cell in enumerate(code_cells[:5], 1):  # Limit to first 5 cells
            code_text = ''.join(cell).strip()
            if code_text:
                code_section += f"```python\n{code_text}\n```\n\n"
        
        # Append before Colab badge
        if "Practice in Notebook" in content:
            content = content.replace("## Practice in Notebook", code_section + "## Practice in Notebook")
        else:
            content += code_section
        
        # Write back
        with open(md_file, 'w') as f:
            f.write(content)
        
        print(f"✓ {md_file.name}")

# Process all courses
repo = Path('.')
for course_dir in sorted(repo.glob('*')):
    if course_dir.is_dir() and not course_dir.name.startswith('.'):
        embed_code_in_markdown(course_dir)

print("✅ Embedded notebook code into markdown modules")
