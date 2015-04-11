import unittest
from Socialnetwork import Panda
from Socialnetwork import PandaSocialNetwork
from Socialnetwork import PandaAlreadyThere

class Test_Panda(unittest.TestCase):

    def setUp(self):
        self.my_account = Panda("Vladislav", "myemail@abv.bg", "male")

    def test_name(self):
        self.assertTrue(isinstance(self.my_account.__name, str))

    def test_name(self):
        self.assertEqual(self.my_account.name(), "Vladislav")

    def test_gender(self):
        self.assertEqual(self.my_account.gender(), "male")

    def test_email(self):
        self.assertEqual(self.my_account.email(), "myemail@abv.bg")

    def test_init(self):
        self.assertEqual(self.my_account.name(), "Vladislav")
        self.assertEqual(self.my_account.email(), "myemail@abv.bg")
        self.assertEqual(self.my_account.gender(), "male")

    def test_str(self):
        result = "Panda info: Vladislav myemail@abv.bg male"
        self.assertEqual(self.my_account.__str__(), result)

    def test_eq(self):
        self.assertTrue(self.my_account.__eq__)

    def test_isMale(self):
        self.assertTrue(self.my_account.isMale())

    def test_isFemale(self):
        self.assertFalse(self.my_account.isFemale())

    def test_hash(self):
        result = self.my_account.__hash__()
        self.assertTrue(isinstance(result, int))

class TestPandaSocialNetwork(unittest.TestCase):

    def setUp(self):
        self.my_account = Panda("Stefan", "techo@abv.bg", "male")
        self.network = PandaSocialNetwork()

    def test_add(self):
        self.network.add_panda(self.my_account)
        with self.assertRaises(PandaAlreadyThere):
            self.network.add_panda(self.my_account)

    def test_haspanda(self):
        self.network.add_panda(self.my_account)
        self.assertTrue(self.my_account)

    def test_makefriends(self):
        Stan = Panda("Stanimir", "stan@amasm.bg", "male")
        self.network.add_panda(Stan)
        self.network.add_panda(self.my_account)
        self.network.make_friends(Stan,self.my_account)
        with self.assertRaises(Exception):
            self.network.make_friends(Stan,self.my_account)

    def test_arefriends(self):
        Stan = Panda("Stanimir", "stan@amasm.bg", "male")
        self.network.make_friends(Stan, self.my_account)
        self.assertTrue(Stan in self.network.diction[self.my_account])
        self.assertTrue(self.my_account in self.network.diction[Stan])

    def test_friendsof(self):
        Stan = Panda("Stanimir", "stan@amasm.bg", "male")
        self.network.make_friends(Stan, self.my_account)
        self.assertEqual([Panda('Stanimir', 'stan@amasm.bg', 'male')], self.network.diction[self.my_account])

    def test_connectionlevel(self):
        Stan = Panda("Stanimir", "stan@amasm.bg", "male")
        Yordan = Panda("Yordan", "yori@gmail.bg", "male")
        self.network.make_friends(Stan, self.my_account)
        self.assertEqual(1,self.network.connection_level(Stan, self.my_account))
        self.assertEqual(-1,self.network.connection_level(self.my_account, self.my_account))
        self.assertEqual(False,self.network.connection_level(Yordan, self.my_account))

    def test_areconnected(self):
        Stan = Panda("Stanimir", "stan@amasm.bg", "male")
        self.network.make_friends(Stan, self.my_account)
        self.assertEqual(True,self.network.are_connected(Stan, self.my_account))

    def test_howmanygender(self):
        Stan = Panda("Stanimir", "stan@amasm.bg", "male")
        self.network.make_friends(Stan, self.my_account)
        self.assertEqual(1,self.network.how_many_genders_in_network(1, Stan, "male"))


if __name__ == '__main__':
    unittest.main()


