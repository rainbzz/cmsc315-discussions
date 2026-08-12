"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy

# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Character:
    max_level = 100
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def status(self):
        return f"{self.name}: {self.health} HP (max level: {self.max_level})"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class Mage(Character):
    max_level = 60
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self):
        return f"{self.name} casts a spell, 10 mana ({self.mana} remaining)"

    def status(self):
        parent_status = super().status()
        return f"{parent_status}, {self.mana} MP (Mage)"

    # my new method, self-contained behavior to an existing class
    # and gives the mage a way to recover mana
    def rest(self, amount=20):
        self.mana += amount
        return f"{self.name} rests and recovers {amount} mana ({self.mana} toal)"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    mage1 = Mage("Bob", 80, 50)
    mage2 = Mage("Steve", 75, 45)
    print (f"Mage.max_level (via class) = {Mage.max_level}")
    print (f"mage1.max_level (via object) = {mage1.max_level}")

    mage1.guild = "Bob's Burgers"
    print(f"\nmage1.__dict__ = {mage1.__dict__} <- has 'guild'")
    print(f"mage2.__dict__ = {mage2.__dict__} <- doesn't")
    print(f"\n'max_level' isn't in either __dict__ above; it's shared")
    print(f"from the class namespace: Mage.__dict__['max_level'] = "
          f"{Mage.__dict__['max_level']}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = Mage("Bob", 80, 50)
    original.inventory = ["Burger", "Fire Scroll"]  #nested mutable data

    shallow = copy(original) #new object, inventory list is shared
    deep = deepcopy(original) #another new object, fully separate inventory list
    original.inventory.append("Mana Crystal") ##mutates the shared list
    original.name = "Bob the Burger Maker" ##reassings a string (not shared)

    print(f"original: name={original.name}, inventory={original.inventory}")
    print(f"shallow: name={shallow.name}, inventory={shallow.inventory}")
    print(f"deep: name={deep.name}, inventory={deep.inventory}")

#########################################################
# shallow.inventory shows "Mana Crystal" (shared list); #
# deep.inventory doesn't (separate/independent list).   #
# shallow.name nor deep.name did not change, as they're #
# immutable strings.                                    #
#########################################################

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    npc = Character("Villager Reinhardt", 30)
    print("\nParent object:")
    print(npc.status())

    hero = Mage("Bob", 80, 50)
    print("\nChild object:")
    print(hero.status())
    print(hero.cast_spell())
    print(hero.rest()) # the rest in action to recover mana

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()