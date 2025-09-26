#!/usr/bin/env python3
"""
Test script to verify markdown link processing
"""

import re
import html

def test_markdown_links():
    """Test the markdown link processing functionality"""
    
    # Test cases with markdown links
    test_cases = [
        "Visit [GitHub](https://github.com) for more information",
        "Check out the [course repository](https://github.com/chrisminnick/modern-frontend-web-dev)",
        "- Download from [https://code.visualstudio.com](https://code.visualstudio.com)",
        "**Website:** [https://www.watzthis.com](https://www.watzthis.com)",
        "Mix of `code` and [links](https://example.com) in **bold** text"
    ]
    
    print("🧪 Testing Markdown Link Processing...")
    print("=" * 60)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"Input:  {test_case}")
        
        # Apply the same processing as in the PDF generator
        processed = test_case
        # Process markdown links first
        processed = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', processed)
        processed = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', processed)
        # Escape HTML inside code tags before creating code elements
        processed = re.sub(r'`([^`]+)`', lambda m: f'<code>{html.escape(m.group(1))}</code>', processed)
        
        print(f"Output: {processed}")
        
        # Check if links are properly converted
        if "<a href=" in processed:
            print("✅ Markdown links properly converted")
        else:
            print("❌ Markdown links NOT converted")
    
    print("\n" + "=" * 60)
    print("Test complete!")

if __name__ == "__main__":
    test_markdown_links()