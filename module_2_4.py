numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in range(len(numbers)):
    #print(numbers[i])
    is_prime = True
    if numbers[i] < 2:
        is_prime = False
    for s in range(2, numbers[i]):
        #print(s)
        if numbers[i] % s == 0:
            is_prime = False
    if is_prime == False:
        not_prime.append(numbers[i])
    else: prime.append(numbers[i])
not_prime.remove(1)
print(prime)
print(not_prime)