f = open("inputs/first.txt", "r")
lines = f.read().splitlines()

x = y = 0
for line in lines:
    tmpx = int(line)
    for line2 in lines:
        tmpy = int(line2)
        if (tmpx+tmpy) == 2020:
            x = tmpx
            y = tmpy
result = x * y

for line in lines:
    tmpx = int(line)
    for line2 in lines:
        tmpy = int(line2)
        for line3 in lines:
            tmpz = int(line3)
            if (tmpx+tmpy+tmpz) == 2020:
                x = tmpx
                y = tmpy
                z = tmpz

result = x*y*z
print(result)
