def roman_to_int():
    """
    :rtype: int
    """
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = input("Enter a Roman numeral: ")
    result = 0
    prev_value = 0
    for c in s:
        curr_value = roman_dict[c]
        if curr_value > prev_value:
            result += curr_value - 2 * prev_value
        else:
            result += curr_value
        prev_value = curr_value
    return result

integer = roman_to_int()
print("Result: ", integer)