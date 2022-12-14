with open("AoC_Inputs\Advent_13_22.txt") as f:
    data = f.read().strip().split("\n\n")
row_split = [row.split("\n") for row in data]
pairs = [(eval(a),eval(b)) for a,b in row_split]
big_list = [eval(x) for x in sum(row_split, [])] + [[[2]]] + [[[6]]] 

def comparison(left, right):
    n_left, n_right = len(left), len(right)
    n = max(n_left, n_right)

    for idx in range(n):
        if idx >= n_left: return True
        if idx >= n_right: return False

        left_v, right_v = left[idx], right[idx]
        left_typ, right_typ = type(left_v), type(right_v)

        if (left_typ is int) & (right_typ is int):
            if left_v < right_v: return True
            elif left_v > right_v: return False
        else: 
            if (left_typ is int): left_v = [left_v]
            if (right_typ is int): right_v = [right_v]
            res = comparison(left_v, right_v)
            
            if res is not None: return res
        
def bubble_sort(big_list):
    n = len(big_list) 
    for i in range(n-1):
        for j in range(0, n-i-1): 
            if comparison(big_list[j + 1], big_list[j]): 
                big_list[j], big_list[j + 1] = big_list[j + 1], big_list[j]

bubble_sort(big_list)
for idx, elem in enumerate(big_list):
    if elem == [[2]]: x = idx+1
    if elem == [[6]]: y = idx+1

print(sum([idx+1 for idx, (left,right) in enumerate(pairs) if comparison(left,right)]))
print(x*y)