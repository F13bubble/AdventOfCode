count = 0
count_part2 = 0
current_pos = 50
current_pos_2 = 50
dial_range = 100
    

with open("2025/Day 1/day1_input.txt", "r") as file:
    lines = file.readlines()


    for line in lines:
        direction, steps = line[0], int(line[1:])

        current_pos_2 += steps if direction == "R" else -steps
        current_pos_2 %= 100
        count += current_pos_2 == 0

        for _ in range(steps):
            current_pos += 1 if direction == "R" else -1
            current_pos %= 100
            count_part2 += current_pos == 0

        
print("Part 1\nCount: ", count)
print("Part 2\nCount: ", count_part2)
