numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, 16):
    for j in range(2, 16):
        if i % j == 0 and i != j:
            primes.append(i)
            break
        elif i / j == 1:
            not_primes.append(i)
        else:
            continue

print('Primes:', primes)
print('Not Primes:', not_primes)


