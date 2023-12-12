file_name = "AoC_Inputs\Advent_2023\Advent_12_23.txt"

with open(file_name, "r") as f:
  data = f.readlines()

cache = {}

def ways(row, nums):
	if (row,tuple(nums)) in cache:
		return cache[(row,tuple(nums))]
	
	if len(nums) == 0:
		return 1 if "#" not in row else 0
	
	size = nums[0]
	total = 0

	for i in range(len(row)):
		if (i + size <= len(row) and all( char != "." for char in row[i:i+size] ) and (i == 0 or row[i-1] != "#") and (i == len(row)-size or row[i+size] != "#")):
			total += ways(row[i+size+1:], nums[1:])
		if row[i] == "#":
			break
	
	cache[(row,tuple(nums))] = total
	return total


def Part1():
	total = 0
	for line in data:
		row, nums = line.split()
		row = "?".join([row])
		nums = [int(n) for n in nums.split(",")]
		total += ways(row, nums)
	print(total)

def Part2():
	total = 0
	for line in data:
		row, nums = line.split()
		row = "?".join([row]*5)
		nums = [int(n) for n in nums.split(",")]*5
		total += ways(row, nums)
	print(total)

def main():
	Part1()
	Part2()

if __name__ == "__main__":
	main()