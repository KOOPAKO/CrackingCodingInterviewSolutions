def palindrome_permutation(input: str) -> bool:
    """
    Checks if a string is a permutation of a palindrome.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    map = [0] * 128  # assumption
    input = input.lower()
    for char in input:
        if char != " ":  # ignore spaces
            assert ord(char) < 128, "input contains non-ASCII character"
            map[ord(char)] += 1

    odd_count = 0
    total_count = 0
    for count in map:
        total_count += count
        if count % 2 == 1:
            odd_count += 1
            if odd_count > 1:
                return False

    # if input length is even, there should be no odd counts
    if total_count % 2 == 0 and odd_count == 1:
        return False

    return True
