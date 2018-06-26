

numbers = [i for i in range(100)]

for i in range(len(numbers)):
    numbers[i] = numbers[i]**5
    numbers[i] += numbers[i]**2
print(numbers[30])
