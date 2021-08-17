def first_non_repeating_letter(string):
    for i in string:
        if (string.upper()).count(i.upper()) == 1:
            return i
    return ''
