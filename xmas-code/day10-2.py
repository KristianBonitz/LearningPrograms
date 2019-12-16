class Asteroid:
    """docstring for Asteroid"""
    def __init__(self, x, y, xp, yp, m, d):
        super(Asteroid, self).__init__()
        self.x = x 
        self.y = y 
        self.xp = xp 
        self.yp = yp 
        self.d = d
        self.rotation = 0 
        if xp > 0 and yp > 0:
            self.rotation = 1 
            self.m = m 
        elif xp > 0 and yp < 0:
            self.rotation = 2
            self.m = m * -1
        elif xp < 0 and yp < 0:
            self.rotation = 3
            self.m = m 
        elif xp < 0 and yp > 0:
            self.rotation = 4
            self.m = m * -1

    def __repr__(self):
         return repr((self.x, self.y, self.xp, self.yp,self.rotation, self.m, self.d))
        
def get_asteroids(array):
    coord_list = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == '#'  and [j,i] != [13,17] :
                coord_list.append(Asteroid(j, i, *get_m([j, i]), get_d([j, i])))
    return coord_list

def get_m(coord):
    x = (13 - coord[0])
    y = (17 - coord[1]) 
    
    xpos = -1 if x > 0 else 1
    ypos = -1 if y < 0 else 1 
    
    
    if y == 0:
        m = 10000000
    elif x == 0:
        m = 0
    else:
        m = abs(x/y) 
            
    return [xpos, ypos, m]

def get_d(coord):
    return abs(coord[1] - 17) + abs(coord[0] - 13)

def rotate_lazer(asteroids):
    a_list = sorted(asteroids, key = lambda a: (a.rotation, a.m, a.d))
    pre_m = 99
    lazer_order = []
    i = 0
    while len(a_list) > len(lazer_order):
        full_loop = True
        if a_list[i].m != pre_m and a_list[i] not in lazer_order:
            full_loop = False
            pre_m = a_list[i].m 
            lazer_order.append(a_list[i])
        
        if i == 0 and full_loop == True:
            pre_m = 99
            
        i = (i + 1) % len(a_list)
    return lazer_order
         

def find_asteroid_lines(coord_list):
    max_lines = 0

    for i in range(len(coord_list)):
        unique_lines = []
        unique_coord = []
        for j in range(len(coord_list)):
            y = (coord_list[i].y - coord_list[j].y) 
            x = (coord_list[i].x- coord_list[j].x)
            
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

f = open("input.txt")
puzzle_input = [j.strip() for i, j in enumerate(f)]

#print(find_asteroid_lines(get_asteroids(puzzle_input)))
print(rotate_lazer(get_asteroids(puzzle_input)))