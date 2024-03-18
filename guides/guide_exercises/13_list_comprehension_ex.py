# Coding Exercise

# Create a variable called result and use list comprehension to increment each number from the numbers list by 1.

numbers = [1,2,3,4,5,6]
# result = []

# for num in numbers:
#     result.append(num + 1)

result = [num + 1 for num in numbers ]

print(result)



