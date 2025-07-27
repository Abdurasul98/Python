"""list:append, insert, remove, pop, sort, reverse"""
# ------------------------------------------------------------

my_list = []
print(my_list)

# ------------------------------------------------------------

for _ in range(1,5):
    number = input("Number: ")
    my_list.append(int(number))
print(my_list)

# ------------------------------------------------------------

my_list.insert(1,100)
print(my_list)

# ------------------------------------------------------------

my_list.remove(4)
print(my_list)

# ------------------------------------------------------------

my_list.pop(-1)
print(my_list)

# ------------------------------------------------------------

my_list.sort()
print(my_list)

# ------------------------------------------------------------

my_list.reverse()
print(my_list)