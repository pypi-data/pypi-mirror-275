# damage_calculator/calculator.py

import random

def calculate_damage(level, attack, defense, power, type_effectiveness, stab=1.5, random_factor_range=(0.85, 1.0)):
    level_factor = (2 * level) / 5 + 2
    random_factor = random.uniform(*random_factor_range)
    damage = (((level_factor * attack * power / defense) / 50) + 2) * random_factor * stab * type_effectiveness
    return damage

def get_user_input():
    try:
        level = int(input("Enter the level of your Pokémon: "))
        attack = int(input("Enter the attacker's Pokémon attack power: "))
        defense = int(input("Enter the defending Pokémon's defense: "))
        power = int(input("Enter the power of the move to be used.: "))
        type_effectiveness = float(input("Enter the effect multiplier(0.25, 0.5, 1, 2, 4): "))
        stab_input = input("Is there a type-matching bonus?(yes/no): ").strip().lower()
        stab = 1.5 if stab_input == 'yes' else 1.0
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
        return None
    return level, attack, defense, power, type_effectiveness, stab

def main():
    user_input = get_user_input()
    if user_input:
        level, attack, defense, power, type_effectiveness, stab = user_input
        damage = calculate_damage(level, attack, defense, power, type_effectiveness, stab)
        print(f'Damage inflicted: {damage:.2f}')

if __name__ == "__main__":
    main()
