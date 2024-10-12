def romanToInt(s):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0  # Store final result
    prev_value = 0  # Store prev result

    # map: reverse
    for char in reversed(s):
        value = roman_dict[char]  # current string
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total