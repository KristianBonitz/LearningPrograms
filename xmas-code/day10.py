def asteroids(array):
	coord_list = []
	for i in range(len(array)):
		for j in range(len(array[i])):
			if array[i][j] == '#':
				coord_list.append([i,j])

	return coord_list

def find_asteroid_lines(coord_list):
	max_lines = 0

	for i in range(len(coord_list)):
		unique_lines = []
		for j in range(len(coord_list)):
			y = (coord_list[i][1] - coord_list[j][1]) 
			x = (coord_list[i][0] - coord_list[j][0]) 
			m = (x/y if y != 0 else None)
			if m not in unique_lines:
				unique_lines.append(m)

		if(max_lines < len(unique_lines)):
			max_lines = len(unique_lines)

	return max_lines

puzzle_input = ["#.#...#.#.",
".###....#.",
".#....#...",
"##.#.#.#.#",
"....#.#.#.",
".##..###.#",
"..#...##..",
"..##....##",
"......#...",
".####.###."]

print(find_asteroid_lines(asteroids(puzzle_input)))