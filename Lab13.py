import random
# 1
classes = ["CS113", "CS121", "CS122", "CS232", "CS241"]
print(classes[0])
print(classes[1])
print(classes[2])
print(classes[3])
print(classes[4])

# 2
movies = ["LOST", "The Soprano", "Breaking Bad", "Deal or No Deal Island"]
print(f"I picked {random.choice(movies)} for you")

# 3
my_list = []

quest1 = input("What do you need to do: ")
quest2 = input("What do you need to do: ")
quest3 = input("What do you need to do: ")
quest4 = input("What do you need to do: ")
quest5 = input("What do you need to do: ")

my_list.append(quest1)
my_list.append(quest2)
my_list.append(quest3)
my_list.append(quest4)
my_list.append(quest5)

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

# 4
classes = ["CS113", "CS121", "MAT131", "ENG101"]
quest_drop = input("What class would you like to drop? ")
classes.remove(quest_drop)
quest_add = input("What class would you like to add? ")
classes.append(quest_add)
print("Final List: ")
print(classes[0])
print(classes[1])
print(classes[2])
print(classes[3])

# 5
solar_system = []
planet1 = input("Enter Planet 1: ")
solar_system.append(planet1)
planet2 = input("Enter Planet 2: ")
solar_system.append(planet2)
planet3 = input("Enter Planet 3: ")
solar_system.append(planet3)

solar_system.sort()
print("Sorted: ")
print(solar_system[0])
print(solar_system[1])
print(solar_system[2])

solar_system.reverse()
print("Reverse Sorted: ")
print(solar_system[0])
print(solar_system[1])
print(solar_system[2])