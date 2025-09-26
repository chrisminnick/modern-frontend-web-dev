#!/usr/bin/env python3
"""
Validation script for the PDF generation tools
Tests the markdown processing and provides feedback
"""

import re
from pathlib import Path

def validate_markdown_structure(markdown_file):
    """
    Validate the markdown structure for slide generation
    """
    print(f"🔍 Validating: {markdown_file}")
    print("=" * 50)
    
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count different elements
        slides = re.findall(r'^## (?!Module |Comprehensive)', content, re.MULTILINE)
        modules = re.findall(r'^## Module \d+:', content, re.MULTILINE)
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        lists = re.findall(r'^- .+', content, re.MULTILINE)
        
        print(f"📊 Structure Analysis:")
        print(f"   • Total slides: {len(slides)}")
        print(f"   • Module sections: {len(modules)}")
        print(f"   • Code blocks: {len(code_blocks)}")
        print(f"   • List items: {len(lists)}")
        print()
        
        print(f"📄 Slide Titles Found:")
        for i, slide in enumerate(slides[:10], 1):  # Show first 10
            title = slide.strip()
            print(f"   {i:2d}. {title}")
        
        if len(slides) > 10:
            print(f"   ... and {len(slides) - 10} more slides")
        
        print()
        print(f"📚 Module Sections:")
        for module in modules:
            print(f"   • {module}")
        
        print()
        print("✅ Markdown structure validation complete!")
        
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: File '{markdown_file}' not found.")
        return False
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False

def check_pdf_output():
    """
    Check if PDF files were generated
    """
    print("\n🔍 Checking PDF Output")
    print("=" * 50)
    
    pdf_files = list(Path('.').glob('*.pdf'))
    
    if pdf_files:
        print(f"✅ Found {len(pdf_files)} PDF file(s):")
        for pdf in pdf_files:
            size = pdf.stat().st_size
            size_kb = size / 1024
            print(f"   📄 {pdf.name} ({size_kb:.1f} KB)")
    else:
        print("❌ No PDF files found in current directory")
    
    return len(pdf_files) > 0

def main():
    """Main validation function"""
    print("🎯 Modern Frontend Web Development - PDF Generation Validator")
    print("=" * 60)
    
    # Check markdown file
    markdown_file = "modern-frontend-development-slides-v3.0.0.md"
    if not validate_markdown_structure(markdown_file):
        return False
    
    # Check PDF output
    if not check_pdf_output():
        print("\n💡 To generate PDF, run: ./generate_pdf.sh")
        return False
    
    print("\n🎉 All validations passed!")
    print("\n📖 Usage:")
    print("   • Run: ./generate_pdf.sh")
    print("   • Or: python3 generate_slides_pdf_simple.py slides.md")
    print("   • See: README-PDF-Generation.md for details")
    
    return True

if __name__ == "__main__":
    main()