lst = [1, 2, 3, 1, 2, 1, 4, 5, 1, 2, 3, 3]

counts = {}

for number in lst:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

print(counts)
