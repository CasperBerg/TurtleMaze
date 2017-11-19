from turtle import Turtle, setup, done
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
indx, obj = (argv[1], argv[1])

arrow = Turtle()
setup(width=600, height=600, startx=0, starty=0)

def search(x, y):
	arrow.color('green')
	arrow.shape('turtle')
	arrow.resizemode('user')
	arrow.shapesize(0.35, 0.35)
	arrow.penup()

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
					arrow.circle(1)
					#arrow.penup()
				elif height_obj == 2:
					arrow.pendown()
					arrow.color('red')
					arrow.circle(1)
					arrow.color('black')
					#arrow.penup()
				else:
					arrow.penup()
				#sleep(0.2)
		y+=1

def random(indx, obj):
  add = []
  for x in range(indx):
    for y in range(obj):
      add.append(randrange(0, 1))
  for i, o in enumerate(add):
    up = i-1
    down = i+1
    try:
      if i
    for 0 in o:
      add[][o]
  grid.append(add)
  print (grid)

random(int(indx), int(obj))
#setup(0, 0)
arrow.penup()
arrow.setx(0)
arrow.sety(0)
arrow.pendown()
#search(1, 1)
