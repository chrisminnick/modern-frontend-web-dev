#!/usr/bin/env python3
"""
Simple PDF Generator for Modern Frontend Web Development Slides
Uses Python's built-in libraries and system tools for maximum compatibility
"""

import re
import html
import subprocess
import tempfile
import os
from pathlib import Path
import argparse
import sys

def process_markdown_simple(markdown_content):
    """
    Simple markdown to HTML conversion with slide breaks, lists, and tables
    """
    lines = markdown_content.split('\n')
    html_lines = []
    in_code_block = False
    in_list = False
    in_table = False
    code_lang = ''
    
    # Pre-process to remove horizontal rules that are immediately followed by slide titles
    cleaned_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # If this is a horizontal rule, check if next non-empty line is a slide title
        if line.strip() == '---':
            # Look ahead for next non-empty line
            j = i + 1
            while j < len(lines) and lines[j].strip() == '':
                j += 1
            
            # If next non-empty line is a slide title, skip the horizontal rule
            if (j < len(lines) and lines[j].startswith('## ') and 
                not lines[j].startswith('## Comprehensive Course Slides')):
                i += 1  # Skip the horizontal rule
                continue
        
        cleaned_lines.append(line)
        i += 1
    
    # Process the cleaned lines
    for i, line in enumerate(cleaned_lines):
        # Handle code blocks
        if line.startswith('```'):
            # Close any open list before starting code block
            if in_list:
                html_lines.append('</ul>')
                in_list = False
                
            if not in_code_block:
                # Start of code block
                in_code_block = True
                code_lang = line[3:].strip()
                html_lines.append(f'<pre><code class="language-{code_lang}">')
                continue
            else:
                # End of code block
                in_code_block = False
                html_lines.append('</code></pre>')
                continue
        
        if in_code_block:
            html_lines.append(html.escape(line))
            continue
        
        # Handle slide titles and module titles (page breaks)
        if (line.startswith('## ') and 
            not line.startswith('## Comprehensive Course Slides')):
            
            # Close any open list before starting new slide
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Close any open table before starting new slide
            if in_table:
                if '<tbody>' in ''.join(html_lines[-10:]):
                    html_lines.append('</tbody>')
                elif '<thead>' in ''.join(html_lines[-10:]) and '</thead>' not in ''.join(html_lines[-5:]):
                    html_lines.append('</thead>')
                html_lines.append('</table>')
                in_table = False
            
            # Add page break only if this isn't the first content
            if i > 0 and html_lines:
                html_lines.append('<div class="page-break"></div>')
            
            # Extract title text (remove "## " and handle Module format)
            title_text = line[3:].strip()
            if line.startswith('## Module '):
                # For module titles, add special styling
                html_lines.append(f'<h2 class="slide-title module-title">{html.escape(title_text)}</h2>')
            else:
                html_lines.append(f'<h2 class="slide-title">{html.escape(title_text)}</h2>')
            continue
        
        # Handle other headers
        if line.startswith('# '):
            # Close any open list before header
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            html_lines.append(f'<h1>{html.escape(line[2:])}</h1>')
            continue
        elif line.startswith('### '):
            # Close any open list before header
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Close any open table before header
            if in_table:
                if '<tbody>' in ''.join(html_lines[-10:]):
                    html_lines.append('</tbody>')
                elif '<thead>' in ''.join(html_lines[-10:]) and '</thead>' not in ''.join(html_lines[-5:]):
                    html_lines.append('</thead>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<h3>{html.escape(line[4:])}</h3>')
            continue
        elif line.startswith('#### '):
            # Close any open list before header
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Close any open table before header
            if in_table:
                if '<tbody>' in ''.join(html_lines[-10:]):
                    html_lines.append('</tbody>')
                elif '<thead>' in ''.join(html_lines[-10:]) and '</thead>' not in ''.join(html_lines[-5:]):
                    html_lines.append('</thead>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append(f'<h4>{html.escape(line[5:])}</h4>')
            continue
        
        # Handle lists
        elif line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            
            # Process the list item content for inline formatting
            item_content = line[2:].strip()
            # Process markdown links first
            item_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', item_content)
            item_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item_content)
            # Escape HTML inside code tags before creating code elements
            item_content = re.sub(r'`([^`]+)`', lambda m: f'<code>{html.escape(m.group(1))}</code>', item_content)
            html_lines.append(f'<li>{html.escape(item_content) if not ("<strong>" in item_content or "<code>" in item_content or "<a href=" in item_content) else item_content}</li>')
            continue
        
        # Handle tables (only if not in code block and line starts with |)
        elif not in_code_block and line.strip().startswith('|') and line.strip().endswith('|') and line.count('|') >= 2:
            # Close any open list before table
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            
            # Check if this is a table separator line (|---|---|)
            if re.match(r'^\s*\|[\s\-\|]*\|\s*$', line):
                continue  # Skip separator lines
            
            # Process table row
            if not in_table:
                html_lines.append('<table>')
                in_table = True
                # Check if this looks like a header row by looking ahead for separator
                is_header = False
                if i + 1 < len(cleaned_lines):
                    next_line = cleaned_lines[i + 1]
                    if re.match(r'^\s*\|[\s\-\|]*\|\s*$', next_line):
                        is_header = True
                
                if is_header:
                    html_lines.append('<thead>')
            
            # Split the line by pipes and clean up
            cells = [cell.strip() for cell in line.split('|')[1:-1]]  # Remove first and last empty parts
            
            # Determine if this is a header row
            is_header_row = False
            if in_table and i + 1 < len(cleaned_lines):
                next_line = cleaned_lines[i + 1]
                if re.match(r'^\s*\|[\s\-\|]*\|\s*$', next_line):
                    is_header_row = True
            
            # Create table row
            if is_header_row:
                row_cells = []
                for cell in cells:
                    # Process inline formatting in cell
                    processed_cell = cell
                    processed_cell = re.sub(r'`([^`]+)`', lambda m: f'<code>{html.escape(m.group(1))}</code>', processed_cell)
                    processed_cell = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', processed_cell)
                    if "<code>" in processed_cell or "<strong>" in processed_cell:
                        row_cells.append(f'<th>{processed_cell}</th>')
                    else:
                        row_cells.append(f'<th>{html.escape(processed_cell)}</th>')
                html_lines.append(f'<tr>{"".join(row_cells)}</tr>')
            else:
                # Check if we need to close thead and open tbody
                if in_table and '</thead>' not in html_lines[-5:]:  # Look back a few lines
                    # Check if we just finished a header
                    if i > 0 and re.match(r'^\s*\|[\s\-\|]*\|\s*$', cleaned_lines[i-1]):
                        html_lines.append('</thead>')
                        html_lines.append('<tbody>')
                elif in_table and '<tbody>' not in ''.join(html_lines[-10:]):
                    html_lines.append('<tbody>')
                
                row_cells = []
                for cell in cells:
                    # Process inline formatting in cell
                    processed_cell = cell
                    processed_cell = re.sub(r'`([^`]+)`', lambda m: f'<code>{html.escape(m.group(1))}</code>', processed_cell)
                    processed_cell = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', processed_cell)
                    if "<code>" in processed_cell or "<strong>" in processed_cell:
                        row_cells.append(f'<td>{processed_cell}</td>')
                    else:
                        row_cells.append(f'<td>{html.escape(processed_cell)}</td>')
                html_lines.append(f'<tr>{"".join(row_cells)}</tr>')
            continue
        
        # Handle horizontal rules (slide separators) - these should be rare now due to pre-processing
        elif line.strip() == '---':
            # Close any open list before page break
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Close any open table before page break
            if in_table:
                if '<tbody>' in ''.join(html_lines[-10:]):
                    html_lines.append('</tbody>')
                elif '<thead>' in ''.join(html_lines[-10:]) and '</thead>' not in ''.join(html_lines[-5:]):
                    html_lines.append('</thead>')
                html_lines.append('</table>')
                in_table = False
            html_lines.append('<div class="page-break"></div>')
            continue
        
        # Handle empty lines
        elif line.strip() == '':
            # Close list on empty line
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Close table on empty line
            if in_table:
                if '<tbody>' in ''.join(html_lines[-10:]):
                    html_lines.append('</tbody>')
                elif '<thead>' in ''.join(html_lines[-10:]) and '</thead>' not in ''.join(html_lines[-5:]):
                    html_lines.append('</thead>')
                html_lines.append('</table>')
                in_table = False
            continue
        
        # Handle regular paragraphs
        else:
            # Close any open list before paragraph
            if in_list:
                html_lines.append('</ul>')
                in_list = False
            # Close any open table before paragraph
            if in_table:
                if '<tbody>' in ''.join(html_lines[-10:]):
                    html_lines.append('</tbody>')
                elif '<thead>' in ''.join(html_lines[-10:]) and '</thead>' not in ''.join(html_lines[-5:]):
                    html_lines.append('</thead>')
                html_lines.append('</table>')
                in_table = False
            
            # Process inline formatting
            processed_line = line
            # Process markdown links first
            processed_line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', processed_line)
            processed_line = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', processed_line)
            # Escape HTML inside code tags before creating code elements
            processed_line = re.sub(r'`([^`]+)`', lambda m: f'<code>{html.escape(m.group(1))}</code>', processed_line)
            
            if "<strong>" in processed_line or "<code>" in processed_line or "<a href=" in processed_line:
                html_lines.append(f'<p>{processed_line}</p>')
            else:
                html_lines.append(f'<p>{html.escape(processed_line)}</p>')
    
    # Close any remaining open list
    if in_list:
        html_lines.append('</ul>')
    
    # Close any remaining open table
    if in_table:
        if '<tbody>' in ''.join(html_lines[-10:]):
            html_lines.append('</tbody>')
        elif '<thead>' in ''.join(html_lines[-10:]) and '</thead>' not in ''.join(html_lines[-5:]):
            html_lines.append('</thead>')
        html_lines.append('</table>')
    
    return '\n'.join(html_lines)

