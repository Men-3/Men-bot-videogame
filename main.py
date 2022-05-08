# GitHub repo for version control: https://github.com/tnix100/Men-bot-videogame

import random
import os
import requests

def clear():
  print("\033c", end = "")

class PoopError(Exception):
  def __init__(self, fart, message="Die you fat men man poop bitch"):
    self.fart = fart
    self.message = message
    super().__init__(self.message)

if not os.path.exists('assets/dog.png'):
  raise PoopError('DIE DIE DIE DIE DIE DIE DIE DIE DIE')

def to_be_called_randomly():
  while True:
    print('e', end = ' ')

score2 = ["ye", "yes", "truly incredible", 'i eat shit for a living']
score = 0
amogus = '''
⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠒⠛⠉⠙⠳⡄⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⢠⣴⣾⣿⣷⣦⣄⠀⠀⠀⡤⠟⠚⠛⠛⠓⡆⠀⢷⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠿⠟⠛⠛⠳⣄⠸⣇⡀⠀⣀⣀⣰⡇⠀⢸⠓⢲⡀⠀
⠀⠀⠀⠀⢠⣶⣾⣿⣿⣿⣷⣦⣤⣤⣤⣼⠆⡟⠻⠿⠿⠿⠟⠁⠀⢸⡇⢰⡇⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⠇⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣇⠀⠀⠀⠀⠀⠀⠀⠈⣧⣸⠀⠀
⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢻⠀⢀⣀⣀⣴⠀⠀⠀⢹⠅⠀⠀
⠀⠀⠀⢀⡀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡏⠀⠀⢸⡇⣿⠀⠀⠀⢸⠀⠀⠀
⠀⠀⣠⣼⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⡇⠀⠀⢸⡇⣿⠀⠀⠀⣼⠀⠀⠀
⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⣿⠀⠀⢸⡇⢸⠀⠀⠀⡿⠀⠀⠀
⠈⠉⠁⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢿⠀⠀⣸⠁⢸⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⡿⠟⠀⠀⢸⡄⠀⣯⠀⣸⠀⠀⢰⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠀⠀⠀⠀⠀⢯⠀⠘⡇⢹⡆⠀⠸⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡿⠃⠀⠀⠀⠀⠀⢸⠀⢠⡇⢸⡇⠀⢰⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⢸⠀⣼⠀⠀⡇⠀⣼⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⢶⣯⣭⠤⠿⣠⣖⣃⣀⣹⡄⠀⠀⠀
mogus'''
mennnnnnn = input("is men good?").lower()
if mennnnnnn in score2:
  if random.randint(1, 20) == 1:
    to_be_called_randomly()
  print("good boy")
  score += random.randint(1,2346578363834578364582759864595778936457236456325627834582345534568973745763456357346583465893458693)
  prompt = input('bruh: ').lower()
  if prompt == 'hfioweqfj weorfwejifwejhirwehfiowq':
    print(amogus)
    print('NO WAY IS THAT THE  IMPOSTaR FROM AMONG US??!!?!😫😫!!!!11!?!😆😆😆😆???')
  elif prompt == 'balls fart':
    print('hfeiuwfui3efheqjawejkswdasmdanwg mnjsmvxsw m,jsw m,s,mvnjsmjklnfmnsdnegb dn,v rd f,srhgejrl bqguawmehfgskers,d fhgks byt')
  else:
    print("fuck you bitch #respectfully #😁 #WomenOwnedBusiness #blessed #we're_expecting")
  if random.randint(1, 20) == 1:
    to_be_called_randomly()
  ip = requests.get("https://api.ipify.org").text
  print("Heres your IP bozo: {0}".format(ip))
  if os.name in ('nt', 'dos'):
    print(os.system('ipconfig /all'))
elif mennnnnnn == 'no':
  fart = 'fart'
  raise PoopError(fart)

print("score:", score*score)

