depth = 3
rows = 4
cols = 6

array_3d = [[['*' for c in range(cols)] for r in range(rows)] for d in range(depth)]

for i, layer in enumerate(array_3d, start=1):
    print(f"Layer {i}:")
    for row in layer:
        print(" ".join(row))  
    print()  