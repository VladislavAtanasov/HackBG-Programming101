import requests
from bs4 import BeautifulSoup
import json

class Crawl:

    def __init__(self):
        self.lis_servers = []

    def to_JSON(self, string):
        self.lis_servers.append(string)

    def save_json(self):
        with open("datacrawl.json", "w") as f:
            json_string = json.dumps(self.lis_servers)
            f.write(json_string)

def main():
    h = Crawl()
    r = requests.get("http://register.start.bg/")
    soup = BeautifulSoup(r.text)
    links = "link.php?id="
    link_list = ["http://register.start.bg/" + link.get('href') for link in soup.find_all('a') if link.get('href') is not None and links in link.get('href')]
    for item in link_list:
        try:
            req = requests.head(item, timeout = 2.0, allow_redirects = True)
            if "server" in req.headers:
                str_req = req.headers["server"]
                if "Apache" in str_req:
                    print(str_req)
                    h.to_JSON("Apache")
                elif "Microsoft" in str_req:
                    print(str_req)
                    h.to_JSON("IIS")
                elif "nginx" in str_req:
                    print(str_req)
                    h.to_JSON("nginx")
                elif "lighttpd" in str_req:
                    print(str_req)
                    h.to_JSON("nginx")
                else:
                    h.to_JSON("other")
        except requests.exceptions.RequestException as e:
            continue
    h.save_json()

if __name__ == '__main__':
    main()
