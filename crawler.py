import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


def is_valid_url(url):
    """Check if the URL is valid."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def crawl_page(url, max_depth, current_depth, crawled_urls):
    """Crawl a given URL recursively up to a specified depth."""
    if current_depth > max_depth:
        return

    try:
        # Fetch the content of the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all anchor tags to extract links
        for link in soup.find_all('a', href=True):
            abs_url = urljoin(url, link['href'])  # Make it an absolute URL
            if is_valid_url(abs_url) and abs_url not in [entry['url'] for entry in crawled_urls]:
                crawled_urls.append({'url': abs_url, 'depth': current_depth})
                # Recursively crawl the next level
                crawl_page(abs_url, max_depth, current_depth + 1, crawled_urls)

    except Exception as e:
        print(f"Failed to crawl {url}: {e}")
