"""Iterator Pattern - Pattern

This file shows the Pattern example in the Iterator Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from typing import List
from abc import ABC, abstractmethod


class Song:
    def __init__(self, title: str):
        self.__title: str = title

    def get_title(self):
        return self.__title


# Abstract Class
class Iterator:
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


class PlaylistIterator(Iterator):
    def __init__(self, song_list: List[Song]):
        self.__song_list = song_list
        self.__position = 0

    def has_next(self):
        if self.__position < len(self.__song_list):
            return True
        return False

    def next(self) -> Song | None:
        while self.has_next() == True:
            song = self.__song_list[self.__position]
            self.__position += 1
            return song
        return None


class Playlist:
    def __init__(self):
        self.__playlist: List[Song] = []

    def add_song(self, song: Song):
        self.__playlist.append(song)

    def create_iterator(self) -> PlaylistIterator:
        return PlaylistIterator(self.__playlist)


playlist = Playlist()
playlist.add_song(Song("song1"))
playlist.add_song(Song("song2"))
playlist.add_song(Song("song3"))
playlist.add_song(Song("song4"))

iterator = playlist.create_iterator()

while iterator.has_next():
    print(iterator.next().get_title())

# Revision summary:
# - Part of the Iterator Pattern examples.
# - Shows the Pattern example.
# - Use this file to review the pattern and understand its purpose.
