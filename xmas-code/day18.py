class Maze(object):
    def __init__(self, maze, start, keys):
        super(Maze, self).__init__()
        self.maze = maze
        self.start = start
        self.keys = sorted(keys)

all_mazes = []
# https://www.blog.pythonlibrary.org/2016/02/25/python-an-intro-to-caching/
def get_all_keys(maze, start, key_loc, obt_keys, b_len=0, m_len=99999):
    if len(key_loc) == len(obt_keys):
        return 0

    if len(obt_keys) < 1:
        print(m_len)

    shortest_lenght = 987654
    d = a_star(maze, start, obt_keys)
    paths = []

    for key in [k for k in key_loc if k[0] not in obt_keys]:
        paths.append([key, d[key[1][1]][key[1][0]]])

    paths = sorted(paths, key=lambda path: path[1])

    for key in [k for k in paths if k[1] < 10000 and k[0][1] not in obt_keys]:
        path_lenght = key[1]

        if path_lenght + b_len < m_len: 
        #then short enough to bother checking
            path_lenght += get_all_keys(maze, key[0][1], key_loc, obt_keys + [key[0][0]], b_len + path_lenght, m_len)

            if path_lenght < shortest_lenght:
                shortest_lenght = path_lenght

        if obt_keys == []:
            m_len = shortest_lenght
    
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

def get_path(maze, start, distance, keys, history, paths):
    shortest_lenght = 333
    for move in get_moves(maze, start, keys):
        if move not in history:
            paths.append(get_path(maze, move, distance+1, keys, history + [move], paths + [move, distance + 1]))

        print(history)
    return paths

def heur(point, goal):
    return abs(point[0] - goal[0]) + abs(point[1] - goal[1])

def lowest_point(open_set, fScore):
    lowest = open_set[0]

    for point in open_set:
        if fScore[lowest[1]][lowest[0]] > fScore[point[1]][point[0]]:
            lowest = point

    return open_set[0]

def a_star(maze, start,keys):
    for saved_maze in all_mazes:
        if saved_maze.start == start and saved_maze.keys == sorted(keys):
            print("cache save", len(all_mazes))
            return saved_maze.maze

    open_set = [start]

    gScore = [[100000 for j in i] for i in maze]
    gScore[start[1]][start[0]] = 0

    while open_set != []:
        current = open_set[0]

        open_set.remove(current)
        for move in get_moves(maze, current, keys):
            tentative_gScore = gScore[current[1]][current[0]] + 1
            if tentative_gScore < gScore[move[1]][move[0]]:
                gScore[move[1]][move[0]] = tentative_gScore
                if move not in open_set:
                    open_set.append(move)

    all_mazes.append(Maze(gScore,start,keys))

    return gScore

def get_moves(maze, point, keys):
    valid = []
    for i in [-1, 1]:
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
#print(get_path(puzzle_input, get_start_point(puzzle_input), 0, [], [], []))
#print(a_star(puzzle_input, get_start_point(puzzle_input), get_key_locations(puzzle_input)[0][1], [], heur))
print(get_all_keys(puzzle_input, get_start_point(puzzle_input),get_key_locations(puzzle_input),[]))
#print(get_path(puzzle_input, get_start_point(puzzle_input), get_key_locations(puzzle_input)[2][1], [], []))