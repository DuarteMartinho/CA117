#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name="", age=0, doctor=""):
        self.name = name
        self.age = age
        self.doctor = doctor

    def __eq__(self, other):
        return self == other

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}\nDoctor: {self.doctor}'

class Ward(object):
    def __init__(self):
        self.patients = {}

    def add(self, objToAdd):
        self.patients[objToAdd.name] = objToAdd

    def lookup(self, name):
        try:
            return self.patients[name]
        except KeyError:
            return None

    def remove(self, name):
        self.patients.pop(name)
