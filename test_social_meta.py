#!/usr/bin/env python3
"""
Test script to verify social media meta tags are properly configured.
This script checks if the Open Graph and Twitter Card meta tags are correctly set.
"""

import requests
from bs4 import BeautifulSoup
import re

def test_meta_tags(url):
    """Test meta tags for a given URL"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Check for Open Graph tags
        og_tags = {
            'og:title': soup.find('meta', property='og:title'),
            'og:description': soup.find('meta', property='og:description'),
            'og:image': soup.find('meta', property='og:image'),
            'og:url': soup.find('meta', property='og:url'),
            'og:type': soup.find('meta', property='og:type'),
            'og:site_name': soup.find('meta', property='og:site_name'),
        }
        
        # Check for Twitter Card tags
        twitter_tags = {
            'twitter:card': soup.find('meta', name='twitter:card'),
            'twitter:title': soup.find('meta', name='twitter:title'),
            'twitter:description': soup.find('meta', name='twitter:description'),
            'twitter:image': soup.find('meta', name='twitter:image'),
        }
        
        print(f"\n=== Testing {url} ===")
        
        print("\nOpen Graph Tags:")
        for tag_name, tag in og_tags.items():
            if tag and tag.get('content'):
                print(f"✓ {tag_name}: {tag['content']}")
            else:
                print(f"✗ {tag_name}: Missing or empty")
        
        print("\nTwitter Card Tags:")
        for tag_name, tag in twitter_tags.items():
            if tag and tag.get('content'):
                print(f"✓ {tag_name}: {tag['content']}")
            else:
                print(f"✗ {tag_name}: Missing or empty")
        
        # Check if image URLs are absolute
        og_image = og_tags['og:image']
        if og_image and og_image.get('content'):
            image_url = og_image['content']
            if image_url.startswith('http'):
                print(f"✓ Image URL is absolute: {image_url}")
            else:
                print(f"✗ Image URL is relative: {image_url}")
        
        return True
        
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return False
    except Exception as e:
        print(f"Error parsing {url}: {e}")
        return False

def main():
    """Main function to test all pages"""
    base_url = "https://siamsarker.pythonanywhere.com"
    pages = [
        "",
        "/about.html",
        "/projects.html", 
        "/contact.html",
        "/experience.html",
        "/education.html",
        "/skills.html"
    ]
    
    print("Testing Social Media Meta Tags for Siam Sarker's Portfolio")
    print("=" * 60)
    
    all_passed = True
    for page in pages:
        url = base_url + page
        if not test_meta_tags(url):
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ All tests passed! Your social media meta tags are properly configured.")
        print("\nNext steps:")
        print("1. Use Facebook's Sharing Debugger: https://developers.facebook.com/tools/debug/")
        print("2. Use Twitter's Card Validator: https://cards-dev.twitter.com/validator")
        print("3. Test sharing on WhatsApp and Facebook")
    else:
        print("✗ Some tests failed. Please check the issues above.")

if __name__ == "__main__":
    main()
