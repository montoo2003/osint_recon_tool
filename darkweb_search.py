import requests

def darkweb_lookup(query):
    url = f"https://ahmia.fi/search/?q={query}"
    response = requests.get(url)
    
    if "No results found" in response.text:
        return "No dark web mentions found."
    return f"Possible mentions of {query} on the dark web. Check manually."
