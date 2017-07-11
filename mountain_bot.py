import time

from api import getAPI
from mg_bot_gen import gen_lyrics

API = getAPI()
GENERATOR = gen_lyrics()

print(GENERATOR)	
API.update_status(GENERATOR)
time.sleep(15)

print('Done!')
