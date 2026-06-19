# search.py - Utility script to search Nigerian Constitution text
# Loads constitution.json and allows keyword-based search of sections

import json

# Load constitution data from JSON file
with open("constitution.json", "r", encoding="utf-8") as f:
    constitution = json.load(f)

def search_constitution(keyword):
    """
    Search constitution sections for a given keyword.
    Returns a list of matching sections.
    """
    results = []
    for section in constitution["sections"]:
        if keyword.lower() in section["text"].lower():
            results.append(section)
    return results

# Example usage: search for 'fundamental rights'
matches = search_constitution("fundamental rights")
for m in matches:
    print(f"Section {m['number']}: {m['text'][:100]}...")
