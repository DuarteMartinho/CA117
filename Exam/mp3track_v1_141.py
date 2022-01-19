#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title="", duration=0):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f'Title: {self.title}\nDuration: {self.duration}'
