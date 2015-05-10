import requests
from keys import CLIENT_ID, CLIENT_SECRET

class DirectedGraph:

    def __init__(self):
        self.graph = requests.get('https://api.github.com/users/VladislavAtanasov?client_id=4f6f61e8b2212d38ac82&client_secret=4fe11adf8968431cb77124cb44e17a0c5ad5b774')
        self.id = CLIENT_ID
        self.secret = CLIENT_SECRET
        self.nodes = {}

    def _make_list_of_usernames(self, source):
        return [user['login'] for user in source.json()]

    def get_network_for(self, user):

        network = {
            'followers': [],
            'following': []
        }

        cur_followers_page = 1
        cur_following_page = 1
        is_there_followers = True
        is_there_following = True

        while is_there_followers:
            followers = requests.get('https://api.github.com/users/'
                                     + user +
                                     '/followers?page={}&per_page=100&client_id='.format(cur_followers_page)
                                     + self.id +
                                     '&client_secret='
                                     + self.secret)

            if followers.status_code != 200:
                raise CantConnectToGitHubApi

            if followers.json():
                network['followers'] += self._make_list_of_usernames(followers)
            else:
                is_there_followers = False
            cur_followers_page += 1

        while is_there_following:
            following = requests.get('https://api.github.com/users/'
                                     + user +
                                     '/following?page={}&per_page=100&client_id='.format(cur_following_page)
                                     + self.id +
                                     '&client_secret='
                                     + self.secret)

            if following.status_code != 200:
                raise CantConnectToGitHubApi

            if following.json():
                network['following'] += self._make_list_of_usernames(following)
            else:
                is_there_following = False

            cur_following_page += 1

        return network


    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()
        else:
            raise ValueError("Node already here")

    def add_edge(self, node_a, node_b):
        if node_b not in self.nodes:
            self.add_node(node_b)
        if node_a not in self.nodes:
            self.add_node(node_a)
        if node_b not in self.nodes[node_a]:
            self.nodes[node_a].add(node_b)
            return True

    def get_neighbors_for(self, node):
        return self.nodes[node]

    def path_between(self,node_a, node_b):
        if isinstance(node_b, str) and isinstance(node_a, str):
            visited = set()
            queue = []
            path_to = {}
            queue.append(node_a)
            visited.add(node_a)
            path_to[node_a] = None
            found = False
            path_lenght = 0
            while len(queue) != 0:
                current_node = queue.pop(0)
                if current_node == node_b:
                    found = True
                    break
                for neighbour in self.nodes[current_node]:
                    if neighbour not in visited:
                        path_to[neighbour] = current_node
                        visited.add(neighbour)
                        queue.append(neighbour)
            if found:
                while path_to[node_b] is not None:
                    path_lenght += 1
                    node_b = path_to[node_b]
            if path_lenght != 0:
                return path_lenght
            else:
                return -1
        else:
            raise ValueError("Nodes are not strings")

graph = DirectedGraph()
graph.add_edge("Vladislav", "Dilyan")
graph.add_edge("Dilyan", "Martin")
graph.add_edge("Vladislav", "Rado")
print(graph.get_neighbors_for("Vladislav"))
print(graph.path_between("Vladislav","Martin"))
print(graph.get_network_for("VladislavAtanasov"))
print(graph.nodes)
