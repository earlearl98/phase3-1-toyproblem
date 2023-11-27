def solve(s):
    vowels = "aeiou"
    consonant_values = {letter: i for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz", start=1)}
    
    def calculate_value(substring):
        return sum(consonant_values[letter] for letter in substring)
    
    max_value = 0
    current_substring = ""

    for char in s:
        if char not in vowels:
            current_substring += char
        else:
            max_value = max(max_value, calculate_value(current_substring))
            current_substring = ""

    # Check the last substring
    max_value = max(max_value, calculate_value(current_substring))

    return max_value