def create_complete_html(content, title="Modern Frontend Web Development Slides"):
    """Create complete HTML document with embedded CSS"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        @media print {{
            @page {{
                size: A4 portrait;
                margin: 0.5in;
            }}
            
            .page-break {{
                page-break-before: always;
                height: 0;
                margin: 0;
                visibility: hidden;
            }}
            
            .slide-title {{
                page-break-after: avoid;
            }}
            
            h1, h2, h3, h4 {{
                page-break-after: avoid;
                orphans: 2;
                widows: 2;
            }}
            
            pre, code {{
                page-break-inside: avoid;
            }}
            
            ul, ol {{
                page-break-inside: avoid;
            }}
        }}
        
        /* Reset all margins and indentation */
        * {{
            margin: 0;
            padding: 0;
            text-indent: 0;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
            line-height: 1.6;
            color: #333;
            font-size: 11pt;
            max-width: none;
            margin: 0;
            padding: 20px;
        }}
        
        /* Restore necessary margins */
        h1, h2, h3, h4, p, ul, ol, pre, blockquote {{
            margin-bottom: 10px;
        }}
        
        h1, h2, h3, h4 {{
            margin-top: 15px;
        }}
        
        h1 {{
            font-size: 24pt;
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        
        .slide-title, h2 {{
            font-size: 20pt;
            color: #2c3e50;
            margin: 25px 0 15px 0;
            padding: 0 0 8px 0;
            border-bottom: 2px solid #3498db;
            text-indent: 0;
            position: relative;
            left: 0;
        }}
        
        .module-title {{
            font-size: 22pt;
            background-color: #3498db;
            color: white;
            padding: 15px 20px;
            margin: 25px 0 20px 0;
            border-radius: 5px;
            border-bottom: none;
            text-align: center;
            font-weight: bold;
        }}
        
        h3 {{
            font-size: 16pt;
            color: #34495e;
            margin-top: 20px;
            margin-bottom: 10px;
            font-weight: bold;
        }}
        
        h4 {{
            font-size: 14pt;
            color: #34495e;
            margin-top: 15px;
            margin-bottom: 8px;
            font-weight: bold;
        }}
        
        p {{
            margin-bottom: 10px;
            text-align: justify;
        }}
        
        ul, ol {{
            margin: 10px 0 15px 0;
            padding-left: 20px;
            list-style-type: disc;
        }}
        
        li {{
            margin-bottom: 5px;
            padding-left: 0;
            text-indent: 0;
        }}
        
        /* Reset any nested indentation */
        ul ul, ol ol, ul ol, ol ul {{
            margin-left: 0;
            padding-left: 20px;
        }}
        
        code {{
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
            font-size: 10pt;
            color: #e74c3c;
        }}
        
        pre {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 4px;
            padding: 12px;
            margin: 12px 0;
            overflow-x: auto;
        }}
        
        pre code {{
            background-color: transparent;
            padding: 0;
            color: #333;
            font-size: 10pt;
        }}
        
        strong {{
            font-weight: 600;
            color: #2c3e50;
        }}
        
        em {{
            font-style: italic;
            color: #34495e;
        }}
        
        a {{
            color: #3498db;
            text-decoration: underline;
            font-weight: 500;
        }}
        
        a:hover {{
            color: #2980b9;
        }}
        
        /* Table styling */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            font-size: 10pt;
        }}
        
        th, td {{
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
            vertical-align: top;
        }}
        
        th {{
            background-color: #f8f9fa;
            font-weight: 600;
            color: #2c3e50;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        /* Ensure code in tables doesn't break */
        td code {{
            white-space: nowrap;
        }}
        
        .page-break {{
            page-break-before: always;
            height: 0;
            margin: 0;
            visibility: hidden;
        }}
        
        @media screen {{
            .page-break {{
                border-top: 2px dashed #ccc;
                margin: 40px 0;
                text-align: center;
                position: relative;
                height: 20px;
                visibility: visible;
            }}
            
            .page-break::after {{
                content: "Page Break";
                background: white;
                padding: 0 10px;
                color: #666;
                font-size: 10pt;
                position: absolute;
                top: -8px;
                left: 50%;
                transform: translateX(-50%);
            }}
        }}
    </style>
</head>
<body>
{content}
</body>
</html>"""

