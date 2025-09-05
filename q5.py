# starting dictionary
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i) add new entry key=8, value=8.8
D[8] = 8.8
print("After adding key=8:", D)

# (ii) remove key=2
if 2 in D:
    D.pop(2)
print("After removing key=2:", D)

# (iii) check if key=6 exists
if 6 in D:
    print("Key 6 is present")
else:
    print("Key 6 is not present")

# (iv) count number of elements
print("Number of elements:", len(D))

# (v) add all values
total = 0
for v in D.values():
    total += v
print("Sum of all values:", total)

# (vi) update value of key=3 to 7.1
if 3 in D:
    D[3] = 7.1
print("After updating key=3:", D)

# (vii) clear dictionary
D.clear()
print("After clearing:", D)