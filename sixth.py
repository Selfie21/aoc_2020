f = open("inputs/sixth.txt", "r")


def check_valid(all_chars, group_size):
    tmp = 0
    for v in all_chars.values():
        if v > group_size:
            tmp += 1
    return tmp


groups = f.read().rsplit("\n\n")
first = second = 0

for group in groups:
    hashtable = {}
    for character in group:
        if character != '\n':
            hashtable[character] = 1
        first += len(hashtable)

for group in groups:
    hashtable = {}
    groupMembers = 0
    for character in group:
        if character != '\n':
            if character in hashtable:
                hashtable[character] += 1
            else:
                hashtable[character] = 1
        else:
            groupMembers += 1

    second += check_valid(hashtable, groupMembers)


print(first)
print(second)