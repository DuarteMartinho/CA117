from ward_v1_142 import Patient, Ward

def main():
    p1 = Patient('Mary', 34, 'James Kildare')
    p2 = Patient('Wendy', 40, 'Gregory House')

    w = Ward()

    w.add(p1)
    w.add(p2)

    p = w.lookup('Mary')
    assert(isinstance(p, Patient))
    assert(p.name == 'Mary')
    assert(p.age == 34)

    w.remove('Mary')
    p = w.lookup('Mary')
    assert(p is None)

if __name__ == '__main__':
    main()