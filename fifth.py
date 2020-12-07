import re


def get_mid(low, high):
    return int((high - low) / 2)


def binary_search(low, high, input):
    while low <= high:
        mid = get_mid(low, high)
        if (input[0] == 'F' or input[0] == "L") and mid < 1:
            return low
        elif (input[0] == 'B' or input[0] == "R") and mid < 1:
            return high
        elif input[0] == "F" or input[0] == "L":
            high -= mid + 1
            input = input[1:]
        elif input[0] == 'B' or input[0] == "R":
            low += mid + 1
            input = input[1:]


MAX_ROW = 127
MAX_COLUMN = 7

f = open("inputs/fifth.txt", "r")
tickets = f.read().splitlines()
idents = []
checker = []
for ticket in tickets:
    row = binary_search(0, MAX_ROW, ticket)
    column = binary_search(0, MAX_COLUMN, ticket[7:])
    ident = row * 8 + column
    idents.append(ident)

idents.sort()
i = 0
while idents[i] == (idents[i+1] - 1):
    i += 1

print(max(idents))
print(idents[i] + 1)

print("")
