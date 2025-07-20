"""Non primitive types: list, tuple, set, dict"""

# ------------------------------------------------------------

# my_list = []
# while True:
#     choice = input("qoshish: ")
#     if choice == "yes":
#         word = input("Enter anything word: ")
#         my_list.append(word)
#     else:
#         break
# print(my_list)
# my_list.remove("banan")
# print(my_list)
# print(my_list[0])

# ------------------------------------------------------------

# number = tuple((1,2,3,4,5))
# print(len(number))
# print(number[2])

# ------------------------------------------------------------

# unique_nums = (1,2,2,3,4,4,5)
# result = set(unique_nums)
# result.add(6)
# print(unique_nums)
# print(result)
# result.discard(7)
# print(f"hatolik chiqmadi lekin ishlavoti maqsad 3 ochirish bogan:{result}")
# print("uzunligi",result.__len__())

# ------------------------------------------------------------

person  = {"name": "Anvar", 'age': 25, 'city': 'Toshkent', 'email': 'anvar@gmail.com'}
print(person)
person.update({"age": 26})
print(person)
person["ball"] = 5
print(person)
print(person.get("ball"))

# ------------------------------------------------------------