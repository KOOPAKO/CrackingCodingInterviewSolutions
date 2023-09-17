def one_away(str1: str, str2: str) -> bool:
    """
    Checks if two strings are one edit (or zero edits) away.
    Operation: insert, remove, replace
    """
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) == len(str2):
        return check_replace(str1, str2)
    else:
        return check_delete_insert(str1, str2)


def check_replace(str1: str, str2: str) -> bool:
    """
    Checks if two strings are one replacement away.
    """
    found_difference = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found_difference:
                return False
            found_difference = True
    return True


def check_delete_insert(str1: str, str2: str) -> bool:
    """
    Checks if two strings are one deletion or insertion away. (which is the
    same operation from the perspective of this algorithm)
    """
    assert len(str1) != len(str2), "Strings must have different lengths."

    if len(str1) > len(str2):
        longer = str1
        shorter = str2
    else:
        longer = str2
        shorter = str1

    index = 0
    change_occurred = False

    for char in shorter:
        if char != longer[index]:
            if change_occurred:
                return False
            elif char == longer[index + 1]:
                change_occurred = True
                index += 1
            else:
                return False
        index += 1

    return True
