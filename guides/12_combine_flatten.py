# How to Combine and Flatten Lists in Python with the For / In Loop

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

# raw_db = [legacy_customers, new_customers]

# print(raw_db)

for legacy_customer in legacy_customers:
  new_customers.append(legacy_customer)

print(new_customers)

