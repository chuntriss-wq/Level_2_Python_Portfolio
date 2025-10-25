# 1. THE DRY FUNCTION (The one-time definition)
def calculate_damage(health, armor, attack):
    damage = attack - (armor / 2)
    return health - damage # <--- This line MUST be indented!

# 2. MAIN SCRIPT LOGIC (These lines MUST start at the far left, NO INDENTATION)
player_health = 100
enemy_armor = 10
player_attack = 25

# DRY Logic: Calling the function every time
player_health = calculate_damage(player_health, enemy_armor, player_attack)
print(f"After Attack 1 (DRY): {player_health}")

player_health = calculate_damage(player_health, enemy_armor, player_attack)
print(f"After Attack 2 (DRY): {player_health}")

player_health = calculate_damage(player_health, enemy_armor, player_attack)
print(f"After Attack 3 (DRY): {player_health}")
   

