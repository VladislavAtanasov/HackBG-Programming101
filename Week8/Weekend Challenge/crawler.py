import requests
from bs4 import BeautifulSoup
from settings import STARTING_PAGE
from settings import JAVASCRIPT
from settings import HASHTAG
from settings import EXTERNAL_PART
from settings import INTERNAL_PART
from settings import SLASH
from settings import SERVER_FIELD


class Crawler:

    def __init__(self):
        self.internal_links = [STARTING_PAGE]
        self.external_links = []

    @staticmethod
    def get_soup_of_url(url):
        response = requests.get(url, timeout=2, allow_redirects=True)
        soup = BeautifulSoup(response.text)

        return soup

    @staticmethod
    def get_links_from_soup(soup):
        links = set()

        for link in soup.find_all('a'):
            links.add(link.get('href'))

        return links

    def classify_internal_links(self, links):
        for link in links:
            # Check for bad links
            if link is None or JAVASCRIPT in link or link.startswith(HASHTAG):
                continue

            # Add internal urls
            if INTERNAL_PART in link:
                if not link.endswith(SLASH):
                    link = link + SLASH
                self.internal_links.append(link)

    def classify_external_links(self, links):
        for link in links:
            # Check for bad links
            if link is None or JAVASCRIPT in link or link.startswith(HASHTAG):
                continue

            # Add external urls
            if EXTERNAL_PART in link:
                self.external_links.append(STARTING_PAGE + link)

    @staticmethod
    def get_server_header(link):
        server_name = ""

        try:
            response = requests.head(link, timeout=3, allow_redirects=True)
            if SERVER_FIELD in response.headers:
                server_name = response.headers["Server"]
        except requests.exceptions.RequestException:
            pass

        return server_name

    def get_internal_links(self):
        return self.internal_links

    def get_external_links(self):
        return self.external_links
