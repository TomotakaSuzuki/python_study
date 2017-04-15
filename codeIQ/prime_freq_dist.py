import math
try:
    while True:
        def prime_num(n):
            if n == 2:
                return True
            if n < 2 or n % 2 == 0:
                return False
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
        c = 0
        prime, cut = (int(_) for _ in input().split())
        pri_rank = int(math.log10(prime)+1)
        for n in range(1, prime+cut):
            if prime_num(n) == True:
                if n <= prime:
                    c += 1
            if n % cut == 0:
                print(((pri_rank-int(math.log10(n-cut+1)+1))*'0')+str(n-cut+1)+'-'+((pri_rank-int(math.log10(n)+1))*'0')+str(n)+':'+(c*'*'))
                c = 0
except EOFError:
    pass


