import sqlite3


class Database:

    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def create_tables_from_file(self, filename):
        with open(filename, "r") as f:
            self.cursor.executescript(f.read())

        self.connection.commit()

    def add_internal_links(self, links):
        add_internal_link_query = '''
            INSERT INTO InternalLinks(url, visited)
            VALUES(?, ?)
        '''

        for link in links:
            self.cursor.execute(add_internal_link_query, (link, 0))

        self.connection.commit()

    def get_non_visited_internal_link(self):
        get_non_visited_internal_link = '''
            SELECT url
            FROM InternalLinks
            WHERE visited = 0
            LIMIT 1
        '''

        self.cursor.execute(get_non_visited_internal_link)
        all_urls = self.cursor.fetchall()

        return all_urls[0][0]

    def add_external_link(self, link, server_name):
        add_external_link_query = '''
            INSERT INTO ExternalLinksAndServers(url, server)
            VALUES(?, ?)
        '''

        self.cursor.execute(add_external_link_query, (link, server_name))
        self.connection.commit()

    def check_for_external_link(self, link):
        check_for_external_link_query = '''
        SELECT url
        FROM ExternalLinksAndServers
        WHERE url = ?
        '''

        self.cursor.execute(check_for_external_link_query, (link, ))
        data = self.cursor.fetchone()

        if data is None:
            return True
        else:
            return False

    def set_visited_internal_link(self, link):
        set_visited_internal_link_query = '''
            UPDATE InternalLinks
            SET visited = 1
            WHERE url = ?
        '''

        self.cursor.execute(set_visited_internal_link_query, (link, ))
        self.connection.commit()

    def count_server(self, server):
        count_server_query = '''
            SELECT COUNT(id)
            FROM ExternalLinksAndServers
            WHERE server LIKE ?
        '''

        server_as_string = "%{}%".format(server)

        self.cursor.execute(count_server_query, (server_as_string, ))
        count_servers = self.cursor.fetchone()[0]

        return count_servers
