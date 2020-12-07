import re

f = open("inputs/fourth.txt", "r")

constraints = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passports = f.read().rsplit("\n\n")
validPassports = []

first = second = 0

for identification in passports:
    tmp = 0
    for constraint in constraints:
        if constraint in identification:
            tmp += 1
    if tmp >= 7:
        first += 1
        validPassports.append(identification)

print(first)


for identification in validPassports:

    line = identification.replace("\n", " ")

    passport = {k: v for part in line.split(" ") for k, v in [part.split(":")]}
    if (
            int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002 and
            int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020 and
            int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030 and
            re.match("^(1([5-8][0-9]|9[0-3])cm|(59|[6][0-9]|[7][0-6])in)$", passport['hgt']) and
            re.match("#[0-9a-f]{6}", passport['hcl']) and
            re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl']) and
            re.match("^\d{9}$", passport['pid'])
    ):
        second += 1
print(second)
