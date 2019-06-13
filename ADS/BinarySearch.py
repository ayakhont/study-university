import sys

# first input number is n - array length, rest others are sorted array
array = [int(x) for x in input().split()]
n = array[0]

# first input number is k - number of searched numbers, rest others are searched numbers
search_array = [int(x) for x in input().split()]
count = search_array[0]

result = list()
for i in range(1, count + 1):
    l = 1
    r = n
    k = search_array[i]
    is_searched = False
    while l <= r:
        m = int((l + r)/2)
        if array[m] == k:
            result.append(m)
            is_searched = True
            break
        elif array[m] > k:
            r = m - 1
        else:
            l = m + 1

    if not is_searched:
        result.append(-1)

sys.stdout.write(" ".join(str(x) for x in result))

