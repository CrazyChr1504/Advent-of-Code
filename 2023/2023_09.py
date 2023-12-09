file_name = "AoC_Inputs\Advent_2023\Advent_09_23.txt"

with open(file_name, "r") as f:
	data = f.read()
	nums = [list(map(int, lines.split())) for lines in data.splitlines()]

def solve(nums):
	if len(set(nums)) == 1:
		return nums[0]
	diff = []
	for i in range(len(nums)-1):
		diff.append(nums[i+1]-nums[i])
	return nums[-1] + solve(diff)

def Part1():
	print(sum(solve(n) for n in nums))

def Part2():
	print(sum(solve(n[::-1]) for n in nums))

def main():
  Part1()
  Part2()

if __name__ == "__main__":
  main()