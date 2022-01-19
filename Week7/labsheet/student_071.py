class Student(object):

    def __init__(self, surname="", forename="", sid=0, modlist=[]):
        self.surname = surname
        self.forename = forename
        self.sid = sid
        self.modlist = modlist

    def add_module(self, value):
        self.modlist.append(value)

    def del_module(self, value):
        if value in self.modlist:
            self.modlist.remove(value)

    def print_details(self):
        modsentence = " ".join(self.modlist)
        print('ID: {}'.format(self.sid))
        print('Surname: {}'.format(self.surname))
        print('Forename: {}'.format(self.forename))
        print('Modules: {}'.format(modsentence))
