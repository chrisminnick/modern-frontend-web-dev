#!/usr/bin/env python3
"""
PDF Generator for Modern Frontend Web Development Slides
Converts Markdown slides to PDF with page breaks between slides
"""

import re
import markdown
from weasyprint import HTML, CSS
from pathlib import Path
import argparse
import sys

def process_markdown_for_slides(markdown_content):
    """
    Process markdown content to add page breaks before slide titles
    and improve formatting for PDF generation
    """
    # Split content into lines
    lines = markdown_content.split('\n')
    processed_lines = []
    
    for i, line in enumerate(lines):
        # Check if this is a slide title (## followed by content, but not module headers)
        if (line.startswith('## ') and 
            not line.startswith('## Module ') and 
            not line.startswith('## Comprehensive Course Slides')):
            
            # Add page break before slide title (except for the first slide)
            if i > 0 and processed_lines:
                processed_lines.append('<div class="page-break"></div>')
                processed_lines.append('')
            
            # Add slide class to the title
            processed_lines.append(f'<div class="slide-title">{line[3:]}</div>')
        else:
            processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def create_css_styles():
    """
    Create CSS styles for the PDF with professional formatting
    """
    return CSS(string="""
    @page {
        size: A4 landscape;
        margin: 1in;
        @top-center {
            content: "Modern Frontend Web Development";
            font-family: 'Arial', sans-serif;
            font-size: 10pt;
            color: #666;
        }
        @bottom-right {
            content: counter(page);
            font-family: 'Arial', sans-serif;
            font-size: 10pt;
            color: #666;
        }
    }
    
    body {
        font-family: 'Arial', 'Helvetica', sans-serif;
        line-height: 1.6;
        color: #333;
        font-size: 12pt;
    }
    
    .page-break {
        page-break-before: always;
    }
    
    .slide-title {
        font-size: 24pt;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 3px solid #3498db;
    }
    
    h1 {
        font-size: 28pt;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
        page-break-after: avoid;
    }
    
    h2 {
        font-size: 20pt;
        color: #34495e;
        margin-top: 25px;
        margin-bottom: 15px;
        page-break-after: avoid;
    }
    
    h3 {
        font-size: 16pt;
        color: #34495e;
        margin-top: 20px;
        margin-bottom: 10px;
        page-break-after: avoid;
    }
    
    h4 {
        font-size: 14pt;
        color: #34495e;
        margin-top: 15px;
        margin-bottom: 8px;
        font-weight: bold;
        page-break-after: avoid;
    }
    
    p {
        margin-bottom: 12px;
        text-align: justify;
        orphans: 2;
        widows: 2;
    }
    
    ul, ol {
        margin-bottom: 15px;
        padding-left: 25px;
    }
    
    li {
        margin-bottom: 5px;
    }
    
    code {
        background-color: #f8f9fa;
        padding: 2px 4px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
        font-size: 11pt;
        color: #e74c3c;
    }
    
    pre {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 5px;
        padding: 15px;
        margin: 15px 0;
        overflow-x: auto;
        page-break-inside: avoid;
    }
    
    pre code {
        background-color: transparent;
        padding: 0;
        color: #333;
        font-size: 10pt;
    }
    
    strong, **strong** {
        font-weight: bold;
        color: #2c3e50;
    }
    
    em {
        font-style: italic;
        color: #34495e;
    }
    
    blockquote {
        border-left: 4px solid #3498db;
        padding-left: 15px;
        margin: 15px 0;
        font-style: italic;
        color: #555;
        background-color: #f8f9fa;
        padding: 10px 15px;
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
        page-break-inside: avoid;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 8px 12px;
        text-align: left;
    }
    
    th {
        background-color: #3498db;
        color: white;
        font-weight: bold;
    }
    
    tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    
    .module-header {
        background-color: #3498db;
        color: white;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
        font-size: 18pt;
        font-weight: bold;
        text-align: center;
        page-break-before: always;
        page-break-after: avoid;
    }
    
    .learning-objectives {
        background-color: #e8f6f3;
        border-left: 4px solid #27ae60;
        padding: 15px;
        margin: 15px 0;
    }
    
    .key-concepts {
        background-color: #fef9e7;
        border-left: 4px solid #f39c12;
        padding: 15px;
        margin: 15px 0;
    }
    
    /* Avoid page breaks in code blocks and lists */
    pre, ul, ol, .learning-objectives, .key-concepts {
        page-break-inside: avoid;
    }
    
    /* Ensure slide titles don't get orphaned */
    .slide-title {
        page-break-after: avoid;
    }
    
    /* Better spacing for the first page */
    body > h1:first-child {
        margin-top: 0;
    }
    """)

def markdown_to_pdf(input_file, output_file=None):
    """
    Convert Markdown slides to PDF
    """
    try:
        # Read the markdown file
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Process markdown for slides
        processed_content = process_markdown_for_slides(markdown_content)
        
        # Convert to HTML with extensions
        md = markdown.Markdown(extensions=[
            'codehilite',
            'fenced_code',
            'tables',
            'toc'
        ])
        html_content = md.convert(processed_content)
        
        # Wrap in HTML document
        full_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Modern Frontend Web Development Slides</title>
        </head>
        <body>
            {html_content}
        </body>
        </html>
        """
        
        # Generate output filename if not provided
        if output_file is None:
            input_path = Path(input_file)
            output_file = input_path.parent / f"{input_path.stem}.pdf"
        
        # Create CSS styles
        css_styles = create_css_styles()
        
        # Generate PDF
        html_doc = HTML(string=full_html)
        html_doc.write_pdf(output_file, stylesheets=[css_styles])
        
        print(f"✅ PDF generated successfully: {output_file}")
        return True
        
    except ImportError as e:
        if 'weasyprint' in str(e):
            print("❌ Error: weasyprint is not installed.")
            print("Install it with: pip install weasyprint")
        elif 'markdown' in str(e):
            print("❌ Error: markdown is not installed.")
            print("Install it with: pip install markdown")
        else:
            print(f"❌ Import error: {e}")
        return False
        
    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_file}' not found.")
        return False
        
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return False

def main():
    """
    Main function with command line argument parsing
    """
    parser = argparse.ArgumentParser(
        description="Convert Markdown slides to PDF with page breaks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_slides_pdf.py slides.md
  python generate_slides_pdf.py slides.md -o presentation.pdf
  python generate_slides_pdf.py slides.md --output /path/to/output.pdf
        """
    )
    
    parser.add_argument(
        'input_file',
        help='Input Markdown file'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output PDF file (default: same name as input with .pdf extension)'
    )
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not Path(args.input_file).exists():
        print(f"❌ Error: Input file '{args.input_file}' does not exist.")
        sys.exit(1)
    
    # Convert to PDF
    success = markdown_to_pdf(args.input_file, args.output)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()