def import_file(file_name):
    with open(file_name, "rt") as f:
        file_list = [entry for entry in f.readlines()]
        for i in range(len(file_list)):
            file_list[i] = file_list[i].strip("\n")
    return file_list

if __name__ == "__main__":
    elf_list = []
    cal_calc = 0
    cal_list = import_file("Aoc_Inputs\Advent_01_22.txt")
    for i in range(len(cal_list)):
        if cal_list[i] != "":
            cal_calc += int(cal_list[i])
        else:
            elf_list.append(cal_calc)
            cal_calc = 0
    elf_list.sort()
    print(elf_list[-1])
    cals = elf_list[-1]+elf_list[-2]+elf_list[-3]
    print(cals)