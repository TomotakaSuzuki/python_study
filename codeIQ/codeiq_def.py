if __name__ == '__main__':
    for line i in fileinput.input():
        cds = list(map(int, line.strip().split()))
        a, b = cds[0], cds[1]
        print(a, b)


