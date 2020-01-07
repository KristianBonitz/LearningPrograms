class Maze(object):
    def __init__(self, maze):
        super(Maze, self).__init__()
        self.maze = maze
        self.starting_point = get_start_point(maze)
        self.maze_keys = get_key_locations(maze)
        self.obt_keys = []
    
def get_all_keys(maze, start, key_loc, obt_keys):
    shortest_lenght = 987654
    for key in key_loc:
        if key[0] not in obt_keys:
            print(key[0], obt_keys)
            if len(obt_keys) + 1 == len(key_loc):
                #print(start, key, obt_keys, get_path(maze, start, key[1], obt_keys, []))
                return get_path(maze, start, key[1], obt_keys, [])
            else:
                #print(start, key, obt_keys, get_path(maze, start, key[1], obt_keys, []))
                path_lenght = get_path(maze, start, key[1], obt_keys, []) 
                if path_lenght < 100:
                    path_lenght += get_all_keys(maze, key[1], key_loc, obt_keys + [key[0]])
                    if path_lenght < shortest_lenght:
                        shortest_lenght = path_lenght   
    
    return shortest_lenght

def get_all_keys_depth(maze, start, key_loc, obt_keys, p_len=0, s_len=9999):
    paths = []

    if len(key_loc) == len(obt_keys):
        return 0

    for key in [k for k in key_loc if k[0] not in obt_keys]:
        paths.append([key, get_path(maze, start, key[1], obt_keys, [])])

    paths = sorted(paths, key=lambda path: path[1])
    print(paths)

    for key in [k for k in paths if k[1] < 3000 and k[0][1] not in obt_keys]:
        p_len += get_all_keys_depth(maze, key[0][1], key_loc, obt_keys + [key[0][0]], key[1], s_len)
        print(s_len, p_len,len(key_loc),len(obt_keys))
        if s_len > p_len and obt_keys == []:
            s_len = p_len

        break

    return s_len 

def get_path(maze, start, end, keys, history):
    shortest_lenght = 333
    for move in get_moves(maze, start, keys):
        if move not in history:
            if move == end:
                return 1
            else:
                path_lenght = 1 + get_path(maze, move, end, keys, history + [move])
                if path_lenght < shortest_lenght:
                    shortest_lenght = path_lenght   
    return shortest_lenght

def get_moves(maze, point, keys):
    valid = []
    for i in range(-1, 2):
        if vaild_move(maze[point[1] + i][point[0]], keys):
            valid.append([point[0], point[1] + i])

        if vaild_move(maze[point[1]][point[0] + i], keys):
            valid.append([point[0] + i, point[1]])
    
    return valid

def vaild_move(tile, key):
    if tile == '.':
        return True
    elif tile == '#':
        return False
    elif tile == '@':
        return True
    elif tile >= 'a' and tile <= 'z':
        return True
    elif tile >= 'A' and tile <= 'Z':
        return tile.lower() in key

def get_key_locations(maze):
    keys = []
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] >= 'a' and maze[y][x] <= 'z':
                keys.append([maze[y][x],[x,y]])
    return keys

def get_start_point(maze):
    keys = []
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == '@':
                return [x,y]
    return None

f = open("input.txt")
puzzle_input = [j.strip() for i, j in enumerate(f)]

print(get_all_keys_depth(puzzle_input, get_start_point(puzzle_input),get_key_locations(puzzle_input),[]))
#print(get_path(puzzle_input, get_start_point(puzzle_input), get_key_locations(puzzle_input)[2][1], [], []))