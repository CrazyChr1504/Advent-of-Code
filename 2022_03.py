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
    count = []
    values = {"a": 1, "b": 2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13,
          "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v":22, "w": 23, "x": 24,
          "y":25, "z": 26, "A": 27, "B": 28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36,
          "K":37, "L":38, "M":39, "N":40, "O": 41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U": 47, "V":48,
          "W":49, "X":50, "Y":51, "Z":52}
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
        count.append(values[letter])
    print(sum(count))

def part_two():
    same_item = []
    list_1 = []
    list_2 = []
    list_3 = []
    items = []
    counter = 0
    count = []
    values = {"a": 1, "b": 2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13,
          "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v":22, "w": 23, "x": 24,
          "y":25, "z": 26, "A": 27, "B": 28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36,
          "K":37, "L":38, "M":39, "N":40, "O": 41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U": 47, "V":48,
          "W":49, "X":50, "Y":51, "Z":52}
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
        count.append(values[letter])
    print(sum(count))

if __name__ == "__main__":
    part_one()
    part_two()