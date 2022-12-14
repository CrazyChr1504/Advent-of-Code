def import_file(file_name):
    matches = []
    with open(file_name, "rt") as f:
        data = [entry for entry in f.readlines()]
        for line in data:
            line = line.strip("\n")
            matches.append(line)              
        return matches

def part_one():
    tot_points = []
    matches = import_file("Aoc_Inputs\Advent_02_22.txt")
    for match in matches:
        (key, val) = match.split()
        if key == "A":
            if val == "Y":
                tot_points.append(8)
            elif val == "X":
                tot_points.append(4)
            elif val == "Z":
                tot_points.append(3)
        elif key == "B":
            if val == "Y":
                tot_points.append(5)
            elif val == "X":
                tot_points.append(1)
            elif val == "Z":
                tot_points.append(9)
        elif key == "C":
            if val == "Y":
                tot_points.append(2)
            elif val == "X":
                tot_points.append(7)
            elif val == "Z":
                tot_points.append(6)
    print(sum(tot_points))

def part_two():
    tot_points = []
    matches = import_file("Aoc_Inputs\Advent_02_22.txt")
    for match in matches:
        (key, val) = match.split()   
        if key == "A":          
            if val == "Y":
                tot_points.append(4)
            elif val == "X":
                tot_points.append(3)
            elif val == "Z":
                tot_points.append(8)
        elif key == "B":
            if val == "Y":
                tot_points.append(5)
            elif val == "X":
                tot_points.append(1)
            elif val == "Z":
                tot_points.append(9)
        elif key == "C":
            if val == "Y":
                tot_points.append(6)
            elif val == "X":
                tot_points.append(2)
            elif val == "Z":
                tot_points.append(7)
    print(sum(tot_points))
    
if __name__ == "__main__":
    part_one()
    part_two()