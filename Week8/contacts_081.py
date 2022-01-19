#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "{} {} {}".format(self.name, self.phone, self.email)

class ContactList(object):

    def __init__(self, d={}):
        self.d = d

    def __str__(self):
        output = "Contact list\n------------"
        for k, v in sorted(self.d.items()):
            output += "\n" + self.d[k]
        return output

    def add_contact(self, contact):
        self.d[contact.name] = contact.name + " " + contact.phone + " " + contact.email
        return self

    def del_contact(self, contact):
        try:
            self.d.pop(contact)
        except KeyError:
            return self
        return self

    def get_contact(self, contact):
        try:
            return self.d[contact]
        except KeyError:
            return "None"
