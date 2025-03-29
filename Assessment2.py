
# Python Week2 Assessment

# Create an empty list called my_list

my_list = []
print(my_list)

# Append the following elements to my_list: 10, 20, 30, 40.

my_list= []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Insert the value 15 at the second position in the list

my_list = [10, 20, 30, 40]
my_list.insert(1, 15)
print(my_list)

# Extent my_list with another list

my_list = [10, 15, 20, 30, 40]
ext1 = [50, 60, 70]
my_list.extend(ext1)
print(my_list)

# Remove the last elements from my_list

my_list = [10, 15, 20, 30, 40, 50, 60, 70]
my_list.pop()
print(my_list)

# Sort my_list in ascending order

my_list = [10, 15, 20, 30, 40, 50, 60, 70]
my_list.sort()
print(my_list)

# Find and print the index of the value 30 in my_list

my_list = [10, 15, 20, 30, 40, 50, 60, 70]
x = my_list.index(30)
print(x)
