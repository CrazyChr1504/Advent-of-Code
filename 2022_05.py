with open("Aoc_Inputs\Advent_05_22.txt") as f:
    f_piles, f_ins = f.read().split("\n\n")

f_piles = f_piles.splitlines()
f_piles = f_piles[:-1]
f_ins = f_ins.splitlines()

piles = [[] for i in range(0, len(f_piles) + 1)]

for i in range(-1, (-1 - len(f_piles)), -1):
    for ind, pkg in enumerate(f_piles[i][1::4]):
        if pkg != " ":
            piles[ind].append(pkg)

piles_two = [x.copy() for x in piles]

ins = []
for i in f_ins:
    _, amount, _, fro, _, to = i.split()
    ins.append([int(amount), int(fro), int(to)])

for i in ins:
    amount, fro, to = i
    for _ in range(0, amount):
        piles[to - 1].append(piles[fro - 1][-1])
        piles[fro - 1].pop()

pkg_one = ""

for i in piles:
    pkg_one += i[-1]

for i in ins:
    amount, fro, to = i
    for x in range(0, amount):
        piles_two[to - 1].append(piles_two[fro - 1][0 - amount + x])
    for _ in range(0, amount):
        piles_two[fro - 1].pop()

pkg_two = ""
for i in piles_two:
    pkg_two += i[-1]

print(pkg_one)
print(pkg_two)