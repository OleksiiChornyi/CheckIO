from itertools import permutations, product


def checkio(data):
    # replace this for solution
    for operator in product(['', '+', '-', '*', '/'], repeat=5):
        num, exp = operator.count(''), list(data)
        for i in range(4, -1, -1):
            exp.insert(i + 1, operator[i])
        for j in range(num):
            i = exp.index('')
            exp = (exp[:i - 1] + [exp[i - 1] + exp[i + 1]] + exp[i + 2:])
        for k in permutations(range(5 - num)):
            value, k = exp[:], list(k)
            for i in range(5 - num):
                j = k.pop(0)
                for l in range(len(k)):
                    if k[l] > j:
                        k[l] -= 1
                j = 2 * j + 1
                value = (value[:j - 1] + ['(' + value[j - 1] + value[j] + value[j + 1] + ')'] + value[j + 2:])
            try:
                result = eval(value[0])
            except:
                result = None
            finally:
                if result == 100:
                    return False
    return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"

