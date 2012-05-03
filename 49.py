from helpers import gen_primes
primes = [a for a in gen_primes(10000) if a > 1000]
sets = [sorted(set(str(a))) for a in primes]
groups = {}
for x in range(len(sets)):
    groups.setdefault(str(sets[x]),[]).append(primes[x])

for g in groups:
    group = groups[g]
    if len(group) > 2:
        print(group, end=" ")
        diff = group[1]-group[0]
        count = 0
        for x in range(len(group)-1):
            print(group[x+1]-group[x], end=" ")
        print()


