# Problem name: CCC '13 S1 - From 1987 to 2013
# Code: ccc13s1
# Link: https://dmoj.ca/problem/ccc13s1

def check_distinct_year_true(year: int) -> bool:
    """Check if every digit is different.

    Args:
        year (int): any year (1985, 1000, 25, 658, etc)

    Returns:
        bool: True if any digit of the year is repeated, False otherwise
    """
    year_str = str(year)
    for i in range(len(year_str)):
        if year_str.count(year_str[i]) > 1:
            return False
    return True


def next_distinct_digit_year(Y: int) -> int:
    """Return the next year with all distinct digits after Y.

    Args:
        Y (int): any year

    Returns:
        int: The next year after Y that has unique digits.
    """

    year = Y + 1
    
    while True:
        if check_distinct_year_true(year):
            return year
        year += 1


# Main
Y = int(input())

D = next_distinct_digit_year(Y)

print(D)