res1 = 0
res2 = 0

with open("2025/Day 2/day2_input.txt", "r") as file:
    inp = file.read()
    ranges = inp.split(",")
    for ran in ranges:
        start, end = ran.split("-")
        for id in range(int(start), int(end)):
            s = str(id).rstrip()
            mid = len(s) // 2
            if len(s) % 2 == 0 and s[:mid] == s[mid:]:
                res1 += id
            if any(s == s[:l] * (len(s) // l) for l in range(1, mid + 1)):
                res2 += id
            
print("Part 1: ", res1)
print("Part 2: ", res2)