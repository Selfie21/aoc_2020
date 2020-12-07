f = open("inputs/second.txt", "r")
lines = f.read().splitlines()

counter = 0
secondcounter = 0
for line in lines:
    loginData = line.rsplit(": ", 1)
    password = loginData[1]
    constraints = loginData[0].rsplit(" ", 1)
    lowNum, highNum = constraints[0].rsplit("-", 1)
    letter = constraints[1]

    if (password.count(letter) >= int(lowNum)) and (password.count(letter) <= int(highNum)):
        counter = counter + 1

    try:
        if (password[int(lowNum)-1] == letter) and (password[int(highNum)-1] != letter):
            secondcounter = secondcounter + 1
        elif (password[int(lowNum)-1] != letter) and (password[int(highNum)-1] == letter):
            secondcounter = secondcounter + 1
    except:
        continue

print(counter)
print(secondcounter)
