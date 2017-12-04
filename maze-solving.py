from turtle import Turtle, setup, done, delay, tracer, screensize
from time import sleep
from sys import argv
from random import randrange

#grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#				[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1],
#				[1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
#       [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 2, 1],
#				[1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
#       [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
#       [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
#				[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
#				[1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
#				[1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
#				[1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
#				[1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
#				[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
#				[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
#				[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

grid = []
value = (argv[1])
solv = False

arrow = Turtle()
setup(width=600, height=600, startx=600, starty=None)
delay(0)

def search(x, y):
	arrow.color('green')
	arrow.shape('turtle')
	arrow.resizemode('user')
	arrow.shapesize(0.35, 0.35)
	#arrow.penup()

	if grid[x][y] == 2:
		print ('found at %d,%d' % (x, y))
		done()
		return True
	elif grid[x][y] == 1:
		print ('wall at %d,%d' % (x, y))
		return False
	elif grid[x][y] == 3:
		print ('visited at %d,%d' % (x, y))
		return False

	#sleep(0.5)
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
  arrow.penup()
  arrow.speed('fastest')
  for width, width_obj in enumerate(grid[x]):
    print ('width: '+str(width))
    arrow.setx(width*8)
    arrow.penup()
    for height, height_obj in enumerate(grid[y]):
      print ('height: '+str(height))
      arrow.sety(height*8)
      if height_obj == 1:
        arrow.pendown()
        #arrow.circle(1)
        arrow.dot()
        arrow.penup()
      elif height_obj == 2:
        arrow.pendown()
        arrow.color('red')
        #arrow.circle(1)
        arrow.dot()
        arrow.color('black')
        arrow.penup()
      else:
        arrow.penup()
        #sleep(0.2)
    y+=1

def random(value):
  for x in range(value):
    add = []
    for y in range(value):
      print('x: '+str(x))
      print('y: '+str(y))
      if x == 0 or x == value-1 or y == 0 or y == value-1:
        add.append(1)
      elif x == 1 and y == 1:
        add.append(0)
      elif x == value-2 and y == value-2:
        add.append(2)
      else:
        try:
          if grid[y][y] == 0:
            add.append(0)
          else:
            add.append(randrange(0, 2))
        except:
          add.append(randrange(0, 2))

    grid.append(add)

  print (grid)

while True:
  random(int(value))
  def check(x,y):
    global solv
    if grid[x][y] == 2:
      print ('found at %d,%d' % (x, y))
      solv = True
      print (grid)
      for index, obj in enumerate(grid):
        i = -1
        for x in obj:
          print(str(x)+'x')
          if x == 3:
            grid[index][i] = 0
            print('g'+str(grid[index][i]))
          i+=1
        #grid[index][x] = 0
      return True
    elif grid[x][y] == 1:
      print ('wall at %d,%d' % (x, y))
      return False
    elif grid[x][y] == 3:
      print ('visited at %d,%d' % (x, y))
      return False

    grid[x][y]=3
    if x < len(grid)-1 and check(x+1, y) \
    or y > 0 and check(x, y-1) \
    or x > 0 and check(x-1, y) \
    or y < len(grid)-1 and check(x, y+1):
      solv = True
      return True
    return False
  check(1,1)
  if not solv == True:grid = []
  else:break

setup(0, 0)
arrow.penup()
arrow.setx(0)
arrow.sety(0)
arrow.pendown()
search(1, 1)
