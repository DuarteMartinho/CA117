from student_v4_121 import Student

def main():

    s1 = Student('Boris Spassky', 'Dublin', 17345654)
    s2 = Student('Bobby Fischer', 'Cork', 17907321)
    s3 = Student('Mikhail Tal', 'Belfast', 17884786)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)
    print(s1)

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)
    print(s2)

    s3.add_mark('CA103', 60)
    s3.add_mark('CA106', 50)
    print(s3)

    assert(s1 == s3)
    assert(s1 < s2)
    assert(s2 > s3)

if __name__ == '__main__':
    main()