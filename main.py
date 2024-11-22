# imported methods to clear the terminal
from os import system, name
import random as r
import ship as s

# function to clear the terminal
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

# prints the grid in the terminal
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

# checks if the ship position is valid - i.e. if it is within the grid and not overlapping any other ship
def check_ship(ship):
    for i in ship.coords:
        if i[0] >= grid_size[0] or i[1] >= grid_size[1]:
            return False
        if grid[i[1]][i[0]] != 0:
            return False
    return True

# adds the ship to the grid
def add_ship(ship):
    for i in ship.coords:
        grid[i[1]][i[0]] = ship.id, ship.coords.index(i)

# loads the start screen
def start_screen():
    clear()
    print("-Battleships-")
    input("Press Enter to Start")

# initialises the game
def initialise_game():
    # sets the grid size
    global grid_size
    grid_size = [10, 10]
    # list to store information about each grid co-ordinate
    global grid
    grid = []
    for y in range(grid_size[1]):
        grid_row = []
        for x in range(grid_size[0]):
            grid_row.append(0)
        grid.append(grid_row)
    # dictionary of each ship in play
    global ships
    ships = {
        # "C": s.ship("C", 5, "Carrier"),
        # "B": s.ship("B", 4, "Battleship"),
        # "R": s.ship("R", 3, "Cruiser"),
        "S": s.ship("S", 3, "Submarine"),
        "D": s.ship("D", 2, "Destroyer")
    }
    # dictionary of all the ships that have sunk
    global ships_sunk
    ships_sunk = {}
    for key in ships.keys():
        ships_sunk[key] = False

    # initialises each ship
    for ship in ships.values():
        ship_check = False
        while ship_check is False:
            ship.place_ship(r.randint(0, grid_size[0] - 1), r.randint(0, grid_size[1] - 1), r.randint(0, 1))
            ship_check = check_ship(ship)
        add_ship(ship)

# runs when a player needs to take a turn
def take_turn():
    print_grid(True)
    print(f"Turn {turn}")
    player_input = input("Enter Co-ordinates: ")
    player_coords = [ord(player_input[0].upper()) - ord("A"), int(player_input[1:]) - 1]
    # checks if a player hits or skinks a ship
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
# game ends when all ships have sunk
while game_over is not True:
    game_over = take_turn()
    turn += 1
    if turn > 100:
        break
print_grid(True)
print("You Win!")
print(f"Turns Taken: {turn - 1}")



# print_grid(True)

