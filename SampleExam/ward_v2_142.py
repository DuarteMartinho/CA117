#!/usr/bin/env python3

class Patient(object):

    def __init__(self, name="", age=0, doctor="", meds=[]):
        self.name = name
        self.age = age
        self.doctor = doctor
        self.meds = meds

    def __str__(self):
        ans = 'Name: ' + self.name + '\nAge: ' + str(self.age) + '\nMedications: ' + ", ".join(self.meds) + '\nDoctor: ' + self.doctor
        return ans

class Ward(object):
    def __init__(self):
        self.patients = {}
        self.patients_by_medication = []

    def add(self, objToAdd):
        self.patients[objToAdd.name] = objToAdd

    def lookup(self, name):
        try:
            return self.patients[name]
        except KeyError:
            return None

    def get_patients_by_medication(self, medname):
        self.patients_by_medication = []
        # print(medname)
        for k, v in self.patients.items():
            # print(k, v.meds)
            if medname in v.meds:
                self.patients_by_medication.append(v)
        return self.patients_by_medication

    def remove(self, name):
        self.patients.pop(name)
