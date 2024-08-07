'''
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:

1 <= month <= 12
'''


def quarter_of(month):
    if month == 8:
        return 3
    if month == 7:
        return 3
    if month == 9:
        return 3
    
    if 12 // month >= 4:
        return 1
    
    if 12 // month >= 2:
        return 2
    
    if (12 // month) < 2 and (12 // month) > 1.2:
        return 3
    
    if 12 // month <= 1.2:
        return 4