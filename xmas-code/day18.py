class Point(object):
    """docstring for point"""
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.x = x  
        self.y = y
        
class Maze(object):
    def __init__(self, maze):
        super(Maze, self).__init__()
        self.maze = maze
        self.starting_point = get_start_point(maze)
        self.maze_keys = get_key_locations(maze)
        self.obt_keys = []
    
    def get_all_keys(self, moon):
        pass
        
        #print(self.vx,self.vy,self.vz)
def get_path_lenght(maze, start, end, keys, history):
    for move in get_moves(maze, start, keys):
        if move not in history:
            history.append(move)
            if move == end:
                return 1
            else:
                return 1 + get_path(maze, start, end, keys, history)    
        
    return 10000

def get_moves(maze, point, keys):
    valid = []
    for i in range(-1, 2):
        if vaild_move(maze[point.y + i][point.x], keys):
            valid.append([point.x, point.y + i])

        if vaild_move(maze[point.y][point.x + i], keys):
            valid.append([point.x + i, point.y])
    
    return valid

def vaild_move(tile, key):
    if tile == '.':
        return True
    elif tile == '#':
        return False
    elif tile >= 'a' and tile <= 'z':
        return True
    elif tile >= 'A' and tile <= 'Z':
        return tile.lower() in key

f = open("input.txt")
puzzle_input = [j.strip() for i, j in enumerate(f)]

print(get_path(puzzle_input, Point(5,1), Point(7,1), [], []))
