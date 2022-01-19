from re import findall
import sys

from patterns_062 import date, phone, email, ldate

def main():

    # Verify regular expressions are not overly long
    assert(len(date) < 40)
    assert(len(phone) < 40)
    assert(len(email) < 40)
    assert(len(ldate) < 80)

    s = sys.stdin.read()

    datelist = findall(date, s)
    print(f'Dates: {datelist}')

    phonelist = findall(phone, s)
    print(f'Phones: {phonelist}')

    emaillist = findall(email, s)
    print(f'Emails: {emaillist}')

    ldatelist = findall(ldate, s)
    print(f'Long dates: {ldatelist}')

if __name__ == '__main__':
    main()