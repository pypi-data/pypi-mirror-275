# damage_calculator/calculator.py

import random

def calculate_damage(level, attack, defense, power, type_effectiveness, stab=1.5, random_factor_range=(0.85, 1.0)):
    level_factor = (2 * level) / 5 + 2
    random_factor = random.uniform(*random_factor_range)
    damage = (((level_factor * attack * power / defense) / 50) + 2) * random_factor * stab * type_effectiveness
    return damage

def get_user_input():
    try:
        level = int(input("ポケモンのレベルを入力してください: "))
        attack = int(input("攻撃側のポケモンの攻撃力を入力してください: "))
        defense = int(input("防御側のポケモンの防御力を入力してください: "))
        power = int(input("使用する技の威力を入力してください: "))
        type_effectiveness = float(input("技のタイプの効果を入力してください (0.25, 0.5, 1, 2, 4): "))
        stab_input = input("タイプ一致ボーナスがありますか？ (yes/no): ").strip().lower()
        stab = 1.5 if stab_input == 'yes' else 1.0
    except ValueError:
        print("無効な入力です。数値を入力してください。")
        return None
    return level, attack, defense, power, type_effectiveness, stab

def main():
    user_input = get_user_input()
    if user_input:
        level, attack, defense, power, type_effectiveness, stab = user_input
        damage = calculate_damage(level, attack, defense, power, type_effectiveness, stab)
        print(f'与えたダメージ: {damage:.2f}')

if __name__ == "__main__":
    main()
