#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name="", age=0, doctor="", meds=[]):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.meds = meds

    def __eq__(self, other):
        return self == other

    def __str__(self):
        ans = 'Name: ' + self.name + '\nAge: ' + str(self.age) + '\nMedications: ' + ", ".join(self.meds) + '\nDoctor: ' + self.doctor
        return ans
