'''
	Advent of Code - Day 2
	Corruption Checksum

	High-Level Solution by Naufal Fikri
	http://github.com/naufik
'''

def sheet_checksum(sheet):
	''' Calculates the checksum of the spreadsheet, when given as a list-of-lists '''
	return sum([max(row) - min(row) for row in sheet])


def parse_sheet(text):
	''' Parses a string into a 2d spreadsheet of floats '''
	return [[float(entry) for entry in line.split('\t')] for line in text.split('\n')[:-1]]

sheet = parse_sheet(open("testcase", "r").read())
print(sheet_checksum(sheet))