# phase3-1-toyproblem

# converting_12hr.py
This function takes an hour, minute, and period ('am' or 'pm') as input and returns a four-digit string representing the time in 24-hour format.

Here's a brief explanation of the code:

If the period is 'pm' and the hour is not 12, add 12 to the hour.
If the period is 'am' and the hour is 12, set the hour to 0.
Format the hour and minute as a four-digit string using f'{hour:02d}{minute:02d}'

-> he :02d means to format the variable as a decimal (d), with at least two digits (2), and pad with zeros if necessary. This ensures that the hour is always represented by at least two digits.

{minute:02d}: Similarly, this is formatting the minute variable in the same way.

So, the entire expression f'{hour:02d}{minute:02d}' is creating a string that represents the time in a four-digit format, with leading zeros if necessary. For example, if hour is 8 and minute is 5, it would result in the string '0805'.

# two_positive_no.py

 My job was to write a function, which takes three integers a, b, and c as arguments, and returns True if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.


You can write a function in Python to solve this challenge. Here's an example:

python
Copy code
def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2


# constant_value.py

This function, solve, takes a lowercase string as input, iterates through the characters, identifies consonant substrings, calculates their values using the provided mapping, and returns the maximum value among these consonant substrings.

Consonants are any letters of the alphabet except "aeiou".We shall assign the following values