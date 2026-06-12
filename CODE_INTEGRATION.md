# Code Integration Guide

## How Code Snippets Are Used

Code files in `code/{course}/{module}/part-{N}.py` are referenced by notebook stubs using IPython magic:

```python
%load https://raw.githubusercontent.com/ailearningclub/ailearningclub-collab/main/code/{course}/{module}/part-{N}.py
```

## Code Organization

- **code/{course}/{module}/part-1.py**: First code block from module markdown
- **code/{course}/{module}/part-2.py**: Second code block (if it exists)
- etc.

Code blocks are extracted from course markdown by `tf-ailearningclub-com/generate_ipynb_stubs.py`

## Cleanup Status

- ✅ Unused code directories moved to `.unused/` (preserves git history)
- ✅ Expected code modules defined in `MANIFEST.json`
- 📋 To restore: `git reset HEAD path/to/file && git restore path/to/file`

## What's Included

- **code/**: Production code snippets for courses that have content
- **.unused/**: Archive of previously used code (can be recovered via git tags)
- **.gitignore**: Configured to preserve .unused as history

See `MANIFEST.json` for complete list of expected code modules.
