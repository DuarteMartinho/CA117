def count_letters(s, i=0, c=0):
    if s == ("-" * c):
        return i
    s = s.replace(s[i], "-", 1)
    return count_letters(s, i + 1, c + 1)
