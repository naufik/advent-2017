'''
	Advent of Code - Day 8
	I Heard You Like Registrars
	
	High-Level Solution by Naufal Fikri
	http://github.com/naufik
'''


COMPARISONS = {'>': (lambda x, y: x > y), '==': (lambda x,y: x == y), '<': (lambda x,y: x < y), '>=': (lambda x,y: x >= y), '!=': (lambda x,y: x != y), '<=': (lambda x,y: x <= y)}
OPERATIONS = {'inc': (lambda x: x), 'dec': (lambda x: -x)}

def apply_instruction(inst, mem):
	''' Mutates the memory by applying the instruction. Returns the memory set after the mutation. '''	
	
	tvar, op, delta, ignored, cvar, cond, cval = inst.split(' ')
	
	if cvar not in mem:
		mem[cvar] = 0

	if tvar not in mem:
		mem[tvar] = 0

	if COMPARISONS[cond](mem[cvar], int(cval)):
		mem[tvar] += OPERATIONS[op](int(delta))

	return mem

# Initialize the 'memory' and read the input instruction files.
memory = dict()
max_per_step = []
instruction_set = open("testcase", "r").read().split('\n')[:-1]

for instruction in instruction_set:
	memory = apply_instruction(instruction, memory)
	max_per_step.append(max(memory.values()))

# This prints the answer to part 1 of the problem. (Finding maximum value at final state)
print(max(memory.values()))

# This prints the answer to part 2 of the problem. (Finding maximum value ever held)
print(max(max_per_step))