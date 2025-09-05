# starting sets
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i) add 55 and 66 in S1
S1.add(55)
S1.add(66)
print("After adding 55, 66 in S1:", S1)

# (ii) remove 10 and 30 from S1
S1.discard(10)   # discard avoids error if not present
S1.discard(30)
print("After removing 10, 30 from S1:", S1)

# (iii) check if 40 present in S1
if 40 in S1:
    print("40 is present in S1")
else:
    print("40 is not in S1")

# (iv) union of S1 and S2
print("Union:", S1 | S2)

# (v) intersection of S1 and S2
print("Intersection:", S1 & S2)

# (vi) difference S1 - S2
print("S1 - S2:", S1 - S2)