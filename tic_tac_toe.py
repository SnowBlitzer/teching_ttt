import pygame
from pygame.locals import *

DEBUG = False

def log(thing):
    if DEBUG:
        print(thing)

def init_board(ttt_display):
    """
    Building the detalails of the board - lines and set up

    ttt_display : a properly initialized pyGame display variable
    """

    # Creates the surface of the GUI
    background = pygame.Surface(ttt_display.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Draw the board_state lines - vertical than horizontal
    pygame.draw.line(background, (0, 0, 0), (100, 0), (100, 300), 2)
    pygame.draw.line(background, (0, 0, 0), (200, 0), (200, 300), 2)

    pygame.draw.line(background, (0, 0, 0), (0, 100), (300, 100), 2)
    pygame.draw.line(background, (0, 0, 0), (0, 200), (300, 200), 2)

    return background

def display_winning(board, winner):
    """ Displays a message when a winner is found"""

    if winner == None:
        winning_message = "Draw between players!"
    else:
        winning_message = "Player " + winner + " has won!"

    font = pygame.font.Font(None, 24)
    text = font.render(winning_message, 1, (10, 10, 10))

    # Adds the message above to the board
    board.fill((250, 250, 250), (0, 300, 300, 25))
    board.blit(text, (10, 300))

def draw_move(board, boardRow, boardCol):

    # Find center of clicked square - used to draw out from
    center_x = (boardCol * 100) + 50
    center_y = (boardRow * 100) + 50

    # Draw which ever player made the move
    if current_player == "O":
        pygame.draw.circle(board, (0, 0, 0), (center_x, center_y), 36, 2)
    else:
        pygame.draw.line(board, (0, 0, 0), (center_x - 24, center_y - 24), \
                         (center_x + 24, center_y + 24), 2)
        pygame.draw.line(board, (0, 0, 0), (center_x + 24, center_y - 24), \
                         (center_x - 24, center_y + 24), 2)

    board_state[boardRow][boardCol] = current_player

def check_value(mouse_position):
    if mouse_position < 100:
        return 0
    elif mouse_position < 200:
        return 1
    else:
        return 2

def find_click_pos(mouse_x, mouse_y):
    """Determines which square was picked based on the coordinate of the clicked"""

    # Determine the row the user clicked, then the column
    row = check_value(mouse_y)
    col = check_value(mouse_x)

    return (row, col)

def make_move(board):
    """
    Determine where was clicked, if there was a play there already, and if not,
    draws the player's icon
    """

    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    (row, col) = find_click_pos(mouse_x, mouse_y)

    # If the place has already been selected, we won't do anything
    if board_state[row][col] != None:
        return

    draw_move(board, row, col)
    check_win()

    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def show_board(ttt_display, board):
    """
    Redraw the board with updated information

    ttt   : the initialized pyGame display
    board : the game board surface
    """

    #draw_status(board)
    ttt_display.blit(board, (0, 0))
    pygame.display.flip()

def check_win():
    """
    Logic to check when the game has finished
    """

    # check for winning rows
    for row in range(0, 3):
        if board_state[row][0] == board_state[row][1] == board_state[row][2] and \
           board_state[row][0] is not None:
            # this row won
            winner = board_state[row][0]
            pygame.draw.line(board, (250, 0, 0), (0, (row + 1)*100 - 50), \
                            (300, (row + 1)*100 - 50), 2)
            break

    # check for winning columns
    for col in range(0, 3):
        if (board_state[0][col] == board_state[1][col] == board_state[2][col]) and \
           (board_state[0][col] is not None):
            # this column won
            winner = board_state[0][col]
            pygame.draw.line(board, (250, 0, 0), ((col + 1) * 100 - 50, 0), \
                            ((col + 1)* 100 - 50, 300), 2)
            break

    # check for diagonal winners
    if (board_state[0][0] == board_state[1][1] == board_state[2][2]) and \
       (board_state[0][0] is not None):
        # game won diagonally left to right
        winner = board_state[0][0]
        pygame.draw.line(board, (250, 0, 0), (50, 50), (250, 250), 2)

    if (board_state[0][2] == board_state[1][1] == board_state[2][0]) and \
       (board_state[0][2] is not None):
        # game won diagonally right to left
        winner = board_state[0][2]
        pygame.draw.line(board, (250, 0, 0), (250, 50), (50, 250), 2)

def main():
    while 1:
        for event in pygame.event.get():
            if event.type is QUIT:
                return
            elif event.type is MOUSEBUTTONDOWN:
                make_move(board)

            show_board(ttt_display, board)

if __name__ == "__main__":
    board_state = [[None, None, None],
                   [None, None, None],
                   [None, None, None]]

    current_player = "X"

    pygame.init()
    ttt_display = pygame.display.set_mode((300, 325))
    pygame.display.set_caption('Tic-Tac-Toe')

    board = init_board(ttt_display)

    main()
