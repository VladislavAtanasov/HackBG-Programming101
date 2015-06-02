from crawler import Crawler
from database import Database
from settings import STARTING_PAGE
from settings import DB_NAME
from settings import TABLES
from plot import Plotter


def main():

    database = Database(DB_NAME)
    database.create_tables_from_file(TABLES)

    # Get (external, internal) links from starting page
    crawler = Crawler()
    soup = Crawler.get_soup_of_url(STARTING_PAGE)
    links = Crawler.get_links_from_soup(soup)
    crawler.classify_internal_links(links)

    # Get all internal links
    internal_links = list(set(crawler.internal_links))
    for link in internal_links:
        soup = Crawler.get_soup_of_url(link)
        links = Crawler.get_links_from_soup(soup)
        crawler.classify_internal_links(links)

    all_internal_links = list(set(crawler.internal_links))
    database.add_internal_links(all_internal_links)

    # Crawl server headers and save it to the database
    while True:
        non_visited_link = database.get_non_visited_internal_link()
        print(non_visited_link)

        soup = Crawler.get_soup_of_url(non_visited_link)
        links = Crawler.get_links_from_soup(soup)
        crawler.classify_external_links(links)

        for link in crawler.external_links:
            if database.check_for_external_link(link):
                server_name = Crawler.get_server_header(link)
                database.add_external_link(link, server_name)
            else:
                continue

        database.set_visited_internal_link(non_visited_link)
        crawler.external_links = []

    # Make a histogram
    server_names = ["Apache", "nginx", "Microsoft", "lighttpd"]

    server_count = []
    server_count.append(database.count_server("Apache"))
    server_count.append(database.count_server("nginx"))
    server_count.append(database.count_server("Microsoft-IIS"))
    server_count.append(database.count_server("lighttpd"))

    new_plot = Plotter()
    new_plot.make_plot(server_names, server_count)

if __name__ == '__main__':
    main()
