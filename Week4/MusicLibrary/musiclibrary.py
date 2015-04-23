import random
import json
import os.path, os
from tabulate import tabulate
from subprocess import Popen, PIPE
import time
from mutagen.mp3 import MP3


class Song:

    def __init__(self, title, artist, album, lenght):
        self.title = title
        self.artist = artist
        self.album = album
        self.lenght = lenght

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.lenght)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        s1 = self.title == other.title
        s2 = self.artist == other.artist
        s3 = self.album == other.album
        s4 = self.lenght == other.lenght
        return s1 and s2 and s3 and s4

    def __hash__(self):
        return hash(self.title + self.artist + self.album + self.lenght)

    def sec_lenght(self):
        if self.lenght.count(":") > 1:
            hours = self.lenght[: self.lenght.index(":")]
            minutes = self.lenght[self.lenght.index(":")+1:self.lenght.index(":")+3]
            seconds = self.lenght[self.lenght.index(":")+4:]
            return int(hours)*3600 + int(minutes)*60 + int(seconds)
        else:
            hours = self.lenght[: self.lenght.index(":")]
            minutes = self.lenght[self.lenght.index(":")+1:]
            return int(hours)*3600 + int(minutes)*60

    def min_lenght(self):
        if self.lenght.count(":") > 1:
            hours = self.lenght[: self.lenght.index(":")]
            minutes = self.lenght[self.lenght.index(":")+1:self.lenght.index(":")+3]
            return int(hours)*60 + int(minutes)
        else:
            hours = self.lenght[: self.lenght.index(":")]
            minutes = self.lenght[self.lenght.index(":")+1:]
            return int(hours)*60 + int(minutes)

    def hour_lenght(self):
        if self.lenght.count(":") > 1:
            hours = self.lenght[: self.lenght.index(":")]
            return int(hours)
        else:
            hours = self.lenght[: self.lenght.index(":")]
            return int(hours)

    def full_lenght(self):
        return 'The lenght of the song is: {}'.format(self.lenght)

    def leng(self):
        if self.lenght.count(":") > 1:
            hours = self.lenght[: self.lenght.index(":")]
            minutes = self.lenght[self.lenght.index(":")+1:self.lenght.index(":")+3]
            seconds = self.lenght[self.lenght.index(":")+4:]
            new = []
            for x in [hours, minutes, seconds]:
                new.append(int(x))
            return new
        else:
            hours = self.lenght[: self.lenght.index(":")]
            minutes = self.lenght[self.lenght.index(":")+1:]
            for x in [hours, minutes]:
                new.append(int(x))
            return new

