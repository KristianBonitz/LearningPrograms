class Asteroid:
    """docstring for Asteroid"""
    def __init__(self, x, y, xp, yp, m, d):
        super(Asteroid, self).__init__()
        self.x = x 
        self.y = y 
        self.xp = xp 
        self.yp = yp 
        self.m = m 
        self.d = d
    def __repr__(self):
         return repr((self.x, self.y, self.xp, self.yp, self.m, self.d))
        
def get_asteroids(array):
    coord_list = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '#':
                coord_list.append(Asteroid(j, i, *get_m([j, i]), get_d([j, i])))
    return coord_list

def get_m(coord):
    x = (coord[0] - 11)
    y = (coord[1] - 13) 
    
    xpos = -1 if x < 0 else 1
    ypos = -1 if y < 0 else 1 
    
    m = abs(x/y) if y != 0 else 100000000
            
    return [xpos, ypos, m]

def get_d(coord):
    return abs(coord[1] - 13) + abs(coord[0] - 17)

def rotate_lazer(asteroids):
    a_list = sorted(sorted(asteroids, key = lambda a: a.d), key = lambda a: (a.xp, a.yp, a.m), reverse = True )
    pre_m = 99
    lazer_order = []
    i = 0
    while len(a_list) > len(lazer_order):
        
        if a_list[i].m != pre_m:
            pre_m = a_list[i].m 
            lazer_order.append(a_list[i])
        
        i = (i + 1) % len(a_list)
    return lazer_order
         

def find_asteroid_lines(coord_list):
    max_lines = 0

    for i in range(len(coord_list)):
        unique_lines = []
        unique_coord = []
        for j in range(len(coord_list)):
            y = (coord_list[i][1] - coord_list[j][1]) 
            x = (coord_list[i][0] - coord_list[j][0])
            
            xpos = 1 if x > 0 else -1
            ypos = 1 if y > 0 else -1 
            
            m = abs(x/y) if y != 0 else None
            
            if [xpos,ypos,m] not in unique_lines and coord_list[i] != coord_list[j]:
                
                unique_lines.append([xpos,ypos,m])
                unique_coord.append([coord_list[j], m])
            
        print(coord_list[i], len(unique_lines))

        if(max_lines < len(unique_lines)):
            max_lines = len(unique_lines)

    return max_lines

puzzle_input = [
".#..##.###...#######",
"##.############..##.",
".#.######.########.#",
".###.#######.####.#.",
"#####.##.#.##.###.##",
"..#####..#.#########",
"####################",
"#.####....###.#.#.##",
"##.#################",
"#####.##.###..####..",
"..######..##.#######",
"####.##.####...##..#",
".#####..#.######.###",
"##...#.##########...",
"#.##########.#######",
".####.#.###.###.#.##",
"....##.##.###..#####",
".#.#.###########.###",
"#.#.#.#####.####.###",
"###.##.####.##.#..##"]
print(rotate_lazer(get_asteroids(puzzle_input)))