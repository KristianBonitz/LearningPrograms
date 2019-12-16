class Moon (object):
    def __init__(self, x,y,z):
        super(Moon, self).__init__()
        self.x = x
        self.y = y
        self.z = z
        
        self.vx = 0
        self.vy = 0
        self.vz = 0
    
    def get_gravity(self, moon):
        self.vx += 1 if moon.x > self.x else -1 if moon.x < self.x else 0    
        self.vy += 1 if moon.y > self.y else -1 if moon.y < self.y else 0
        self.vz += 1 if moon.z > self.z else -1 if moon.z < self.z else 0
        
        #print(self.vx,self.vy,self.vz)
    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        
    def get_potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)
        
    def get_kenetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)
    
    def get_total_energy(self):
        return self.get_kenetic_energy() * self.get_potential_energy()

    def print(self):
        print('pos=',self.x,self.y,self.z, 'vel=', self.vx,self.vy,self.vz)
        
def apply_group_gravity(set):
    for m in set:
        for om in set:
            if m != om: m.get_gravity(om)
    
moon_set = [Moon(-7, 17, -11), Moon(9, 12, 5),Moon(-9, 0, -4),Moon(4, 6, 0)]
static_moon_set = [Moon(-7, 17, -11), Moon(9, 12, 5),Moon(-9, 0, -4),Moon(4, 6, 0)]
loop_steps = [[],[],[]]
steps = 0

while 186028 > steps:
    apply_group_gravity(moon_set)
    for x in moon_set: 
        x.apply_velocity()

    steps += 1

    #x
    if all(moon_set[i].vx == 0 for i in range(4)) == True and all(moon_set[i].x == static_moon_set[i].x for i in range(4)) == True:
        print([moon_set[i].vx == 0 for i in range(4)], [moon_set[i].x == static_moon_set[i].x for i in range(4)])
        print('x: ', end='')
        for x in moon_set: x.print()
        loop_steps[0] = steps

print(loop_steps)
for x in moon_set: x.print()
for x in static_moon_set: x.print()