def string_compression(input: str) -> str:
    """
    Compresses strings with repeating characters and returns the compressed 
    string if its shorter than the original.
    """
    output_array = []

    for character in input:
        if len(output_array) and output_array[-1][0] == character:
            output_array[-1][1] += 1
        else:
            output_array.append([character, 1])

    potential_output = "".join(f"{comp[0]}{comp[1]}"for comp in output_array)
    if len(potential_output) < len(input):
        return potential_output
    return input
