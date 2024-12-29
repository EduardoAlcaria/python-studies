val = [10, 5, 2]
def times(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)
times(val)