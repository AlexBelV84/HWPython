numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_Prime = True
    if numbers[i] == 2:
        Primes.append(numbers[i])
        continue
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_Prime = False
            break
    if is_Prime:
        Primes.append(numbers[i])
    else:
        Not_Primes.append(numbers[i])
print("Primes: ", Primes)
print("Not_Primes:", Not_Primes)
