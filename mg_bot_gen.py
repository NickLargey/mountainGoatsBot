import random

lines = 2
def gen_lyrics():
	chunk = []
	for i in range(lines):
		with open('mg_lyrics.txt','r') as f:
			line = f.read()
			line = line.split('\n')

			new_line = random.choice(line)
			chunk.append(new_line)
			
	return '\n'.join(chunk)

gen_lyrics()