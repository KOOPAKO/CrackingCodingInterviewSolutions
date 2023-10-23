def is_rotation(string, candidate):
    if len(string) != len(candidate):
        return False
    
    for i in range(len(string)):
        if string[i:] + string[:i] == candidate:
            return True
    return False