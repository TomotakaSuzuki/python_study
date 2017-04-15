try:
    while True:
        mozi = input()
        list(mozi)
        mozi = [int(i) for i in mozi]
        l_mozi = len(mozi)
        fg = True
        while fg:
            if l_mozi < 2:
                fg = False
            for j in range(l_mozi-1):
                if abs(mozi[j] - mozi[j+1]) == 1:
                    del mozi[j:j+2]
                    l_mozi = len(mozi)
                    break
                if j == l_mozi-2:
                    fg = False
        for k in mozi:
            print(k, end="")
except EOFError:
    pass