def markdown_to_pdf_simple(input_file, output_file=None):
    """
    Convert Markdown slides to PDF using simple HTML generation and system print
    """
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
            output_file = input_path.parent / f"{input_path.stem}.pdf"
        
        # Create temporary HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as temp_html:
            temp_html.write(full_html)
            temp_html_path = temp_html.name
        
        try:
            # Try different methods to convert HTML to PDF
            success = False
            
            # Method 1: Try using Safari's headless mode (macOS)
            if sys.platform == 'darwin':
                try:
                    cmd = [
                        '/System/Library/Frameworks/WebKit.framework/Versions/Current/Helpers/WebKitTestRunner',
                        '--no-timeout',
                        f'file://{temp_html_path}'
                    ]
                    # This might not work, but we'll try other methods
                except:
                    pass
            
            # Method 2: Try using Chrome/Chromium headless mode
            chrome_paths = [
                '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                '/Applications/Chromium.app/Contents/MacOS/Chromium',
                'google-chrome',
                'chromium',
                'chrome'
            ]
            
            for chrome_path in chrome_paths:
                try:
                    cmd = [
                        chrome_path,
                        '--headless',
                        '--disable-gpu',
                        '--no-pdf-header-footer',
                        '--print-to-pdf=' + str(output_file),
                        f'file://{temp_html_path}'
                    ]
                    
                    result = subprocess.run(cmd, capture_output=True, timeout=30)
                    if result.returncode == 0 and Path(output_file).exists():
                        success = True
                        break
                except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
                    continue
            
            if success:
                print(f"✅ PDF generated successfully: {output_file}")
                return True
            else:
                # Fallback: Create the HTML file for manual conversion
                html_output = Path(output_file).with_suffix('.html')
                with open(html_output, 'w', encoding='utf-8') as f:
                    f.write(full_html)
                
                print(f"⚠️  Could not automatically generate PDF.")
                print(f"📄 HTML file created: {html_output}")
                print(f"🖨️  To create PDF manually:")
                print(f"   1. Open {html_output} in your browser")
                print(f"   2. Press Cmd+P (or Ctrl+P)")
                print(f"   3. Select 'Save as PDF'")
                print(f"   4. Choose portrait orientation")
                print(f"   5. Save as {output_file}")
                return True
                
        finally:
            # Clean up temp file
            try:
                os.unlink(temp_html_path)
            except:
                pass
        
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
        description="Convert Markdown slides to PDF (simple version)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_slides_pdf_simple.py slides.md
  python generate_slides_pdf_simple.py slides.md -o presentation.pdf

This script tries to automatically generate PDF using Chrome/Chromium.
If that fails, it creates an HTML file that you can manually print to PDF.
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
    success = markdown_to_pdf_simple(args.input_file, args.output)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()