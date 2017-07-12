
import random
from markov_bot import runBot

lines = 2
OUTPUT = runBot()

def outText():
	return OUTPUT

def gen_lyrics():	
	chunk = []
	for i in range(lines):
		with open('output.txt','r') as f:
			line = f.read()
			line = line.split('\n')

			new_line = random.choice(line)
			chunk.append(new_line)
			
	return '\n'.join(chunk)	

outText()
gen_lyrics()