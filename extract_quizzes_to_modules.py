#!/usr/bin/env python3
import json
import re
from pathlib import Path

def extract_quiz_from_notebook(nb_path):
    """Extract quiz HTML from notebook markdown cells."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
    except:
        return None
    
    for cell in nb.get('cells', []):
        if cell.get('cell_type') != 'markdown':
            continue
        content = ''.join(cell.get('source', []))
        if '<div class="quiz"' in content:
            return content
    return None

def remove_answer_from_quiz(quiz_html):
    """Remove data-correct attribute from quiz divs to hide answers."""
    return re.sub(r' data-correct="\d+"', '', quiz_html)

def insert_quiz_to_module(md_path, quiz_html):
    """Insert quiz into markdown module before ## Practice in Notebook section."""
    with open(md_path) as f:
        content = f.read()
    
    # Don't overwrite if quiz already exists
    if '## Quiz' in content or '<div class="quiz"' in content:
        return False
    
    # Find insertion point
    match = re.search(r'(## Practice in Notebook|## Next Steps|$)', content)
    if not match:
        return False
    
    quiz_section = f"\n## Quiz\n\n{quiz_html}\n"
    new_content = content[:match.start()] + quiz_section + content[match.start():]
    
    with open(md_path, 'w') as f:
        f.write(new_content)
    return True

# Process all courses
for course_dir in Path('.').iterdir():
    if not course_dir.is_dir() or course_dir.name.startswith('.'):
        continue
    
    for i in range(1, 100):
        nb_path = course_dir / f'mod-{i}.ipynb'
        md_path = course_dir / f'mod-{i}.md'
        
        if not nb_path.exists():
            break
        if not md_path.exists():
            continue
        
        quiz_html = extract_quiz_from_notebook(nb_path)
        if quiz_html:
            quiz_html = remove_answer_from_quiz(quiz_html)
            if insert_quiz_to_module(md_path, quiz_html):
                print(f"✓ {md_path}")
