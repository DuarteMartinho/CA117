#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title="", duration=0, artist=[]):
        self.title = title
        self.duration = duration
        self.artist = artist

    def __str__(self):
        hour = self.duration // 60
        mins = str(self.duration % 60)
        if len(mins) == 1:
            mins = "0" + mins
        duration = str(hour) + ":" + mins
        return f'Title: {self.title}\nBy: {", ".join(self.artist)}\nDuration: {duration}'

    def add_artist(self, artist):
        self.artist.append(artist)
