f = open("inputs/third.txt", "r")

slope = f.read().splitlines()
rowLength = len(slope[0])


def slope_checker(xAdd, yAdd):
    counter = y = x = 0
    while y + yAdd < len(slope):
        y += yAdd
        x += xAdd

        if slope[y][x % rowLength] == '#':
            counter += 1
    return counter


def multiply(list):
    product = 1
    for item in list:
        product *= item
    return product


second = []
first = slope_checker(3, 1)
second.append(first)
second.append(slope_checker(1, 1))
second.append(slope_checker(5, 1))
second.append(slope_checker(7, 1))
second.append(slope_checker(1, 2))
result = multiply(second)
print(result)










