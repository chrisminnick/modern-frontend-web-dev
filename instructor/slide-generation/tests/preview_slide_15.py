#!/usr/bin/env python3
"""
Test preview of slide 15 with HTML escaping
"""

import re
import html

def preview_slide_15():
    """Preview how slide 15 will look with proper HTML escaping"""
    
    # Slide 15 content from the markdown
    slide_content = """## Lab 04 - Semantic HTML

**Learning Objectives:**

- Structure content with HTML5 semantic elements
- Improve accessibility and SEO
- Create meaningful document outlines
- Build foundation for CSS styling

**Practice Elements:**

- Document structure with `<header>`, `<main>`, `<footer>`
- Content organization with `<article>`, `<section>`
- Navigation with `<nav>`
- Supplementary content with `<aside>`"""

    print("🔍 Preview of Slide 15 (Lab 04 - Semantic HTML)")
    print("=" * 60)
    print("Original Markdown:")
    print(slide_content)
    print("\n" + "=" * 60)
    
    # Process the content similar to how the PDF generator does it
    lines = slide_content.split('\n')
    html_output = []
    
    for line in lines:
        if line.startswith('## '):
            title = line[3:].strip()
            html_output.append(f'<h2 class="slide-title">{html.escape(title)}</h2>')
        elif line.startswith('- '):
            item_content = line[2:].strip()
            # Apply formatting
            item_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_content)
            item_content = re.sub(r'`([^`]+)`', lambda m: f'<code>{html.escape(m.group(1))}</code>', item_content)
            html_output.append(f'<li>{item_content}</li>')
        elif line.strip().startswith('**') and line.strip().endswith('**'):
            content = line.strip()[2:-2]
            html_output.append(f'<p><strong>{html.escape(content)}</strong></p>')
        elif line.strip():
            html_output.append(f'<p>{html.escape(line)}</p>')
    
    print("Generated HTML:")
    for html_line in html_output:
        print(html_line)
    
    print("\n" + "=" * 60)
    print("✅ HTML tags in backticks are now properly escaped!")
    print("✅ They will display as text instead of blank space in the PDF")

if __name__ == "__main__":
    preview_slide_15()