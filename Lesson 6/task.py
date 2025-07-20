"""Loop operators: for , while"""

numbers = int(input("Enter number: "))

for number in range(1,numbers+1):
   if number % 2 == 0:
       print(number,end=" ")

print()
index = 1

while numbers >= index:
    print(numbers,end=" ")
    numbers -= 1