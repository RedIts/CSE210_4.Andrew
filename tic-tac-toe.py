"""
Tic-Tac-Toe: A simple game to overthink
Author: Dean Redito
"""

def main():
    player = 'x'
    values = [' ' for x in range(9)]
    player_pos = {'x': [], 'o': []}

    while True:
        print_board(values)

        #Try Exception Block for wrong input on move variable.
        try:
            print(f"Player {player}'s turn. Choose a spot: ")
            move = int(input())
        except ValueError:
            print("No such moves. Please Try Again.")
            continue

        #Input range check.
        if move <1 or move >9:
            print("Values not on Board. Please Try Again.")
            continue

        #Check spot if not occupied by another player.
        if values[move - 1] != " ":
            print()
            print("SPOT TAKEN! Please Try Again")
            continue

        #Update board info
        values[move - 1] = player

        player_pos[player].append(move)

        #Check for game ending conditions. Win condition, draw condition.
        if check_win_condition(player_pos, player):
            print_board(values)
            print(f"Player '{player}' wins.")
            return player

        if check_draw_condition(player_pos):
            print_board(values)
            print("Game tied. No more moves available. Good Game.")
            return

        #Player switch
        player = switch_player(player)


def print_board(values):
    """
    Function for displaying board.
    """
    print()
    print(" ———————————")
    print(f"| {values[0]} | {values[1]} | {values[2]} |")
    print(f" —— + — + —— ")
    print(f"| {values[3]} | {values[4]} | {values[5]} |")
    print(f" —— + — + —— ")
    print(f"| {values[6]} | {values[7]} | {values[8]} |")
    print(" ———————————")
    print()

def check_win_condition(player_pos, player):
    """
    Check for win conditions.
    """
    #Possible win combinations
    combinations = [[1,2,3], [4,5,6], [7,8,9,], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    for x in combinations:
        if all(y in player_pos[player] for y in x):
            return True

    return False

def check_draw_condition(player_pos):
    """
    Check Draw Condition. If total moves of 'x' and 'o' reached 9, return True.
    """
    if len(player_pos['x']) + len(player_pos['o']) == 9:
        return True
    return False

def switch_player(current_player):
    """
    Switch player.
    """
    if current_player == 'o':
        return 'x'
    elif current_player == 'x':
        return 'o'

if __name__ == "__main__":
    main()