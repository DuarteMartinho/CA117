from mp3track_v1_141 import MP3Track

def main():
    t1 = MP3Track('Fools Gold', 604)
    t2 = MP3Track('Shallow', 197)
    t3 = MP3Track('Telephone', 220)

    assert(t1.title == 'Fools Gold')
    assert(t1.duration == 604)

    print(t1)
    print(t2)
    print(t3)

if __name__ == '__main__':
    main()

print("----------------------------------------------")

from mp3track_v2_141 import MP3Track

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])

    print(t1)
    print(t2)
    print(t3)

if __name__ == '__main__':
    main()

print("----------------------------------------------")

from mp3track_v3_141 import MP3Track

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197)

    print(t1)
    print(t2)

    t2.add_artist('Lady Gaga')
    print(t2)

    t2.add_artist('Bradley Cooper')
    print(t2)

if __name__ == '__main__':
    main()

print("----------------------------------------------")

from mp3track_v4_141 import MP3Track

def main():
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])
    t4 = MP3Track('Her Majesty', 34, ['The Beatles'])
    t5 = MP3Track('Seven Seconds', 7, ['Neneh Cherry'])

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)

if __name__ == '__main__':
    main()