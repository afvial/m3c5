# Guide to Default Arguments in Python Functions

def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
# def some_function(collection = []):
#   collection.append(1)
#   print(id(collection))
#   return collection


# print(some_function())
# print(some_function())
