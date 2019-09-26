import pygame
import time
from pygame.locals import *


class Board:
  def __init__(self):
    self.current_player = "X"
    self.board_state = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]

    pygame.init()
    self.ttt_display = pygame.display.set_mode((450, 475))
    pygame.display.set_caption('Tic-Tac-Toe')

    self.board_layout = self.init_board()

  def set_current_player(self, current):
    self.current_player = current

  def init_board(self):
    """
    Building the details of the board - lines and set up
    """

    # Creates the surface of the GUI
    background = pygame.Surface(self.ttt_display.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Draw the board_state lines - vertical than horizontal
    pygame.draw.line(background, (0, 0, 0), (150, 0), (150, 450), 3)
    pygame.draw.line(background, (0, 0, 0), (300, 0), (300, 450), 3)

    pygame.draw.line(background, (0, 0, 0), (0, 150), (450, 150), 3)
    pygame.draw.line(background, (0, 0, 0), (0, 300), (450, 300), 3)

    return background

  def draw_move(self, boardRow, boardCol):
    # Find center of clicked square - used to draw out from
    center_x = (boardCol * 150) + 75
    center_y = (boardRow * 150) + 75

    # Draw which ever player made the move
    if self.current_player == "O":
      pygame.draw.circle(game.board_layout, (0, 0, 0), (center_x, center_y), 50, 2)
    else:
      pygame.draw.line(game.board_layout, (0, 0, 0), (center_x - 45, center_y - 45), \
                      (center_x + 45, center_y + 45), 2)
      pygame.draw.line(game.board_layout, (0, 0, 0), (center_x + 45, center_y - 45), \
                      (center_x - 45, center_y + 45), 2)

    self.board_state[boardRow][boardCol] = self.current_player

  def draw_status_message(self, winner):
    if winner is not None:
        message = winner + " won!"
    else:
      if game.current_player == "X":
        game.set_current_player("O")
      else:
        game.set_current_player("X")

      message = game.current_player + "'s turn"

    font = pygame.font.Font(None, 24)
    text = font.render(message, 1, (10, 10, 10))

    self.board_layout.fill((250, 250, 250), (0, 450, 450, 25))
    self.board_layout.blit(text, (10, 450))

  def show_board(self):
    """
    Redraw the board with updated information
    """
    self.ttt_display.blit(self.board_layout, (0, 0))
    pygame.display.flip()

def check_value(mouse_position):
  if mouse_position < 150:
    return 0
  elif mouse_position < 300:
    return 1
  else:
    return 2

def find_click_pos(mouse_x, mouse_y):
  """Determines which square was picked based on the coordinate of the clicked"""

  # Determine the row the user clicked, then the column
  row = check_value(mouse_y)
  col = check_value(mouse_x)

  return (row, col)

def make_move(game):
  """
  Determine where was clicked, if there was a play there already, and if not,
  draws the player's icon
  """

  (mouse_x, mouse_y) = pygame.mouse.get_pos()
  (row, col) = find_click_pos(mouse_x, mouse_y)

  # If the place has already been selected, we won't do anything
  if game.board_state[row][col] != None:
    return

  game.draw_move(row, col)
  possible_winner = check_win(game)
  game.draw_status_message(possible_winner)

def check_win(game):
  # Rows
  winner = None
  for row in range(0, 3):
    if game.board_state[row][0] == game.board_state[row][1] == game.board_state[row][2] and \
       game.board_state[row][0] is not None:

        winner = game.board_state[row][0]

        pygame.draw.line(game.board_layout, (255, 0, 0), (0, (row + 1) * 150 - 75), \
                         (450, (row + 1) * 150 - 75), 3)

        break

  # Columns
  for col in range(0, 3):
    if game.board_state[0][col] == game.board_state[1][col] == game.board_state[2][col] and \
       game.board_state[0][col] is not None:

        winner = game.board_state[0][col]
        pygame.draw.line(game.board_layout, (255, 0, 0), ((col + 1) * 150 - 75, 0), \
                         ((col + 1)* 150 - 75, 450), 3)

        break

  # Diagonals
  if game.board_state[0][0] == game.board_state[1][1] == game.board_state[2][2] and \
     game.board_state[0][0] is not None:
        winner = game.board_state[0][0]
        pygame.draw.line(game.board_layout, (255, 0, 0), (50, 50), (400, 400), 3)

  if game.board_state[0][2] == game.board_state[1][1] == game.board_state[2][0] and \
     game.board_state[0][2] is not None:
        winner = game.board_state[0][2]
        pygame.draw.line(game.board_layout, (255, 0, 0), (400, 50), (50, 400), 3)

  return winner

def main(game):
  while 1:
    for event in pygame.event.get():
      if event.type is QUIT:
        return
      elif event.type is MOUSEBUTTONDOWN:
        make_move(game)

      game.show_board()

if __name__ == "__main__":
  game = Board()

  main(game)
