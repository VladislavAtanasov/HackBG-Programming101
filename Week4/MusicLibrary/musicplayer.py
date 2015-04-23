import random
import json
import os.path, os
from tabulate import tabulate
from subprocess import Popen, PIPE
import time
from mutagen.mp3 import MP3
import tkinter
import sys
from tkinter import *
import webbrowser

class MusicPlayer:

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
        end = "End Of Playlist"
        return '{0:^180}'.format(end)

    def save_mylist(self):
        with open("table.txt", "w") as f:
            f.write(self.generate_playlist())

    def stop(self):
        return sys.exit()

class App:
    def __init__(self, master, stop, start, lis):
        self.start = start
        self.stop = stop
        self.lis = lis
        self.master=master
        frame = Frame(master, bg="grey", bd=4, takefocus=True, width=900, height=300)
        frame.pack()
        photo = PhotoImage(file="hack.png")
        w = Label(frame, image=photo, cursor="hand2")
        w.photo = photo
        w.bind("<Button-1>", self.callback)
        w.pack(side=TOP)
        title = Label(frame, text="DA Player",width=30,bg="grey", font=("Helvetia",20))
        title.pack(side=TOP)
        self.slogan = Button(frame, text="Run Playlist!", fg="blue",bd=2, width=30,cursor="hand2",overrelief =RAISED, relief=FLAT, command=self.start)
        self.slogan.pack(side=TOP)
        self.button = Button(frame, text="QUIT", fg="red",bd=2,width=30, relief=FLAT,cursor="hand2",overrelief =RAISED, command=self.stop)
        self.button.pack(side=TOP)

    def callback(self, event):
        webbrowser.open_new(r"http://www.hackbulgaria.com")

def main():
    dirlist = input("Enter Playlist's directory: ")
    my_player = MusicPlayer(dirlist)
    playlist = my_player.generate_playlist()
    print(playlist)
    my_player.save_mylist()
    root = Tk()
    app = App(root, my_player.stop, my_player.run, playlist)
    root.title("Music Player")
    root.mainloop()

if __name__ == '__main__':
    main()
