import requests
from bs4 import BeautifulSoup
from pprint import pprint


class Crawler:
    def __init__(self, url):
        self.url = url
        self.internal_links = []
        self.external_links = []
        self.visited = []

    def start(self):
        links = self.get_links_in_url(self.url)
        self.classify(links)
        self.visited.append(self.url)

        for link in self.internal_links:
            print(link)
            if link not in self.visited:
                sub_pages = self.get_links_in_url(link)
                self.classify(sub_pages)

    def get_links_in_url(self, url):
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
            link_list = set()
            for link in soup.find_all('a'):
                link_list.add(link.get('href'))
            return link_list
        except:
            return "Invalid input"

    def classify(self, links):
        for link in links:
            if link is None:
                continue
            elif "start.bg" in link:
                self.internal_links.append(link)
            elif "link.php?" in link:
                self.external_links.append(link)
            else:
                self.external_links.append(link)
        return self.internal_links

def main():
    crawler = Crawler("http://www.start.bg/")
    #print(crawler.get_links_in_url("http://www.start.bg/"))
    #pprint(crawler.classify(crawler.get_links_in_url("http://www.start.bg/")))
    print(crawler.start())

if __name__ == '__main__':
    main()
