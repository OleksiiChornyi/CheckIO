def backward_string_by_word(text: str) -> str:
    if len(text) == 0:
        return ''
    i: int = 0
    s: str = ""
    st: str = ""
    text += " "
    while i < len(text):
        s = text[i:text.find(" ")]
        st += "".join(reversed(s)) + " "
        i = text.find(" ")
        text = text[i+1:len(text)]
        i = 0
    return st[0:len(st)-1]


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")

