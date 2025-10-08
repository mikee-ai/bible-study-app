"""
Bible API Service
Handles fetching Bible verses from external API
"""

import requests
from typing import Dict, List, Optional

class BibleService:
    """Service for fetching Bible verses"""
    
    def __init__(self):
        # Using Bible API (https://bible-api.com) - free, no key required
        self.base_url = "https://bible-api.com"
    
    def get_verse(self, reference: str, translation: str = "kjv") -> Optional[Dict]:
        """
        Get a Bible verse by reference
        
        Args:
            reference: Bible reference (e.g., "John 3:16", "Romans 8:14-17")
            translation: Bible translation (kjv, web, etc.)
        
        Returns:
            Dictionary with verse data or None if error
        """
        try:
            url = f"{self.base_url}/{reference}"
            params = {"translation": translation}
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    "reference": data.get("reference", reference),
                    "text": data.get("text", ""),
                    "translation": data.get("translation_name", translation.upper()),
                    "verses": data.get("verses", [])
                }
            else:
                return None
        except Exception as e:
            print(f"Error fetching verse: {e}")
            return None
    
    def search_verses(self, query: str, translation: str = "kjv") -> List[Dict]:
        """
        Search for verses containing keywords
        Note: bible-api.com doesn't support search, so this is a placeholder
        In production, you'd use a different API or database
        """
        # For MVP, we'll return empty list
        # In production, integrate with APIs like ESV API or use local database
        return []
    
    def get_chapter(self, book: str, chapter: int, translation: str = "kjv") -> Optional[Dict]:
        """
        Get an entire chapter
        
        Args:
            book: Book name (e.g., "John", "Romans")
            chapter: Chapter number
            translation: Bible translation
        
        Returns:
            Dictionary with chapter data or None if error
        """
        reference = f"{book} {chapter}"
        return self.get_verse(reference, translation)
