numbers=[1,2,3,4,5]

index = 0
doubled_numbers = []
while index < len(numbers):
    doubled_numbers.append(numbers[index] * 2)
    index += 1

print("Original list:", numbers)
print("Doubled list:", doubled_numbers)