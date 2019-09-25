import pygame
from pygame.locals import *

class Board:
  def __init__(self):
    """Setting up the basis of the game!"""
    self.current_player = "X"
    self.board_state = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]

    pygame.init() # Starts up pygame
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

  def show_board(self):
    """
    Redraw the board with updated information
    """
    self.ttt_display.blit(self.board_layout, (0, 0))
    pygame.display.flip()

  def show_winner_message(self, winner):
    pass

def check_value(mouse_position):
  """Checks where the user has clicked"""
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
  pass

def check_win(game):
  """Checking if the last move won the game or not"""
  pass

def main(game):
  pass

if __name__ == "__main__":
  game = Board()

  main(game)
