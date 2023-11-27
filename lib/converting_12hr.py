def convert_to_24_hour(hour, minute, period):
    if period.lower() == 'pm' and hour != 12:
        hour += 12
    elif period.lower() == 'am' and hour == 12:
        hour = 0

    return f'{hour:02d}{minute:02d}'
    #The :02d means to format the variable as a decimal (d), with at least two digits (2), and pad with zeros if necessary. This ensures that the hour is always represented by at least two digits.

    