f = open('input.txt', 'r')
lines = f.readlines()
n = len(lines)

m = int(lines[n-1])
pair = []

for i in range(n-1):
    pair.append(lines[i].split(":"))
    pair[i][1] = pair[i][1].replace("\n", "")

pair.sort ()

for j in range(n-1):
    if m % int(pair[j][0]) == 0:
        print(pair[j][1], end="")
