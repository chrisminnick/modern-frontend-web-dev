#!/usr/bin/env python3
"""
Test script to verify HTML escaping in PDF generation
"""

import re
import html

def test_html_escaping():
    """Test the HTML escaping functionality"""
    
    # Test cases with HTML tags in backticks
    test_cases = [
        "- Document structure with `<header>`, `<main>`, `<footer>`",
        "- Content organization with `<article>`, `<section>`",
        "- Navigation with `<nav>`",
        "Use the `<div>` element for layout",
        "The `<input type='text'>` field accepts user input"
    ]
    
    print("🧪 Testing HTML escaping in inline code...")
    print("=" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input:  {test_case}")
        
        # Apply the same regex transformation as in the PDF generator
        processed = re.sub(r'`([^`]+)`', lambda m: f'<code>{html.escape(m.group(1))}</code>', test_case)
        print(f"Output: {processed}")
        
        # Check if HTML tags are properly escaped
        if "&lt;" in processed and "&gt;" in processed:
            print("✅ HTML tags properly escaped")
        else:
            print("❌ HTML tags NOT properly escaped")
    
    print("\n" + "=" * 50)
    print("Test complete!")

if __name__ == "__main__":
    test_html_escaping()