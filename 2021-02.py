
#     PART 1
# depth = 0
# horizantal = 0
# movement = []
# with open("Assign_Input_21_02", "r", encoding="utf-8") as f:

#     for line in f.readlines():
#         movement.append(line.strip("\n").split(" "))

#     for direction in movement:
#         if direction[0].lower() == "forward":
#             horizantal += int(direction[1])
#         elif direction[0].lower() == "up":
#             depth -= int(direction[1])
#         elif direction[0].lower() == "down":
#             depth += int(direction[1])

#     course = depth*horizantal
#     print(course)

#     #PART 2
# aim = 0
# depth = 0
# horizantal = 0
# moves = []
# with open("Assign_Input_21_02", "r", encoding="utf-8") as f:
#     for line in f.readlines():
#         moves.append(line.strip("\n").split(" "))

#     for directions in moves:
#         if directions[0].lower() == "forward":
#             horizantal += int(directions[1])
#             depth_change = int(directions[1])*aim
#             depth += depth_change
#             print(depth)
#         elif directions[0].lower() == "down":
#             aim += int(directions[1])
#         elif directions[0].lower() == "up":
#             aim -= int(directions[1])

#     course = depth*horizantal
#     print(course)