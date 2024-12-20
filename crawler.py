import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    page_title = soup.title.string
    print(f"Page Title: {page_title}")
    # 您可以在这里添加更多的解析逻辑

def main():
    url = 'https://example.com'  # 替换为您要抓取的URL
    html = fetch_page(url)
    if html:
        parse_html(html)

if __name__ == '__main__':
    main()
