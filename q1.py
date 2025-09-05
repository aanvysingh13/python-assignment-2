# starting list
L = [11, 12, 13, 14]

# (i) add 50 and 60
L.append(50)
L.append(60)
print("After adding 50, 60:", L)

# (ii) remove 11 and 13
if 11 in L:
    L.remove(11)
if 13 in L:
    L.remove(13)
print("After removing 11, 13:", L)

# (iii) sort ascending
L.sort()
print("Ascending:", L)

# (iv) sort descending
L.sort(reverse=True)
print("Descending:", L)

# (v) search 13 in L
if 13 in L:
    print("13 is present")
else:
    print("13 not found")

# (vi) count elements
print("Total elements:", len(L))

# (vii) sum of elements
print("Sum of elements:", sum(L))

# (viii) sum of odd numbers
odd_sum = 0
for i in L:
    if i % 2 != 0:
        odd_sum += i
print("Sum of odd numbers:", odd_sum)

# (ix) sum of even numbers
even_sum = 0
for i in L:
    if i % 2 == 0:
        even_sum += i
print("Sum of even numbers:", even_sum)

# (x) sum of prime numbers
def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            return False
    return True

prime_sum = 0
for i in L:
    if is_prime(i):
        prime_sum += i
print("Sum of prime numbers:", prime_sum)

# (xi) clear the list
L.clear()
print("After clear:", L)

# (xii) delete L
del L