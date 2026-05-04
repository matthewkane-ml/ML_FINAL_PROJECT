from urllib.parse import quote_plus

def get_youtube_review_url(title: str):
    query = quote_plus(f"{title} movie review trailer")
    return f"https://www.youtube.com/results?search_query={query}"
