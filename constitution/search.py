import json

# Load constitution data (assuming JSON format)
with open("constitution.json", "r", encoding="utf-8") as f:
    constitution = json.load(f)

def search_constitution(keyword):
    results = []
    for section in constitution["sections"]:
        if keyword.lower() in section["text"].lower():
            results.append(section)
    return results

# Example usage
matches = search_constitution("fundamental rights")
for m in matches:
    print(f"Section {m['number']}: {m['text'][:100]}...")
