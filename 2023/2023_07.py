from functools import cmp_to_key

file_name = "AoC_Inputs\Advent_2023\Advent_07_23.txt"

with open(file_name, "r") as f:
  data = [line.strip() for line in f.readlines()]

cards = list('AKQJT98765432')[::-1]

def second_categorize_hand(hand):
  max_value = None
  for c in cards:
    replaced_hand = hand.replace('J',c)
    replaced_value = categorize_hand(replaced_hand)
    if max_value is None or replaced_value > max_value:
      max_value = replaced_value
  return max_value

def categorize_hand(hand):
  if len(set(hand)) == 1:
    return 7
  elif len(set(hand)) == 2:
    a,b = set(hand)
    if hand.count(a) == 4 or hand.count(b) == 4:
      return 6
    elif hand.count(a) == 3 or hand.count(b) == 3:
      return 5
  elif len(set(hand)) == 3:
    a,b,c = set(hand)
    a,b,c = [hand.count(v) for v in [a,b,c]]
    if a == 3 or b == 3 or c == 3:
      return 4
    if set([a,b,c]) == {2,2,1}:
      return 3
  elif len(set(hand)) == 4:
    return 2
  return 1

def tie_breaker(a,b):
  values = {
    "A": 15,
    "K": 14,
    "Q": 13,
    "J": 12,
    "T": 11
  }

  for i in range(len(a)):
    aval = a[i]
    bval = b[i]
    if not aval.isdigit():
      aval = values[aval]
    else:
      aval = int(aval)
    if not bval.isdigit():
      bval = values[bval]
    else:
      bval = int(bval)
    if aval < bval:
      return -1
    elif aval > bval:
      return 1
  return 0

def compare_hands(a,b):
    a,_ = a
    b,_ = b
    cha = categorize_hand(a)
    chb = categorize_hand(b)

    if cha > chb:
      return 1
    elif cha < chb:
      return -1

    for ca, cb in zip(a,b):
      if cards.index(ca) > cards.index(cb):
        return 1
      elif cards.index(ca) < cards.index(cb):
        return -1
    return 0

hands = [l.split() for l in data if len(l) > 0]
def Part1():
  hands.sort(key=cmp_to_key(compare_hands))

  sum_wins = 0
  for i, (h, bid) in enumerate(hands):
    sum_wins += int(bid)*(i+1)
  print(sum_wins)

def second_compare_hands(a,b):
  a,_ = a
  b,_ = b
  cha = second_categorize_hand(a)
  chb = second_categorize_hand(b)

  if cha > chb:
    return 1
  elif cha < chb:
    return -1

  for ca, cb in zip(a,b):
    if cards.index(ca) > cards.index(cb):
      return 1
    elif cards.index(ca) < cards.index(cb):
      return -1

  return 0
cards = list('AKQT98765432J')[::-1]
def Part2():
  hands.sort(key=cmp_to_key(second_compare_hands))

  sum_wins = 0

  for i, (h, bid) in enumerate(hands):
    sum_wins += int(bid)*(i+1)

  print(sum_wins)

def main():
  Part1()
  Part2()
  
if __name__ == "__main__":
  main()