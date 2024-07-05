def is_defended(attackers, defenders):
    totalAtkPower = sum(attackers)
    totalDefPower = sum(defenders)
    print("total attack power is: ${totalAtkPower}")
    if len(attackers) > len(defenders):
        longerList = attackers
    else:
        longerList = defenders
    aSurvivors = 0
    dSurvivors = 0
    i = 0
    while i <= len(longerList):
        if attackers[i] > defenders[i]:
            aSurvivors += 1
        elif attackers[i] < defenders[i]:
            dSurvivors += 1
        elif len(attackers) > len(defenders):
            aSurvivors += (len(attackers) - len(defenders))
        elif len(defenders) > len(attackers):
            dSurvivors += (len(defenders) - len(attackers))
        i += 1
    print(aSurvivors)
    print(dSurvivors)
    if dSurvivors > aSurvivors:
        return True
    elif dSurvivors == aSurvivors:
        return totalDefPower >= totalAtkPower
    else:
        return False