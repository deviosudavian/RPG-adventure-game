import random

# Player stats
player = {
    "hp": 100,
    "attack": 15,
    "potions": 3
}

enemies = [
    {"name": "Goblin", "hp": 30, "attack": 8},
    {"name": "Skeleton", "hp": 40, "attack": 10},
    {"name": "Orc", "hp": 50, "attack": 12}
]

def fight(enemy):
    print(f"\n A wild {enemy['name']} appears!")

    while enemy["hp"] > 0 and player["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | {enemy['name']} HP: {enemy['hp']}")
        action = input("Choose action (attack/heal/run): ").lower()

        if action == "attack":
            damage = random.randint(5, player["attack"])
            enemy["hp"] -= damage
            print(f"You deal {damage} damage!")

        elif action == "heal":
            if player["potions"] > 0:
                heal = random.randint(15, 25)
                player["hp"] += heal
                player["potions"] -= 1
                print(f"You healed {heal} HP! Potions left: {player['potions']}")
            else:
                print("No potions left!")

        elif action == "run":
            if random.random() < 0.5:
                print("You escaped!")
                return
            else:
                print("Failed to escape!")

        else:
            print("Invalid action!")
            continue

     
        if enemy["hp"] > 0:
            damage = random.randint(5, enemy["attack"])
            player["hp"] -= damage
            print(f"{enemy['name']} hits you for {damage} damage!")

    if player["hp"] <= 0:
        print("\n You were defeated... Game Over!")
        exit()
    else:
        print(f"\n You defeated the {enemy['name']}!")

def adventure():
    while True:
        print("\n Where do you want to go?")
        print("1. Forest ")
        print("2. Cave ")
        print("3. Village ")
        print("4. Quit")

        choice = input("> ")

        if choice == "1":
            if random.random() < 0.7:
                enemy = random.choice(enemies).copy()
                fight(enemy)
            else:
                print("You found a potion!")
                player["potions"] += 1

        elif choice == "2":
            if random.random() < 0.9:
                enemy = random.choice(enemies).copy()
                enemy["hp"] += 10  
                fight(enemy)
            else:
                print("You found treasure! +10 HP")
                player["hp"] += 10

        elif choice == "3":
            print("You rest at the village. HP restored!")
            player["hp"] = 100

        elif choice == "4":
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice!")

print("Welcome to Mini RPG!")
adventure()