def import_puzzle():
    with open("Assign_Input_21_06", "rt") as f:
        return[int(entry) for entry in f.readline().split(",")]

def part_one(fishes):
    fish_timers = list(fishes)
    days = 80

    for _ in range(days):
        new_fish = []
        for fish in enumerate(fish_timers):
            fish_timers[fish[0]] -= 1
            if fish_timers[fish[0]] == -1:
                new_fish.append(8)
                fish_timers[fish[0]] = 6
        fish_timers.extend(new_fish)
    return len(fish_timers)

def part_two(fishes):
    fish_timers = list(fishes)
    days = 256

    for _ in range(days):
        pass


if __name__ == "__main__":
    fishes = import_puzzle()
    print(part_one(fishes))