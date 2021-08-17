import string

def is_pangram(s):
    if len(s) < 26:
        return False
    s = s.lower()
    for i in range(0, 26):
        if s.count(chr(i+97)) == 0:
            return False
        
    return True
