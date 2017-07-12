import random
import sys
	
def build_chain(text, chain = {}):
    words = text.split(' ')
    index = 1
    for word in words[index:]:
        key = words[index - 1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1
    
    return chain

def generate_message(chain, count = 1000):
    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    
    return message


def read_file(filename):
    with open('mg_lyrics.txt', "r") as file:
        contents = file.read()
    return contents

def write_file(filename, message):
    with open(filename, "w") as file:
        file.write(message)
             
def runBot():
    message = read_file(sys.argv[0])
    chain = build_chain(message)
    message = generate_message(chain)
    write_file("output.txt", message)

