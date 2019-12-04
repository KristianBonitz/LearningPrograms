##Create a grid that expands
path1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
path2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

start_grid = [[-1]]

#add row 

def move_up(grid, x, y):
	if y == 0:
		grid.insert(0, [0 for z in grid[0]])
		grid[0][x] += 1
		return grid, x, 0
	else:
		grid[y-1][x] += 1
		return grid, x, y-1

def move_down(grid, x, y):
	if y+1 >= len(grid):
		grid.append([0 for z in grid[0]])
		grid[y+1][x] += 1
		return grid, x, y+1
	else:
		grid[y+1][x] += 1
		return grid, x, y+1
		
def move_left(grid, x, y):
	if x == 0:
		for row in grid:
			row.insert(0,0)

		grid[y][0] += 1
		return grid, 0, y
	else:
		grid[y][x-1] += 1
		return grid, x-1, y

def move_right(grid, x, y):
	if x+1 >= len(grid[y]):
		for row in grid:
			row.append(0)

		grid[y][x+1] += 1
		return grid, x+1, y
	else:
		grid[y][x+1] += 1
		return grid, x+1, y

#add col
def print_grid(grid,x,y):
	for z in grid:
		print(z)
	print('--',x,y,'--')



print_grid(*move_up(start_grid,0,0))
print_grid(*move_left(start_grid,0,0))
print_grid(*move_down(start_grid,0,0))
print_grid(*move_down(start_grid,0,1))
print_grid(*move_right(start_grid,0,2))


