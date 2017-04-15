try:
    while True:
        cds = input()
        list(cds)
        cds = [int(i) for i in cds]
        cds.sort()
        if cds[0] != 0:
            print(max(cds))
        else:
            print(cds[1])
except EOFError:
    pass

