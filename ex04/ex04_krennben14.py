#!/usr/bin/env python3
# Benjamin "krennben14" Krenn [1410418084]
# ProgKonz  -  Exercise 03

#file
name = 'krennben14'
exercise = 'ex04'
f = open('{0}_{1}.out'.format(exercise, name), 'w')

class Song():
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

    def __str__(self):
        return '{0} (Time: {1}) has been bought by {2}.'.format(self.title, self.length, self.artist)

    def __add__(self, other):
        l = self.length + other.length
        return Song(self.artist, '{} and {}'.format(self.title, other.title),l)

class Musicplayer():
    def nowplaying(self, song):
        return 'We are now playing song \'' + song.title + '\'.'


class HurdyGurdy(Song, Musicplayer):
    def __init__(self, song):
        self.song = song

    def play(self):
        return self.nowplaying(self.song)


song1 = Song(name, 'Always look at the bright side of life', 174)
song2 = Song(name, 'Ein Hotdog unten an Hafen', 129)
song3 = Song(name, 'Funaki', 299)
song4 = Song(name, 'I hea di klopfn', 129)
song5 = Song(name, 'Vladimir Putins Cousine', 234)

album = []
album.append(song1)
album.append(song2)
album.append(song3)
album.append(song4)
album.append(song5)

#1:
f.write('1: {}\n'.format(song4))

#2:
def calcavgsonglength(album):
    length = 0
    for song in album:
        length += song.length
    return length / len(album)

f.write('2: {}\n'.format(calcavgsonglength(album)))

#3:
f.write('3: {}\n'.format(song3 + song1 + song4))


#4
h = HurdyGurdy(song3)
f.write('4: {}\n'.format(h.play()))
f.close()
