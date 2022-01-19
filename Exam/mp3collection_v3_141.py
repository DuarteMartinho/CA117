#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title="", duration=0, artist=[]):
        self.title = title
        self.duration = duration
        self.artist = artist

    def __str__(self):
        return f'Title: {self.title}\nBy: {", ".join(self.artist)}\nDuration: {self.duration}'

class MP3Collection(object):

    def __init__(self):
        self.tracks = {}

    def add(self, ObjectToAdd):
        self.tracks[ObjectToAdd.title] = ObjectToAdd

    def lookup(self, tracktitle):
        try:
            return self.tracks[tracktitle]
        except KeyError:
            return None

    def remove(self, tracktitle):
        self.tracks.pop(tracktitle)

    def get_mp3s_by_artist(self, artist):
        tracklist = []
        for k, v in (self.tracks.items()):
            if artist in v.artist:
                tracklist.append(v)
        return tracklist

    def __add__(self, other):
        tracksnames = []
        obj = MP3Collection()
        for k, v in self.tracks.items():
            if k not in tracksnames:
                addval = MP3Track(v.title, v.duration, v.artist)
                obj.add(addval)
        for k, v in other.tracks.items():
            if k not in tracksnames:
                addval = MP3Track(v.title, v.duration, v.artist)
                obj.add(addval)
        return obj
