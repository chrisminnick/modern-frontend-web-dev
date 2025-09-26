#!/usr/bin/env python3
"""
HTML Preview Generator for testing PDF formatting
Creates HTML version for quick preview of slide formatting
"""

import sys
from pathlib import Path

# Import the processing function from the main script
sys.path.append('.')
from generate_slides_pdf_simple import process_markdown_simple, create_complete_html

def create_html_preview(input_file, output_file=None):
    """Create HTML preview of the slides"""
    
    try:
        # Read the markdown file
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert to HTML
        html_content = process_markdown_simple(markdown_content)
        full_html = create_complete_html(html_content)
        
        # Generate output filename if not provided
        if output_file is None:
            input_path = Path(input_file)
            output_file = input_path.parent / f"{input_path.stem}-preview.html"
        
        # Write HTML file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f"✅ HTML preview created: {output_file}")
        print(f"🌐 Open in browser to check formatting before PDF generation")
        
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_file}' not found.")
        return False
        
    except Exception as e:
        print(f"❌ Error creating HTML preview: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 create_html_preview.py input.md [output.html]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = create_html_preview(input_file, output_file)
    if not success:
        sys.exit(1)