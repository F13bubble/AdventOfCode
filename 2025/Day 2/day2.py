summary = 0

with open("2025/Day 2/day2_input.txt", "r") as file:
    inp = file.read()
    ranges = inp.split(",")
    for ran in ranges:
        start, end = ran.split("-")
        for id in range(int(start), int(end)):
            id = str(id).rstrip()
            summary += int(id) if id[:int(len(id)/2)] == id[int(len(id)/2):] else 0
            
print(summary)