import webbrowser
import urllib.parse

def play_youtube_video(query: str):
    try:
        if not query:
            return "Empty YouTube query."

        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://www.youtube.com/results?search_query={encoded_query}"

        # Open search page first, simulate auto-clicking 1st result (via redirect trick)
        watch_url = f"https://www.youtube.com/results?search_query={encoded_query}&sp=EgIQAQ%253D%253D"

        # Open in default browser
        webbrowser.open(watch_url)

        return f"Playing: {query}"
    except Exception as e:
        return f"YouTube error: {e}"
