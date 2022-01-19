from classlist_v3_121 import Student, Classlist

def main():

    cl = Classlist()
    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)
    s3 = Student('Mikhail Tal', 'Belfast', 17884786)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)

    s3.add_mark('CA103', 80)
    s3.add_mark('CA106', 90)

    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl.least_popular_module())

if __name__ == '__main__':
    main()