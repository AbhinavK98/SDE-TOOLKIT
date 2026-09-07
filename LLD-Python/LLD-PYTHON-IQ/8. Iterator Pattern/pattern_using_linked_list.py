"""Iterator Pattern - Pattern Using Linked List

This file shows the Pattern Using Linked List example in the Iterator Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


# ============= SONG CLASS =============


class Song:
    def __init__(self, title: str):
        self.__title: str = title

    def get_title(self):
        return self.__title


# ============= NODE CLASS (for Linked List) =============


class Node:
    """Node for linked list - contains Song and pointer to next Node"""

    def __init__(self, song: Song):
        self.song: Song = song
        self.next: Node | None = None


# ============= ITERATOR INTERFACE =============


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass


# ============= CONCRETE ITERATOR =============


class PlaylistIterator(Iterator):
    """Iterator for linked list based playlist"""

    def __init__(self, head: Node | None):
        self.__current: Node | None = head

    def has_next(self) -> bool:
        """Check if there's a next node"""
        return self.__current is not None

    def next(self) -> Song | None:
        """Get current song and move to next node"""
        if self.has_next():
            song = self.__current.song
            self.__current = self.__current.next
            return song
        return None


# ============= PLAYLIST CLASS (Linked List) =============


class Playlist:
    """Playlist implemented as a linked list"""

    def __init__(self):
        self.__head: Node | None = None  # First node
        self.__tail: Node | None = None  # Last node

    def add_song(self, song: Song):
        """Add song to the end of linked list"""
        new_node = Node(song)

        if self.__head is None:
            # First song - both head and tail point to it
            self.__head = new_node
            self.__tail = new_node
        else:
            # Add to end - link current tail to new node
            self.__tail.next = new_node
            self.__tail = new_node

    def create_iterator(self) -> PlaylistIterator:
        """Create iterator starting from head of linked list"""
        return PlaylistIterator(self.__head)


# ============= CLIENT CODE =============

playlist = Playlist()
playlist.add_song(Song("song1"))
playlist.add_song(Song("song2"))
playlist.add_song(Song("song3"))
playlist.add_song(Song("song4"))

iterator = playlist.create_iterator()

print("Playing all songs:")
while iterator.has_next():
    print(f"{iterator.next().get_title()}")

# Revision summary:
# - Part of the Iterator Pattern examples.
# - Shows the Pattern Using Linked List example.
# - Use this file to review the pattern and understand its purpose.
