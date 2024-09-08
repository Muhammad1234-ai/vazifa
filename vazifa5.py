def add_two_numbers(l1, l2):
    num1 = int(''.join(map(str, l1[::-1])))
    num2 = int(''.join(map(str, l2[::-1])))
    total = num1 + num2
    return [int(digit) for digit in str(total)[::-1]]

l1 = [2, 4, 3]
l2 = [5, 6, 4]

output = add_two_numbers(l1, l2)
print(output)
