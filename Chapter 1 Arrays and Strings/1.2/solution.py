def check_permutation(str1: str, str2: str) -> bool:
    """
    Determines whether one string is a permutation of another string.

    Parameters
    ----------
    str1 : str
        The first string.
    str2 : str
        The second string.

    Returns
    -------
    bool
        True if str1 is a permutation of str2, False otherwise.

    Time Complexity: O(n + m), where n and m are the lengths of str1 and str2,
        respectively.
    Space Complexity: O(n), where n is the length of str1.
    """
    if len(str1) != len(str2):
        return False

    # create a map of the first strings characters with their counts
    map = {}
    for char in str1:
        if map.get(char):
            map[char] += 1
        else:
            map[char] = 1

    # now loop through characters of the second string subtracting each of the
    # characters locations by 1
    for char in str2:
        if map.get(char):
            map[char] -= 1
        else:
            return False  # a character mismatch has been identified

    # next do a third loop of original array to check that all char values are
    # strictly 0.
    for char in str1:
        if map[char] != 0:  # char will always exist due to second loop
            return False
    return True
