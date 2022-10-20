import random

def rollVirtualDie(sides_of_die):
	result = random.randint(1,sides_of_die)
	return result

def roll_6_and_8():
	roll_6_sided_die = rollVirtualDie(6)
	roll_8_sided_die = rollVirtualDie(8)
	health = roll_6_sided_die * roll_8_sided_die
	return health

print("Character stats generator")

have_a_character = "yes"

while have_a_character == "yes":
	character = input("Name your warrior: ")
	health = str(roll_6_and_8())
	print("Their health is ", health, "hp")
	have_a_Character = input("Want to create another character? ")