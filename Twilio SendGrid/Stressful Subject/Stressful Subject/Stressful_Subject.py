import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    return (subj.isupper() or subj.endswith("!!!") or any(re.search('+[.!-]*'.join(c for c in word), subj.lower()) for word in ['help', 'asap', 'urgent']))

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')

