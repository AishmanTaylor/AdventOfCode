def find_floor(filename):
    with open(filename, 'r') as file:
        instructions = file.read().strip()  
    floor = 0
    basement_position = None    
    for position, char in enumerate(instructions, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1        
        if floor == -1 and basement_position is None:
            basement_position = position

    return floor, basement_position

filename = 'input.txt'
final_floor, basement_position = find_floor(filename)

print(f"Santa ends up on floor {final_floor}")
if basement_position:
    print(f"Santa first enters the basement at position {basement_position}")
else:
    print("Santa never enters the basement.")