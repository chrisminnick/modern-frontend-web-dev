#!/bin/bash

# Modern Frontend Web Development - PDF Generator Script
# This script converts the Markdown slides to PDF format using pandoc

set -e  # Exit on any error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
INPUT_FILE="$PROJECT_ROOT/modern-frontend-development-slides-v3.0.0.md"
OUTPUT_FILE="$SCRIPT_DIR/../generated-pdfs/modern-frontend-development-slides.pdf"

echo "🎯 Modern Frontend Web Development - PDF Generator"
echo "=================================================="

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "❌ Error: Slides file not found: $INPUT_FILE"
    exit 1
fi

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed."
    exit 1
fi

# Generate PDF using simple Python script
echo "📄 Generating PDF from slides..."
python3 "$SCRIPT_DIR/generate_slides_pdf_simple.py" "$INPUT_FILE" -o "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Success! PDF generated at: $OUTPUT_FILE"
    echo "📊 File size: $(du -h "$OUTPUT_FILE" | cut -f1)"
    
    # Try to open the PDF (macOS)
    if command -v open &> /dev/null; then
        read -p "🔍 Would you like to open the PDF? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            open "$OUTPUT_FILE"
        fi
    fi
else
    echo "❌ Error: PDF generation failed."
    exit 1
fi