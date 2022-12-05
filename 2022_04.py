def import_file():
    with open("Advent_04_22", 'r') as f:
        return f.readlines()

def part_one():
    pairs = import_file()
    total = 0
    for pair in pairs:
        pair = pair.split(',')
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')
        if int(elf1[0])<=int(elf2[0]) and int(elf1[1])>=int(elf2[1]):
            total +=1
        elif int(elf2[0])<=int(elf1[0]) and int(elf2[1])>=int(elf1[1]):
            total+=1
    print(total)

def part_two():
    pairs = import_file()
    total = 0
    for pair in pairs:
        pair = pair.split(',')
        elf1 = pair[0].split('-')
        elf2 = pair[1].split('-')
        for i in range(int(elf1[0]), int(elf1[1])+1):
            if i in range(int(elf2[0]), int(elf2[1])+1):
                total+=1
                break
    print(total)

if __name__ == "__main__":
    part_one()
    part_two()