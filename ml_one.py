i, wholepack, net = int(input()), [], {}
for j in range (i):
    wholepack += [input().split(';')]

for team in wholepack:
    if team[0] not in net:
        net[team[0]] = [0,0,0,0,0]
        net[team[0]][0] += 1
        if int(team[1]) > int(team[3]):
            net[team[0]][1] += 1
            net[team[0]][4] += 3
        elif int(team[1]) < int(team[3]):
            net[team[0]][3] += 1
        else:
            net[team[0]][2] += 1
            net[team[0]][4] += 1

    else:
        net[team[0]][0] += 1
        if int(team[1]) > int(team[3]):
            net[team[0]][1] += 1
            net[team[0]][4] += 3
        elif int(team[1]) < int(team[3]):
            net[team[0]][3] += 1
        else:
            net[team[0]][2] += 1
            net[team[0]][4] += 1

    if team[2] not in net:
        net[team[2]] = [0,0,0,0,0]
        net[team[2]][0] += 1
        if int(team[1]) < int(team[3]):
            net[team[2]][1] += 1
            net[team[2]][4] += 3
        elif int(team[1]) > int(team[3]):
            net[team[2]][3] += 1
        else:
            net[team[2]][2] += 1
            net[team[2]][4] += 1

    else:
        net[team[2]][0] += 1
        if int(team[1]) < int(team[3]):
            net[team[2]][1] += 1
            net[team[2]][4] += 3
        elif int(team[1]) > int(team[3]):
            net[team[2]][3] += 1
        else:
            net[team[2]][2] += 1
            net[team[2]][4] += 1

for key, value in net.items():
    print(key,end=':')
    print(*value, sep=' ')
