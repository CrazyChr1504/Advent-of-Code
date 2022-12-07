def import_file(file_name):
    with open(file_name, "rt") as f:
        return f.readline().strip()
def part_one():
    line = import_file("Aoc_Inputs\Advent_06_22.txt")
    for i in range(4, len(line)):
        if len(set(line[i-4:i])) == 4:
            print(i)
            break
def part_two():
    line = import_file("Aoc_Inputs\Advent_06_22.txt")
    for i in range(14, len(line)):
        if len(set(line[i-14:i])) == 14:
            print(i)
            break
if __name__ == "__main__":
    part_one()
    part_two()