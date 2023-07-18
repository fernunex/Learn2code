# Problem name: ECOO '19 R2 P1 - Email
# Code: ecoo19r2p1
# Link: https://dmoj.ca/problem/ecoo19r2p1

def clean(address: str):
    """
    address is a string email address.
    Return cleaned address.
    """

    # Remove from '+' up to but not including '@'
    plus_index = address.find('+')
    at_index = address.find('@')
    if plus_index != -1:
        address = address[:plus_index] + address[at_index:]

    # Remove dots before @ symbol
    at_index = address.find('@')
    i = 0
    before_at = ''
    while i < at_index:
        if address[i] != '.':
            before_at += address[i]
        i += 1
    cleaned = before_at + address[at_index:]

    # Convert to lowercase
    cleaned = cleaned.lower()
    return cleaned

for _ in range(10): # If testing change this range(10) to range(2)
    n = int(input())
    emails = set()
    for _ in range(n):
        email = input()
        email = clean(email)
        emails.add(email)

    print(len(emails))