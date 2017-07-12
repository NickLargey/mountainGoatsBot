import time
from random import randint
from datetime import datetime

from api import getAPI
from mg_bot_gen import gen_lyrics, outText

numTweets = 10
API = getAPI()
OUTPUT = outText()


def text():
	return OUTPUT

def tweetBurst():
	for i in range(numTweets):
		GENERATOR = gen_lyrics()
		timeRange = randint(1, 100)
		print(GENERATOR)
		print('Will sleep for ' + str(timeRange) + ' seconds...')	
		
		API.update_status(GENERATOR)
		time.sleep(int(timeRange))

	print('Done!')

text()
tweetBurst()