class Playlist:
    def __init__(self, name, repeat = False, shuffle = False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.list = []
        self.played = set()
        self.index = 0

    def add_song(self, song):
        self.list.append(song)

    def remove_song(self, song):
        self.list.remove(song)

    def total_lenght(self):
        sum_m = 0
        sum_h = 0
        sum_s = 0
        for x in self.list:
            new = x.lenght.split(":")
            sum_h += int(new[0])
            sum_m += int(new[1])
            sum_s += int(new[2])
        if len(str(sum_h)) < 2 and len(str(sum_s)) < 2 and len(str(sum_m)) < 2:
            return "0{}:0{}:0{}".format(sum_h, sum_m, sum_s)
        elif len(str(sum_h)) < 2 and len(str(sum_m)) < 2:
            return "0{}:0{}:{}".format(sum_h, sum_m, sum_s)
        elif len(str(sum_h)) < 2 and len(str(sum_s)) < 2:
            return "0{}:{}:0{}".format(sum_h, sum_m, sum_s)
        elif len(str(sum_s)) < 2 and len(str(sum_m)) < 2:
            return "{}:0{}:0{}".format(sum_h, sum_m, sum_s)
        elif len(str(sum_h)) < 2:
            return "0{}:{}:{}".format(sum_h, sum_m, sum_s)
        elif len(str(sum_s)) < 2:
            return "{}:{}:0{}".format(sum_h, sum_m, sum_s)
        elif len(str(sum_m)) < 2:
            return "{}:0{}:{}".format(sum_h, sum_m, sum_s)
        else:
            return "{}:{}:{}".format(sum_h, sum_m, sum_s)

    def artists(self):
        diction = {}
        count_songs = 0
        for song in self.list:
            if song.artist in diction:
                count_songs +=1
                diction[song.artist] = count_songs
            else:
                count_songs = 1
                diction[song.artist] = count_songs
        return diction

    def has_next_song(self):
        return self.index < len(self.list)

    def random_song(self):
        random_song = random.choice(self.list)
        while random_song in self.played:
            random_song = random.choice(self.list)
        self.played.add(random_song)
        if len(self.played) == len(self.list):
            self.played = set()
        return random_song

    def next_song(self):
        if self.repeat == "SONG":
            return self.list[self.index]
        if self.shuffle:
            return self.random_song()
        if not self.has_next_song() and self.repeat == False:
            raise Exception("End of playlist")
        if not self.has_next_song() and self.repeat == True:
            self.index = 0
        song = self.list[self.index]
        self.index += 1
        return song

    def pprint_playlist(self):
        headers = ["Artist", "Song", "Lenght"]
        table = []
        for song in self.list:
            table.append([song.artist, song.title, song.lenght])
        return tabulate(table, headers=headers)

    def to_json(self):
        json_play = []
        for song in self.list:
            json_play.append(repr(song))
        playlist = {
        "name": self.name,
        "songs": json_play,
        }
        return playlist

    def save(self):
        if " " in self.name:
            new_name = self.name.replace(" ", "-")
            file_name = new_name + ".json"
        else:
            file_name = self.name + ".json"
        save_path = "/media/vladislav/D82809082808E6FA/PythonHB/Week3/W303/playlist_data"
        complete_name = os.path.join(save_path, file_name)
        json_string = json.dumps(self.to_json(), indent=4)
        with open(complete_name, "w") as f:
            f.write(json_string)

    @staticmethod
    def load(path):
        with open(path, "r") as f:
            content = f.read()
            return json.loads(content)

class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        real_playlist = []
        for root, dirs, files in os.walk(self.path):
            for name in files:
                real_playlist.append([str(name)])
        return tabulate(real_playlist, tablefmt="fancy_grid")

    def _my_playlist(self):
        my_playlist = []
        for root, dirs, files in os.walk(self.path):
            for name in files:
                my_playlist.append(str(name))
        random_song = random.choice(my_playlist)
        return random_song

    def play(self, song):
        p = Popen(["mpg123", song], stdout=PIPE, stderr=PIPE)
        return p

    def len_playlist(self):
        result = 0
        for root, dirs, files in os.walk(self.path):
            for name in files:
                result += 1
        return result

    def run(self):
        count = 0
        played = []
        while count < self.len_playlist():
            name = self._my_playlist()
            full = os.path.join(self.path, name)
            audio = MP3(full)
            if name not in played:
                if count >= 1:
                    nexts = "Next song: {}".format(name)
                    print('{0:^180}'.format(nexts))
                curr = "Currently playing: {}".format(name)
                print('{0:^180}'.format(curr))
                length = str(audio.info.length/60.0)
                mins = length[0:1]
                secs = length[2:3]
                leng ="Length: {} minutes and {} seconds".format(mins, secs)
                print('{0:^180}'.format(leng))
                enj = "ENJOY IT!"
                print('{0:^180}'.format(enj))
                self.play(full)
                time.sleep(audio.info.length)
                count += 1
            played.append(name)
        return "End Of Playlist"

    def save_mylist(self):
        with open("table.txt", "w") as f:
            f.write(self.generate_playlist())


def stop():
    self.play().kill()

s = Song("Odin","Manowar","The Sons of Odin","3:44:12")
s1 = Song("Odin","Manowar","Odin","6:26:21")
s2 = Song("Crying in the rain", "Whitesnake", "WhiteAlbum", "0:21:31")
code_songs = Playlist(name="For Code", repeat=True, shuffle = True)
#print(s.full_lenght())
code_songs.add_song(s)
code_songs.add_song(s1)
code_songs.add_song(s2)
crawler = MusicCrawler("/media/vladislav/D82809082808E6FA/Music/NewSongs/Test/")
playlist = crawler.generate_playlist()
#print(code_songs.total_lenght())
#print(code_songs.list)
#print(code_songs.artists())
#print(code_songs.next_song())
#print(code_songs.next_song())
#print(code_songs.next_song())
#print(code_songs.next_song())
#print(code_songs.pprint_playlist())
#print(code_songs.save())
#print(code_songs.name)
#print(code_songs.load("For-Code.json"))
print(playlist)
