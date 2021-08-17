import string

def is_pangram(s):
    alp = ['a', 'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n',  'o',  'p',  'q',  'r',  's',  't',  'u', 'v',  'w', 'x', 'y', 'z']
    if len(s) < 26:
        return False
    s = s.lower()
    for i in alp:
        if s.count(i) == 0:
            return False
    return True
