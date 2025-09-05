import random
import string

# (i) 100 random strings of length 6–8 with letters only
print("100 Random Strings:")
for _ in range(100):
    length = random.randint(6, 8)
    s = ''.join(random.choice(string.ascii_letters) for i in range(length))
    print(s)

# (ii) Prime numbers between 600 and 800
print("\nPrime numbers between 600 and 800:")
for num in range(600, 801):
    prime = True
    if num < 2:
        prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
    if prime:
        print(num, end=" ")
print()

# (iii) Numbers between 100 and 1000 divisible by 7 and 9
print("\nNumbers divisible by 7 and 9 (100–1000):")
for num in range(100, 1001):
    if num % 7 == 0 and num % 9 == 0:
        print(num, end=" ")
print()