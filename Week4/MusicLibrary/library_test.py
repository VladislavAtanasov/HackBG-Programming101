from musiclibrary import Song, Playlist
import unittest

class Test_Library(unittest.TestCase):

    def setUp(self):
        self.my_song = Song("You Shook me all night long","AC/DC","AC/DC","2:44:12")

    def test_init(self):
        self.assertEqual(self.my_song.title, "You Shook me all night long")
        self.assertEqual(self.my_song.artist, "AC/DC")
        self.assertEqual(self.my_song.album, "AC/DC")
        self.assertEqual(self.my_song.lenght, "2:44:12")

    def test_str(self):
        self.assertEqual("AC/DC - You Shook me all night long from AC/DC - 2:44:12",str(self.my_song))

    def test_eq(self):
        new = Song("You Shook me all night long","AC/DC","AC/DC","3:44:12")
        self.assertFalse(self.my_song.__eq__(new))

    def test_hash(self):
        self.assertTrue(isinstance(hash(self.my_song),int))

    def test_seclen(self):
        self.assertEqual(9852, self.my_song.sec_lenght())

    def test_minlen(self):
        self.assertEqual(164, self.my_song.min_lenght())

    def test_hourlen(self):
        self.assertEqual(2, self.my_song.hour_lenght())

    def test_fulllen(self):
        self.assertEqual('The lenght of the song is: 2:44:12', self.my_song.full_lenght())

class Test_Playlist(unittest.TestCase):

    def setUp(self):
        self.my_song = Song("You Shook me all night long","AC/DC","AC/DC","2:44:12")
        self.my_list = []
        self.songs = Playlist(name="For Code", repeat=True, shuffle = True)

    def test_add(self):
        self.songs.add_song(self.my_song)
        self.assertEqual(len(self.songs.list), 1)

    def test_remove(self):
        self.songs.add_song(self.my_song)
        self.songs.remove_song(self.my_song)
        self.assertEqual(len(self.songs.list), 0)

    def test_total(self):
        new = Song("You Shook me all night long","AC/DC","AC/DC","3:14:12")
        self.songs.add_song(self.my_song)
        self.songs.add_song(new)
        self.assertEqual("05:58:24", self.songs.total_lenght())

    def test_artist(self):
        self.songs.add_song(self.my_song)
        self.assertEqual({"AC/DC":1}, self.songs.artists())




if __name__ == '__main__':
    unittest.main()
