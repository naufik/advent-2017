'''
	Advent of Code - Day 5
	A Maze of Twisty Trampolines, All Alike

	High-Level Solution by Naufal Fikri
	http://github.com/naufik
'''

def maze_exit(instructions):
	''' Finds the path to exit the instruction set given. Notice that '''
	path = [0]
	while (0 <= path[-1] < len(instructions)):
		path.append(path[-1] + instructions[path[-1]])
		instructions[path[-2]] += 1

	return path

# read and parse the testcase file
text = open("testcase").read()
sequence = [int(k) for k in text.split('\n') if k != '']

# print how many 'jumps' are required to finish exit the instruction set
# note that the 'start' line is excluded.
print(len(maze_exit(sequence)) - 1)