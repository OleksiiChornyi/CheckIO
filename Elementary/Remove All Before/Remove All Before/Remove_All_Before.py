from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    items.append(border)
    l: int = len(items)
    i: int = -1
    if items.index(border, 0, l) == len(items)-1:
        items.remove(border)
        return items
    else:
        items.pop(len(items)-1)
    l = len(items)
    if items.index(border, 0, l) >= 0:
        i = items.index(border, 0, l)-1
        while i >= 0 and i < len(items)-1:
            items.pop(i)
            i = i - 1
            if i == 0:
                items.pop(i)
                break
    return items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")

