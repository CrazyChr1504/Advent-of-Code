
file_name = "AoC_Inputs\Advent_2023\Advent_02_23.txt"
BOUNDS = {  'red': 12, 'green': 13, 'blue': 14,  }
with open(file_name, 'r') as f:
  data = f.read().split('\n')

  def part_1():
    sum = 0
    for game, cubes in enumerate(data):
      cubes = cubes.split(':')[1].split(';')
      valid = True
      for colors in cubes:
        colors = colors.strip().split(',')
        for color in colors:
          color = color.strip().split(' ')
          if ((color[1] == 'red' and int(color[0]) > BOUNDS['red']) or
            (color[1] == 'green' and int(color[0]) > BOUNDS['green']) or
            (color[1] == 'blue' and int(color[0]) > BOUNDS['blue'])):
            valid = False
      if valid:
          sum += (game+1)
    print(sum)

  def part2():
    sum = 0
    for inputs in data:
      inputs = inputs.split(':')[1].split(';')
      rgb = [0, 0, 0]
      for cubes in inputs:
        cubes = cubes.strip().split(',')
        for colors in cubes:
          colors = colors.strip().split(' ')
          if colors[1] == 'green' and int(colors[0]) > rgb[1]:
            rgb[1] = int(colors[0])
          if colors[1] == 'red' and int(colors[0]) > rgb[0]:
            rgb[0] = int(colors[0])
          if colors[1] == 'blue' and int(colors[0]) > rgb[2]:
            rgb[2] = int(colors[0])
      sum += (rgb[0]*rgb[1]*rgb[2])
    print(sum)

def main():
  part_1()
  part2()

if __name__ == "__main__":
  main()