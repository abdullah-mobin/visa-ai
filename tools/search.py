import webbrowser
import urllib.parse

def search_google(query: str):
    try:
        if not query:
            return "Empty search query."

        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://www.google.com/search?q={encoded_query}"

        webbrowser.open(url)
        return f"Searching Google for: {query}"
    except Exception as e:
        return f"Search error: {e}"
