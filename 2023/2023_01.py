file_name = "Programmering\AoC_Inputs\Advent_2023\Advent_01_23.txt"

with open(file_name, "r") as file:
  input = file.read()
  input_list = input.split('\n')

  def part_1():
    num = 0
    for input_data in input_list:
      nums = []
      for data in input_data:
        if data.isnumeric():
          nums.append(data)
      num += int(nums[0] + nums[-1])
    print(num)

  def part_2():
    final_num = 0
    spelling = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for data in input_list:
      nums = []
      for i, num in enumerate(data):
        for val, word in enumerate(spelling): 
          if word in data[i:i+len(word)]:
            nums.append(str(val))
          if num.isnumeric():
            nums.append(num)     
      final_num += int(nums[0] + nums[-1])
    print(final_num)

def main():
  part_1()
  part_2()

if __name__ == "__main__":
  main()