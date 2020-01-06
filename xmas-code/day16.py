f = open("input.txt")
puzzle_input = f.readline()

def fft_algorithm(signal, pattern):
	s_out = ""
	for j in range(len(signal)):
		lp = gen_pattern(pattern, j)
		s_sum = 0
		for k in signal:
			s_sum += (int(k)*lp[j+1%len(lp)])
		s_out += s_sum % 10 if s_sum >= 0 else s_sum * -1 % 10


def gen_pattern(pattern, digit):
	out_pattern = []
	for j in pattern:
		out_pattern += [j] * (digit+1)

	return out_pattern

solution = 0
for i in range(1):
	solution = fft_algorithm(puzzle_input, [0, 1, 0, -1])

print(solution)