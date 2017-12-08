'''
	Advent of Code - Day 5
	A Maze of Twisty Trampolines, All Alike

	High-Level Solution by Naufal Fikri
	http://github.com/naufik
'''

def maze_exit(instructions):
	path = [0]
	while (0 <= path[-1] < len(instructions)):
		path.append(path[-1] + instructions[path[-1]])
		instructions[path[-2]] += 1

	return path

text = open("testcase").read()
sequence = [int(k) for k in text.split('\n') if k != '']

print(len(maze_exit(sequence)) - 1)