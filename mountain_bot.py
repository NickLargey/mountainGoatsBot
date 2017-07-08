import random


def get_lyrics():
	chunk = []
	i = 0
	while i <= 3:
		with open('mg_lyrics.txt','r') as f:
			line = f.read()
			line = line.split('\n')

			new_line = random.choice(line)
			chunk.append(new_line)
			
			i += 1
			
	print('\n'.join(chunk))

get_lyrics()
