import requests
from bs4 import BeautifulSoup
import sys

url = 'https://www.bbc.com/news'
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    html_content = response.text
except requests.RequestException as e:
    print(f"Error fetching the URL: {e}")
    sys.exit(1)

soup = BeautifulSoup(html_content, 'html.parser')

headlines = set()

for tag in soup.find_all(['h2', 'h3']):
    text = tag.get_text(strip=True)
    if text and len(text) > 15:
        headlines.add(text)

with open("headlines.txt", "w", encoding="utf-8") as f:
    for idx, headline in enumerate(sorted(headlines), start=1):
        f.write(f"{idx}. {headline}\n")

print(f"✅ Grabbed {len(headlines)} unique headlines and saved them in 'headlines.txt'")
