def sum_numbers(text: str) -> int:
    i: int = 0
    d: int = 0
    s: str = ''
    while i < len(text):
        if text[i].isdigit():
            s += text[i]
            i+=1
        else:
            if text[i] == ' ' and s != '':
                d += int(s)
            s = ''
            i+=1
    if s != '' and i==len(text):
        d += int(s)
        s = ''
    return d


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

