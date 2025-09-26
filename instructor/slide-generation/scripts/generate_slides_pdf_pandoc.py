#!/usr/bin/env python3
"""
Alternative PDF Generator for Modern Frontend Web Development Slides
Uses pandoc and wkhtmltopdf for better macOS compatibility
"""

import re
import subprocess
import tempfile
import os
from pathlib import Path
import argparse
import sys

def check_dependencies():
    """Check if required external tools are installed"""
    missing = []
    
    # Check for pandoc
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        missing.append('pandoc')
    
    # Check for wkhtmltopdf
    try:
        subprocess.run(['wkhtmltopdf', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        missing.append('wkhtmltopdf')
    
    return missing

def install_dependencies_mac():
    """Install dependencies on macOS using Homebrew"""
    print("🍺 Installing dependencies using Homebrew...")
    try:
        # Check if brew is installed
        subprocess.run(['brew', '--version'], capture_output=True, check=True)
        
        # Install dependencies
        subprocess.run(['brew', 'install', 'pandoc', 'wkhtmltopdf'], check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def process_markdown_for_pandoc(markdown_content):
    """
    Process markdown content to add page breaks and improve formatting
    """
    lines = markdown_content.split('\n')
    processed_lines = []
    
    for i, line in enumerate(lines):
        # Check if this is a slide title (## followed by content, but not module headers)
        if (line.startswith('## ') and 
            not line.startswith('## Module ') and 
            not line.startswith('## Comprehensive Course Slides')):
            
            # Add page break before slide title (except for the first slide)
            if i > 0 and processed_lines:
                processed_lines.append('')
                processed_lines.append('\\newpage')
                processed_lines.append('')
            
        processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def create_html_template():
    """Create HTML template with CSS styling"""
    return """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Frontend Web Development Slides</title>
    <style>
        @page {
            size: A4 landscape;
            margin: 0.75in;
        }
        
        body {
            font-family: 'Segoe UI', 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            font-size: 11pt;
            max-width: none;
        }
        
        h1 {
            font-size: 24pt;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            page-break-after: avoid;
        }
        
        h2 {
            font-size: 18pt;
            color: #2c3e50;
            margin-top: 25px;
            margin-bottom: 15px;
            padding-bottom: 8px;
            border-bottom: 2px solid #3498db;
            page-break-after: avoid;
        }
        
        h3 {
            font-size: 14pt;
            color: #34495e;
            margin-top: 20px;
            margin-bottom: 10px;
            font-weight: bold;
            page-break-after: avoid;
        }
        
        h4 {
            font-size: 12pt;
            color: #34495e;
            margin-top: 15px;
            margin-bottom: 8px;
            font-weight: bold;
            page-break-after: avoid;
        }
        
        p {
            margin-bottom: 10px;
            text-align: justify;
        }
        
        ul, ol {
            margin-bottom: 12px;
            padding-left: 20px;
        }
        
        li {
            margin-bottom: 4px;
            text-align: left;
        }
        
        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Monaco', 'Menlo', 'Courier New', monospace;
            font-size: 9pt;
            color: #e74c3c;
        }
        
        pre {
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 4px;
            padding: 12px;
            margin: 12px 0;
            overflow-x: auto;
            page-break-inside: avoid;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
            color: #333;
            font-size: 9pt;
        }
        
        strong {
            font-weight: bold;
            color: #2c3e50;
        }
        
        em {
            font-style: italic;
            color: #34495e;
        }
        
        blockquote {
            border-left: 3px solid #3498db;
            padding-left: 12px;
            margin: 12px 0;
            font-style: italic;
            color: #555;
            background-color: #f8f9fa;
            padding: 8px 12px;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 12px 0;
            page-break-inside: avoid;
            font-size: 10pt;
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 6px 8px;
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
        
        /* Special styling for slide-like sections */
        hr {
            page-break-before: always;
            visibility: hidden;
            margin: 0;
            height: 0;
        }
        
        /* Avoid orphans and widows */
        h1, h2, h3, h4 {
            orphans: 2;
            widows: 2;
        }
        
        p, li {
            orphans: 2;
            widows: 2;
        }
    </style>
</head>
<body>
$body$
</body>
</html>
"""

def markdown_to_pdf_pandoc(input_file, output_file=None):
    """
    Convert Markdown slides to PDF using pandoc and wkhtmltopdf
    """
    try:
        # Check dependencies
        missing = check_dependencies()
        if missing:
            print(f"❌ Missing dependencies: {', '.join(missing)}")
            if sys.platform == 'darwin':  # macOS
                print("🔧 Attempting to install dependencies...")
                if install_dependencies_mac():
                    print("✅ Dependencies installed successfully!")
                    # Re-check dependencies
                    missing = check_dependencies()
                    if missing:
                        print(f"❌ Still missing: {', '.join(missing)}")
                        return False
                else:
                    print("❌ Failed to install dependencies automatically.")
                    print("Please install manually:")
                    print("  brew install pandoc wkhtmltopdf")
                    return False
            else:
                print("Please install the missing dependencies:")
                for dep in missing:
                    print(f"  - {dep}")
                return False
        
        # Read the markdown file
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Process markdown for better slide formatting
        processed_content = process_markdown_for_pandoc(markdown_content)
        
        # Generate output filename if not provided
        if output_file is None:
            input_path = Path(input_file)
            output_file = input_path.parent / f"{input_path.stem}.pdf"
        
        # Create temporary files
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as temp_md:
            temp_md.write(processed_content)
            temp_md_path = temp_md.name
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as temp_html:
            temp_html_path = temp_html.name
        
        try:
            # Convert markdown to HTML using pandoc
            print("📄 Converting Markdown to HTML...")
            pandoc_cmd = [
                'pandoc',
                temp_md_path,
                '-f', 'markdown',
                '-t', 'html',
                '--template', '-',  # Use stdin for template
                '--standalone',
                '--highlight-style', 'tango',
                '-o', temp_html_path
            ]
            
            # Run pandoc with template
            result = subprocess.run(
                pandoc_cmd,
                input=create_html_template(),
                text=True,
                capture_output=True,
                check=True
            )
            
            # Convert HTML to PDF using wkhtmltopdf
            print("📄 Converting HTML to PDF...")
            wkhtmltopdf_cmd = [
                'wkhtmltopdf',
                '--page-size', 'A4',
                '--orientation', 'Landscape',
                '--margin-top', '0.5in',
                '--margin-right', '0.5in',
                '--margin-bottom', '0.5in',
                '--margin-left', '0.5in',
                '--encoding', 'UTF-8',
                '--no-outline',
                '--disable-smart-shrinking',
                '--print-media-type',
                temp_html_path,
                str(output_file)
            ]
            
            result = subprocess.run(wkhtmltopdf_cmd, capture_output=True, check=True)
            
            print(f"✅ PDF generated successfully: {output_file}")
            return True
            
        finally:
            # Clean up temp files
            try:
                os.unlink(temp_md_path)
                os.unlink(temp_html_path)
            except:
                pass
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running external command: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr.decode()}")
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
        description="Convert Markdown slides to PDF using pandoc and wkhtmltopdf",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_slides_pdf_pandoc.py slides.md
  python generate_slides_pdf_pandoc.py slides.md -o presentation.pdf

Dependencies:
  - pandoc (for Markdown to HTML conversion)
  - wkhtmltopdf (for HTML to PDF conversion)
  
On macOS, install with: brew install pandoc wkhtmltopdf
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
    success = markdown_to_pdf_pandoc(args.input_file, args.output)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()