cur_dir = []
dirs = {}
with open("Advent_Inputs\Advent_07_22.txt","rt") as f:
  for l in f:
    e = l.strip().split()
    if l.startswith("$ cd"):
      if e[2] == "..":
        cur_dir.pop()
      else:
        cur_dir.append(e[2])
      p = '/'.join(cur_dir[:-1])
      d = '/'.join(cur_dir)
      if d not in dirs:
        dirs[d] = [0,p]
    elif e[0] not in ("$","dir"):
      s = int(e[0])
      d = '/'.join(cur_dir)
      while d:
        dirs[d][0] += s
        d = dirs[d][1]
  size = 0
d = []
for s,_ in dirs.values():
  d.append(s)
  if s <= 100_000:
    size += s
need = 30_000_000 - (70_000_000 - dirs["/"][0])
for s in sorted(d):
  if s >= need:
    print(size)
    print(s)
    break