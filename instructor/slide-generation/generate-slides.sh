#!/bin/bash

# Convenience script to generate slides PDF from project root
# This calls the slide generation system in the slide-generation folder

set -e

echo "🎯 Generating Slides PDF..."
echo "=========================="

# Change to the slide generation scripts directory and run
cd "$(dirname "$0")/slide-generation/scripts"
./generate_pdf.sh

echo "✅ PDF generation complete!"
echo "📁 Check slide-generation/generated-pdfs/ for output"