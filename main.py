from os import system, name
import random as r
import ship as s

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def print_grid(show_ships = False):
    print("   ", end = '')
    for x in range(grid_size[0]):
        print(f"| {chr(ord('A') + x)} ", end = '')
    for y in range(grid_size[1]):
        print("|\n---", end = '')
        for x in range(grid_size[0]):
            print("+---", end = '')
        if y >= 9:
            print(f"|\n{y + 1} ", end = '')
        else:
            print(f"|\n {y + 1} ", end = '')
        for x in grid[y]:
            if x == 0 or show_ships is False:
                print(f"| · ", end = '')
            elif x in ("X", "O"):
                print(f"| {x} ", end = '')
            else:
                print(f"| {x[1]} ", end = '')
    print("|\n---", end = '')
    for x in range(grid_size[0]):
        print("----", end = '')
    print("-")

def check_ship(ship):
    for i in ship.coords:
        if i[0] >= grid_size[0] or i[1] >= grid_size[1]:
            return False
    return True

def add_ship(ship):
    for i in ship.coords:
        grid[i[1]][i[0]] = ship.id, ship.coords.index(i)

def start_screen():
    clear()
    print("-Battleships-")
    input("Press Enter to Start")

def initialise_game():
    global grid_size
    grid_size = [10, 10]
    global grid
    grid = []

    for y in range(grid_size[1]):
        grid_row = []
        for x in range(grid_size[0]):
            grid_row.append(0)
        grid.append(grid_row)
    global ships
    ships = {
        # "C": s.ship("C", 5, "Carrier"),
        # "B": s.ship("B", 4, "Battleship"),
        # "R": s.ship("R", 3, "Cruiser"),
        # "S": s.ship("S", 3, "Submarine"),
        "D": s.ship("D", 2, "Destroyer")
    }
    global ships_sunk
    ships_sunk = {}
    for key in ships.keys():
        ships_sunk[key] = False

    for ship in ships.values():
        ship_check = False
        while ship_check is False:
            ship.place_ship(r.randint(0, grid_size[0] - ship.size), r.randint(0, grid_size[1] - ship.size), r.randint(0, 1))
            ship_check = check_ship(ship)
        add_ship(ship)

def take_turn():
    print_grid(True)
    print(f"Turn {turn}")
    player_input = list(input("Enter Co-ordinates: "))
    player_coords = [ord(player_input[0].upper()) - ord("A"), int(player_input[1]) - 1]
    if grid[player_coords[1]][player_coords[0]] != 0:
        hit_ship, hit_section = grid[player_coords[1]][player_coords[0]]
        ships[hit_ship].hit[hit_section] = True
        grid[player_coords[1]][player_coords[0]] = "X"
        if all(ships[hit_ship].hit):
            ships_sunk[hit_ship] = True
            print("Hit!")
            input(f"You sunk the {ships[hit_ship].name}!")
            if all(ships_sunk):
                return True
        else:
            input("Hit!")
    else:
        grid[player_coords[1]][player_coords[0]] = "O"
        input("Miss!")

start_screen()
initialise_game()
game_over = False
turn = 1
while game_over is not True:
    game_over = take_turn()
    turn += 1
    if turn > 100:
        break
print_grid(True)
print("You Win!")
print(f"Turns Taken: {turn - 1}")



# print_grid(True)

