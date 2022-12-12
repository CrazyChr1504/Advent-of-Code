def import_file():
    with open("Aoc_Inputs\Advent_10_22.txt") as f:
        data = f.read().splitlines()
        return data
        
def part_one():
    data = import_file()
    res = 0
    st = [1]

    for x in data:
        k = x.split()
        if len(k) > 1:
            st.append(0)
            st.append(int(k[1]) )
        else:
            st.append(0)

    for x in [20, 60, 100, 140, 180, 220]:
        res += sum(st[:x]) * x
    print(res)

def part_two():
    data = import_file()
    st = [1]
    sprite = 0
    res = [str() for _ in range(6)]
    
    for x in data:
        k = x.split()
        if len(k) > 1:
            st.append(0)
            st.append(int(k[1]) )
        else:
            st.append(0)

    for i in range(0, 240, 40):
        for j in range(40):
            sprite += st[i + j] if i + j < len(st) else 0
            res[i // 40] += ['.', '#'][j in range(sprite - 1, sprite + 2)]

    for x in res:
        print(x)

if __name__ == "__main__":
    part_one()
    part_two()