OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction" and (x and y):
        return 1
    if operation == "disjunction" and (x or y):
        return 1
    if operation == "implication" and ((not x) or y):
        return 1
    if operation == "exclusive" and (x ^ y):
        return 1
    if operation == "equivalence" and not(x ^ y):
        return 1
    else:
        return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('All good! Go and check the mission.')

