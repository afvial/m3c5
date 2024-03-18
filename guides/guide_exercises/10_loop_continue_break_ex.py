# Coding Exercise

#Write a loop that loops over the list of vegetables and prints each one out. When it reaches 'apple' it should print 'apple is not a vegetable' and then break.

vegetables = ["onion", "broccoli", "apple", "spinach"]

for vegetable in vegetables:
    if vegetable == 'apple':
        print(f'{vegetable} is not a vegetable')
        break
    else:
        print(vegetable)

