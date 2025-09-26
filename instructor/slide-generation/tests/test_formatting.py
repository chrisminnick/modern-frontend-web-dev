#!/usr/bin/env python3
"""
Test script to validate list and slide formatting
"""

def test_formatting():
    """Test the markdown processing for common formatting issues"""
    
    test_markdown = """# Test Document

## Course Overview

**What You'll Learn:**

- HTML5 semantic markup and modern standards
- CSS3 with Grid, Flexbox, and responsive design
- JavaScript ES6+ with modern programming patterns
- DOM manipulation and event handling

---

## Module 1: Introduction

This is a module introduction.

**Key Topics:**

- Topic 1
- Topic 2

---

## The Modern Web Platform

**Evolution of Web Development:**

**Then (Early 2000s):**

- Static HTML pages
- Table-based layouts
- Inline styles and scripts

**Now (2024):**

- Component-based architectures
- Mobile-first responsive design
- Modern JavaScript with ES6+ features

---

## Module 2: Advanced Topics

Another module section.

---

## Client-Server Architecture

**Key Points:**

- HTML structure and content
- CSS styling and layout
- JavaScript interactivity and logic
"""

    # Import the processing function
    import sys
    sys.path.append('.')
    from generate_slides_pdf_simple import process_markdown_simple
    
    # Process the test markdown
    result = process_markdown_simple(test_markdown)
    
    print("🧪 Testing Markdown Processing")
    print("=" * 40)
    print("Input:")
    print(test_markdown[:200] + "...")
    print("\n" + "=" * 40)
    print("Output HTML:")
    print(result[:500] + "...")
    
    # Check for common issues
    issues = []
    
    # Check for nested lists (shouldn't happen)
    if '<ul><ul>' in result or '</ul></ul>' in result:
        issues.append("❌ Nested <ul> tags detected")
    else:
        print("✅ No nested <ul> tags")
    
    # Check for proper list closing
    ul_opens = result.count('<ul>')
    ul_closes = result.count('</ul>')
    if ul_opens != ul_closes:
        issues.append(f"❌ Unmatched <ul> tags: {ul_opens} opens, {ul_closes} closes")
    else:
        print("✅ All <ul> tags properly closed")
    
    # Check for proper slide structure
    slide_count = result.count('class="slide-title"')
    page_breaks = result.count('class="page-break"')
    print(f"✅ Found {slide_count} slides with {page_breaks} page breaks")
    
    # Debug: Show where page breaks are occurring
    lines = result.split('\n')
    for i, line in enumerate(lines):
        if 'page-break' in line:
            context_start = max(0, i-2)
            context_end = min(len(lines), i+3)
            print(f"Page break at line {i}:")
            for j in range(context_start, context_end):
                marker = ">>> " if j == i else "    "
                print(f"{marker}{lines[j]}")
            print()
    
    if issues:
        print("\n⚠️  Issues found:")
        for issue in issues:
            print(f"   {issue}")
    else:
        print("\n🎉 All formatting tests passed!")
    
    return len(issues) == 0

if __name__ == "__main__":
    test_formatting()