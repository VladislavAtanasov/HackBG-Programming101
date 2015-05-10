import requests
from keys import CLIENT_ID, CLIENT_SECRET
from dirgraph import DirectedGraph

class GitHub:

    def __init__(self, user, level):
        self.user = user
        self.level = level
        self.git = DirectedGraph()

    def build_network(self, start, level):
        if not (0 <= level <= 3):
            raise ValueError
        visited = set()
        queue= []
        visited.add(start)
        queue.append((0,start))
        while len(queue) != 0 :
            current_level, current_node = queue.pop(0)
            if current_level > level:
                break
            network = self.git.get_network_for(current_node)
            for foll in network["followers"]:
                if foll not in visited:
                    self.git.add_edge(foll, current_node)
                    visited.add(foll)
                    queue.append((current_level+1,foll))
            for following in network['following']:
                self.git.add_edge(current_node, following)
                if following not in visited:
                    visited.add(following)
                    queue.append((current_level + 1, following))
        return self.git.nodes

    def do_you_follow(self, user):
        return (user in self.git.get_neighbors_for(self.user))


    def do_you_follow_indirectly(self, other_user):
        return self.git.path_between(self.user, other_user) > 1

    def does_he_she_follows(self, other_user):
        if type(self.git.get_neighbors_for(other_user)) is set:
            return (self.user in self.git.get_neighbors_for(other_user))
        raise ValueError("NoSuchUserinCurrentSocLevel")

    def does_he_she_follows_indirectly(self, other_user):
        if type(self.git.get_neighbors_for(other_user)) is set:
            return self.git.path_between(other_user, self.user) > 1
        raise ValueError("NoSuchUserinCurrentSocLevel")

    def who_follows_you_back(self):
        feedback = []
        net_user = self.git.get_network_for(self.user)
        for user in net_user["followers"]:
            for foll in net_user["following"]:
                if user == foll:
                    feedback.append(user)
        return feedback

def main():
    user = GitHub("VladislavAtanasov",3)
    print(user.who_follows_you_back())

if __name__ == '__main__':
    main()
