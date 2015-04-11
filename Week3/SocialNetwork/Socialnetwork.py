import re
import json
import pprint


class Panda:

    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender

    def email(self):
        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", self.__email):
            raise ValueError
        return self.__email

    def name(self):
        if len(self.__name) <= 0 or not isinstance(self.__name, str):
            raise ValueError
        return self.__name

    def gender(self):
        return self.__gender

    def __str__(self):
        return "Panda info: {} {} {}".format(self.__name, self.__email, self.__gender)

    def __repr__(self):
        return "Panda('{}','{}', '{}')".format(self.__name, self.__email, self.__gender)

    def __eq__(self, other):
        equal_names = self.__name == other.__name
        equal_email = self.__email == other.__email
        equal_genders = self.__gender == other.__gender
        return equal_genders and equal_email and equal_names

    def isMale(self):
        if self.__gender == "male":
            return True
        return False

    def isFemale(self):
        if self.__gender == "female":
            return True
        return False

    def __hash__(self):
        return hash(self.__name + self.__email + self.__gender)

class PandaAlreadyThere(Exception):
    pass

class PandaSocialNetwork:

    def __init__(self):
        self.diction = {}

    def add_panda(self, panda):
        if self.has_panda(panda):
            raise PandaAlreadyThere
        else:
            self.diction[panda] = []

    def has_panda(self, panda):
        return panda in self.diction

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if self.are_friends(panda1, panda2):
            raise Exception("PandasAlreadyFriends")
        self.diction[panda1].append(panda2)
        self.diction[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        if panda2 in self.diction[panda1] and panda1 in self.diction[panda2]:
            return True
        return False

    def friends_of(self, panda):
        if panda in self.diction:
            return self.diction[panda]
        return False

    def connection_level(self, panda1, panda2):
        if self.has_panda(panda1) and self.has_panda(panda2):
            visited = set()
            queue = []
            path_to = {}
            queue.append(panda1)
            visited.add(panda1)
            path_to[panda1.__str__()] = None
            found = False
            path_lenght = 0
            while len(queue) != 0:
                current_node = queue.pop(0)
                if current_node == panda2:
                    found = True
                    break
                for neighbour in self.diction[current_node]:
                    if neighbour not in visited:
                        path_to[neighbour.__str__()] = current_node
                        visited.add(neighbour)
                        queue.append(neighbour)
            if found:
                while path_to[panda2.__str__()] is not None :
                    path_lenght += 1
                    panda2 = path_to[panda2.__str__()]
            if path_lenght != 0:
                return path_lenght
            else:
                return -1
        else:
            return False

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) != -1

    def how_many_genders_in_network(self, level, panda, gender):
        count = 0
        for friend in self.diction.keys():
            if friend != panda:
                if level == self.connection_level(panda, friend) and gender == friend.gender():
                    count += 1
        return count

    def prepare_json(self):
        data = {}
        for pandas in self.diction:
            if repr(pandas) not in data:
                data[repr(pandas)] = []
            for friends in self.diction[pandas]:
                data[repr(pandas)].append(repr(friends))
        return data

    def save(self, file_name):

        with open(file_name,"w") as f:
            json_string = json.dumps(self.prepare_json(), indent = 4)
            f.write(json_string)

    def load(self, file_name):
        with open(file_name, "r") as f:
            contents = f.read()
            return json.loads(contents)

def main():

    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    vladislav = Panda("vladislav", "vladislav@pandamail.com", "male")
    tony = Panda("Tony", "tony@pandamail.com", "female")
    pesho = Panda("Pesho", "pesho@pandamail.com", "male")
    gosho = Panda("Gosho", "gosho@pandamail.com", "female")
    SocNetwork = PandaSocialNetwork()
    for panda in [ivo, vladislav, tony, pesho, gosho]:
        SocNetwork.add_panda(panda)
    SocNetwork.make_friends(ivo, vladislav)
    SocNetwork.make_friends(vladislav, tony)
    SocNetwork.make_friends(ivo, gosho)
    SocNetwork.save("net.json")
    print(SocNetwork.are_friends(ivo, vladislav))
    print(SocNetwork.are_friends(ivo, tony))
    print(SocNetwork.friends_of(vladislav))
    print(SocNetwork.friends_of(ivo))
    print(SocNetwork.friends_of(tony))
    print(SocNetwork.connection_level(ivo, vladislav))
    print(SocNetwork.connection_level(ivo, tony))
    print(SocNetwork.are_connected(ivo, tony))
    print(SocNetwork.how_many_genders_in_network(2, ivo, "female"))
    print(SocNetwork.load("net.json"))

if __name__ == '__main__':
    main()
