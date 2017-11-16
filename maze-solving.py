from turtle import Turtle
from time import sleep

grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

arrow = Turtle()

def search(x, y):

  if grid[x][y] == 2:
    print ('found at %d,%d' % (x, y))
    #arrow.done()
    return True
  elif grid[x][y] == 1:
    print ('wall at %d,%d' % (x, y))
    return False
  elif grid[x][y] == 3:
    print ('visited at %d,%d' % (x, y))
    return False

  sleep(0.5)
  arrow.setx(x*8)
  arrow.sety(y*8)
  print ('visiting %d,%d' % (x, y))

  grid[x][y] = 3

  if x < len(grid)-1 and search(x+1, y) \
    or y > 0 and search(x, y-1) \
    or x > 0 and search(x-1, y) \
    or y < len(grid)-1 and search(x, y+1):
      return True

  return False

def setup(x, y):
   for width, obj in enumerate(grid[x]):
     arrow.penup()
     arrow.setx(width*8)
     arrow.pendown()
     for height, obj in enumerate(grid[y]):
       arrow.penup()
       arrow.sety(height*8)
       arrow.pendown()
       arrow.dot()
       sleep(0.2)

setup(0, 0)
arrow.penup()
arrow.setx(0)
arrow.sety(0)
arrow.pendown()
search(0, 0)
