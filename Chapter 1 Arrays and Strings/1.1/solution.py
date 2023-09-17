def is_unique(input: str) -> bool:
    """
    Determines whether an input string has all unique characters.

    Complexity analysis is based on the assumption that the python dictionary
    implementation uses a hash table with O(1) lookup time for all possible
    characters in the input string.

    Time complexity: O(n)
    Space complexity: O(n)

    Args:
        input: The input string.
    """
    map = {}
    for char in input:
        if char in map:
            return False
        map[char] = True
    return True
