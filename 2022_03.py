def import_file(file_name):
    bags = []
    with open(file_name, "r", encoding="utf-8") as f:
        data = [entry for entry in f.readlines()]
        for line in data:
            line = line.strip("\n")
            bags.append(line)              
        return bags

def part_one():
    same_item = []
    items = []
    count = 0
    bags = import_file("Advent_03_22.txt")
    for item in bags:
        items.append(list(item))
    for char in items:
        for i in range(int(len(char)/2)):
            for x in range(int(len(char)/2), len(char)):
                if char[i] == char[x]: 
                    same_item.append(char[i]) 
                    break
            if char[i] == char[x]:
                break

    for letter in same_item:
        if letter.lower() == "a":
            if letter == "A":
                count += 27
            else:
                count += 1
        elif letter.lower() == "b":
            if letter == "B":
                count += 28
            else:
                count += 2
        elif letter.lower() == "c":
            if letter == "C":
                count += 29
            else:
                count += 3
        elif letter.lower() == "d":
            if letter == "D":
                count += 30
            else:
                count += 4
        elif letter.lower() == "e":
            if letter == "E":
                count += 31
            else:
                count += 5
        elif letter.lower() == "f":
            if letter == "F":
                count += 32
            else:
                count += 6
        elif letter.lower() == "g":
            if letter == "G":
                count += 33
            else:
                count += 7
        elif letter.lower() == "h":
            if letter == "H":
                count += 34
            else:
                count += 8
        elif letter.lower() == "i":
            if letter == "I":
                count += 35
            else:
                count += 9
        elif letter.lower() == "j":
            if letter == "J":
                count += 36
            else:
                count += 10
        elif letter.lower() == "k":
            if letter == "K":
                count += 37
            else:
                count += 11
        elif letter.lower() == "l":
            if letter == "L":
                count += 38
            else:
                count += 12
        elif letter.lower() == "m":
            if letter == "M":
                count += 39
            else:
                count += 13
        elif letter.lower() == "n":
            if letter == "N":
                count += 40
            else:
                count += 14
        elif letter.lower() == "o":
            if letter == "O":
                count += 41
            else:
                count += 15
        elif letter.lower() == "p":
            if letter == "P":
                count += 42
            else:
                count += 16
        elif letter.lower() == "q":
            if letter == "Q":
                count += 43
            else:
                count += 17
        elif letter.lower() == "r":
            if letter == "R":
                count += 44
            else:
                count += 18
        elif letter.lower() == "s":
            if letter == "S":
                count += 45
            else:
                count += 19
        elif letter.lower() == "t":
            if letter == "T":
                count += 46
            else:
                count += 20
        elif letter.lower() == "u":
            if letter == "U":
                count += 47
            else:
                count += 21
        elif letter.lower() == "v":
            if letter == "V":
                count += 48
            else:
                count += 22
        elif letter.lower() == "w":
            if letter == "W":
                count += 49
            else:
                count += 23
        elif letter.lower() == "x":
            if letter == "X":
                count += 50
            else:
                count += 24
        elif letter.lower() == "y":
            if letter == "Y":
                count += 51
            else:
                count += 25
        elif letter.lower() == "z":
            if letter == "Z":
                count += 52
            else:
                count += 26
    print(count)

def part_two():
    same_item = []
    list_1 = []
    list_2 = []
    list_3 = []
    items = []
    counter = 0
    count = 0
    bags = import_file("Advent_03_22.txt")
    for item in bags:
        items.append(list(item))
    
    for _ in range(int(len(items)/3)):
        list_1.append(items[0])
        list_2.append(items[1])
        list_3.append(items[2])
        for i in range(3):
            items.pop(0)

    for lists in list_1:
        for letter in lists:
            if letter in list_2[counter] and letter in list_3[counter]: 
                same_item.append(letter)
                counter+=1
                break

    for letter in same_item:
        if letter.lower() == "a":
            if letter == "A":
                count += 27
            else:
                count += 1
        elif letter.lower() == "b":
            if letter == "B":
                count += 28
            else:
                count += 2
        elif letter.lower() == "c":
            if letter == "C":
                count += 29
            else:
                count += 3
        elif letter.lower() == "d":
            if letter == "D":
                count += 30
            else:
                count += 4
        elif letter.lower() == "e":
            if letter == "E":
                count += 31
            else:
                count += 5
        elif letter.lower() == "f":
            if letter == "F":
                count += 32
            else:
                count += 6
        elif letter.lower() == "g":
            if letter == "G":
                count += 33
            else:
                count += 7
        elif letter.lower() == "h":
            if letter == "H":
                count += 34
            else:
                count += 8
        elif letter.lower() == "i":
            if letter == "I":
                count += 35
            else:
                count += 9
        elif letter.lower() == "j":
            if letter == "J":
                count += 36
            else:
                count += 10
        elif letter.lower() == "k":
            if letter == "K":
                count += 37
            else:
                count += 11
        elif letter.lower() == "l":
            if letter == "L":
                count += 38
            else:
                count += 12
        elif letter.lower() == "m":
            if letter == "M":
                count += 39
            else:
                count += 13
        elif letter.lower() == "n":
            if letter == "N":
                count += 40
            else:
                count += 14
        elif letter.lower() == "o":
            if letter == "O":
                count += 41
            else:
                count += 15
        elif letter.lower() == "p":
            if letter == "P":
                count += 42
            else:
                count += 16
        elif letter.lower() == "q":
            if letter == "Q":
                count += 43
            else:
                count += 17
        elif letter.lower() == "r":
            if letter == "R":
                count += 44
            else:
                count += 18
        elif letter.lower() == "s":
            if letter == "S":
                count += 45
            else:
                count += 19
        elif letter.lower() == "t":
            if letter == "T":
                count += 46
            else:
                count += 20
        elif letter.lower() == "u":
            if letter == "U":
                count += 47
            else:
                count += 21
        elif letter.lower() == "v":
            if letter == "V":
                count += 48
            else:
                count += 22
        elif letter.lower() == "w":
            if letter == "W":
                count += 49
            else:
                count += 23
        elif letter.lower() == "x":
            if letter == "X":
                count += 50
            else:
                count += 24
        elif letter.lower() == "y":
            if letter == "Y":
                count += 51
            else:
                count += 25
        elif letter.lower() == "z":
            if letter == "Z":
                count += 52
            else:
                count += 26
    print(count)

if __name__ == "__main__":
    part_one()
    part_two()