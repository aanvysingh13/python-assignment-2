positions = [(2,3), (4,5), (6,7), (7,8)]

even_x_positions = []
for pos in positions:
    if pos[0] % 2 == 0:
        even_x_positions.append(pos)

print("Positions with even x-coordinate:", even_x_positions)