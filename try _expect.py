
try:
    num_1 = int(input('Enter the number: '))
except ValueError as e:
    num_1 = 0
    print(e)
num_2 = int(input('Enter the number: '))

sum = num_1 + num_2

print(sum)
