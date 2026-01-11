import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title_tag = soup.find("h1")
        if not title_tag:
            return "Error", "Title not found"

        title = title_tag.text

        paragraphs = soup.find_all("p")
        if not paragraphs:
            return title, "No content found"

        text = " ".join(p.text for p in paragraphs[:10])

        return title, text

    except Exception as e:
        return "Error", str(e)
