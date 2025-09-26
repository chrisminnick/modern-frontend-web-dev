# Slide Generation System

This folder contains all the tools and assets for generating PDF presentations from the course slides.

## Folder Structure

```
slide-generation/
├── scripts/                    # Generation scripts
│   ├── generate_slides_pdf_simple.py  # Main PDF generator (recommended)
│   ├── generate_slides_pdf.py          # WeasyPrint version (macOS issues)
│   ├── generate_slides_pdf_pandoc.py   # Pandoc version (alternative)
│   └── generate_pdf.sh                # Shell wrapper script
├── generated-pdfs/            # Output PDFs
│   ├── modern-frontend-development-slides-html-escaped.pdf  # Latest with HTML escaping fix
│   ├── modern-frontend-development-slides-final.pdf        # Previous final version
│   └── [other generated versions]
├── tests/                     # Testing and validation scripts
│   ├── test_html_escaping.py     # Test HTML escaping functionality
│   ├── test_formatting.py       # Test PDF formatting
│   ├── preview_slide_15.py      # Preview specific slide content
│   └── validate_pdf_tools.py    # Validate system requirements
└── documentation/             # Fix summaries and documentation
    ├── HTML-Escaping-Fix-Summary.md     # Latest fix for HTML tags in backticks
    ├── PDF-Final-Fix-Summary.md         # Previous formatting fixes
    └── PDF-Formatting-Fix-Summary.md    # Earlier formatting solutions
```

## Quick Start

### Generate PDF from slides

```bash
# From the project root directory
cd slide-generation/scripts
./generate_pdf.sh
```

### Or run directly with Python

```bash
# From the project root directory
python3 slide-generation/scripts/generate_slides_pdf_simple.py modern-frontend-development-slides-v3.0.0.md -o slide-generation/generated-pdfs/output.pdf
```

## System Requirements

- Python 3.x
- Chrome or Chromium browser (for headless PDF generation)
- macOS, Linux, or Windows

## Features

- ✅ Converts Markdown slides to professional PDF
- ✅ Automatic page breaks for each slide
- ✅ Proper HTML escaping for code examples
- ✅ Module title styling with blue backgrounds
- ✅ Responsive layout for A4 landscape format
- ✅ Professional typography and spacing

## Latest Updates

### HTML Escaping Fix (Current)

- **Issue**: HTML tags in backticks (like `<header>`) were showing as blank space
- **Solution**: Proper HTML entity escaping in inline code
- **File**: `generate_slides_pdf_simple.py` (recommended script)
- **Output**: `generated-pdfs/modern-frontend-development-slides-html-escaped.pdf`

### Previous Fixes

- Cumulative list indentation issues
- Blank pages between slides
- Module title formatting
- Page break management

## Testing

Run tests to verify functionality:

```bash
cd slide-generation/tests
python3 test_html_escaping.py      # Test HTML escaping
python3 test_formatting.py         # Test PDF formatting
python3 validate_pdf_tools.py      # Check system requirements
```

## Troubleshooting

1. **Chrome not found**: Ensure Chrome or Chromium is installed and in PATH
2. **Permission denied**: Make sure `generate_pdf.sh` is executable: `chmod +x generate_pdf.sh`
3. **HTML not escaping**: Use `generate_slides_pdf_simple.py` (latest version with fixes)

## File Organization Benefits

- **Scripts**: All generation tools in one place
- **Generated PDFs**: Version history preserved
- **Tests**: Quality assurance and validation tools
- **Documentation**: Fix histories and troubleshooting guides
- **Clean root**: Main project directory stays organized
