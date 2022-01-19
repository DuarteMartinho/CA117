#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title="", duration=0):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f'Title: {self.title}\nDuration: {self.duration}'

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
