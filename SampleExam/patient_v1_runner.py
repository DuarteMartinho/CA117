from patient_v1_142 import Patient

def main():
    p1 = Patient('Mary', 34, 'James Kildare')
    p2 = Patient('Wendy', 40, 'Gregory House')

    assert(p1.name == 'Mary')
    assert(p1.age == 34)
    assert(p1.doctor == 'James Kildare')

    print(p1)
    print(p2)

if __name__ == '__main__':
    main()