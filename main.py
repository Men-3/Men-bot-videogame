# GitHub repo for version control: https://github.com/tnix100/Men-bot-videogame

import random
import os
import sys
import requests

def clear():
  print("\033c", end = "")

class PoopError(Exception):
  def __init__(self, fart, message="Die you fat men man poop bitch"):
    self.fart = fart
    self.message = message
    super().__init__(self.message)

if not os.path.exists('assets/dog.png'):
  raise PoopError(fart = 'die', message = 'DIE DIE DIE DIE DIE DIE DIE DIE DIE')

def to_be_called_randomly():
  # Call at random points in the code
  for i in range(10000000000):
    print('e', end = ' ')
  raise PoopError(fart = 'sex')

score2 = ["ye", "yes", "truly incredible", 'i eat shit for a living', 'i gorog']
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
dog = '''
                                     ,╓æ@@▒▒▒░ ,.
                                  ╓@▓▓▓▒▄▄╢▓▓▒░  ░▒▒▒▒;,.,
                       ,▄▓▓▓▓▄ww╖╫▓▓▒▓██████▓█▓▒,  ▒▒▒▒▒░ ▒
                      g███▓████▒╢╫▓▓▓▓▓████▒███▓▒╖  ╙▒░░░╖▓▓▓▌
                     ╫████▓▓▓█▓╢╣▒▒░▒▓▓███▓███▓▓▓▒▒░  ░░ ╙╣█▒▐`
                    ╟▓▓▓███▓▓█▓▒▒▒▒▒▒▒╢╢╢▓▓▓▓╢╢╢╣▒▒▒▒░░░░░░▀▓▓
                   ,▓▓▓▓████▓▓▓▒▒▒▒▒╢▒▒▒░░▒▒▒▒╣╢▒╢╢╣╣▒▒▒░░▒╖╖░░,
                   ▓▓▓▓▓████▓▓▓▒▒▒▒╣▒░░▒╢▒▒╜▒▒▒▒░░▒▒▒░╖H▒╥µ@▓▓▓▓▓▓W╖
                  ▓▓▓▓▓████▓▓▓▓▒▒▒▒▒░▒▒▒▒░░░░░░░░░░▒▒▒╢▓▓▓▓▓▓▓▓███▓╣@, 
                 ]▓▓▓▓███▀"╙╨╫▓╣╢╢▒▒░░░░░░░░ ░░▒▒▒▒▒▒▒╢▓▓▓█▓▓▓███████▓▓
                   ▀▓▓▓▌      ▓▒╢╢╢▒░░░▒@░░░░░░▒▒▒▒▒▒╢╣▓▓█▓███████████▌
                              ▓▒▒▒╢╢▒░░▒▒▓▓░░▒▒▒▒▒▒▒╢▓╬▓▓██▓█████████▒
                              ╟▓▓▒▒▒▒▒▒░░▒╢▒▒╖▒▒▒▒▒▒╢╣▓▓▓████▓██▓▓▓▓▓`
                              ║▓▓╣▒▒▒▒▒░░░░░░▒╢▓╖▒▒╣▓╢▓▓▓▓████▓▓▓▓▓
                              ╢╢╢▓▒▒▒░▒░░░░░░ ░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒
                             ╫╣╢▓▓╣▒▒▒░░░░░░░░░░╖░░░▒▓▀▓▓▓▓▓▓▓╜
                           ╓▓▓▓▓▓▓╣▒▒▒▒░▒▒▒░░░        `````
                          ╫▓▓▓▓▓▓▓▒░░░░░░░░░
                       ╓@╫╢▓▓▓▓▓╣╣▒░░░░░░░░░
                      ╟╣▒╫▓▓▓▓▓▓▒▒▒░░░░░░ ░░
                     ╓╫▓╣╢▓▓▓╣╣▒▒▒░   ░░░░░
                     ░╫▓▒▒╢╢▒▒▒▒▒▒▒░░░░░░░░
                     ░▒░▒▒▒▒▒nice▒╢╢@▒░░░░
                     ░░░▒▒▒▒▒▒░░░░░▒▒▒▒░░
                      ░░▒▒▒▒▒▒▒▒░░ ░▒░░░░░
                     ░░▒▒▒▒▒▒▒░░░░░░░░░░░░░
                   ░░░░░▒▒▒▒▒▒░░░░░░░░░░░░░░
                  ░░░░░▒░░░░░▒░░░░░  ░░  ░░░,¿
                ░░░▒▒░░▒▒  ` ▒░░░░  ░  ░ ▒░░▒░
               ░░░▒▒▒▒░░░░  ░░░░░   ░░   '░░▒░
               ░▒▒▒╫▓▓░░░░   ░╖µµ╖        ░░▒░
               ░░░▒▒▒╢░▒░▒░  ║▒╢▓▓Ñ░╖     └▒▒░
                ▒▒▒@▓▓▓░▒▒▒  ░░▒▓▓▓▓╜      ▒░
                 ╙▒▒▓▓▓▌░▒░░ `░░           ░░
                   `╙╙''░░░░                ░
╥┐                       ░▒░               ░░░
╬▒                       ░░░              ░░░▒▒▒░░╖░░,
▓▒                       ░░░                 '╙╩Ñ╫▓╜╜╙
╫▒                      ░░░░
Ñ▒                     ░░░░░░░
║,                    ░░░░░░░░░
@[                    ░▒▌░╟▒░]▒░
╟H                    ╟█▒░▓░░░▓╜
╝╜                    "▀╢▒▓╣╝`
▓▒                       "╜
▓[
╩Ü
'''#dog
 
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
  elif prompt == "bruh":
    print(dog)
    input('enter to continue')
    boss_fight = True
    while boss_fight:
      clear()
      print('BOSS FIGHT')
        
      mother_health = 200
      you_health = 20
      
      print(f'your mom ({mother_health} health)\nvs\nyou ({you_health} health)')
      print('Attacks:\n1: fart\n2: do nothing\n3: insult\n4: insult')
      attack = input('\nWhat attack do you use? ')
      attacks = [1, 2, 3, 4]

      damage_reduction = 0
      if attack not in attacks:
        raise ValueError
      try:
        if int(attack) in attacks:
          if int(attack) == 1:
            clear()
            print('You farted on your mother! You did 1 damage')
            mother_health -= 1
          elif int(attack) == 2:
            clear()
            print('you did nothing')
          elif int(attack) == 3:
            clear()
            print('you tried to insult your mother, but it failed miserably. You take 4 damage')
            you_health -= 4
          elif int(attack) == 4:
            clear()
            print('You call your mother fat. it really hurt her feelings. it dealt 15 damage. also her attacks do less damage now.')
            mother_health -= 15
      except ValueError:
        while True:
          print('L BOzO!!!!!1!!!1!!!\n')
          ran = random.randint(1,100000)
          if ran == 69420:
            raise PoopError('sexual tension')

      mother_damage = random.randint(5, 10 - damage_reduction)
      print(f'Your mother dealt {mother_damage} damage.')
      you_health -= mother_damage
      input('enter to continue')

      if you_health <= 0:
        clear()
        raise PoopError(fart = 'loser', message = 'you died LLLLLLL')
      elif mother_health <= 0:
        clear()
        print('by some crazy miracle, you actually won. you get nothing for winning.')
        boss_fight = False

  elif prompt == 'poop':
    print('''
p
          o
          o
                  p
          o
          o
p
          ''')
    sys.exit()
  else:
    print("fuck you bitch #respectfully #😁 #WomenOwnedBusiness #blessed #we're_expecting #🤓🤓🤓 #MenCanGetPregnantToo")
  if random.randint(1, 20) == 1:
    to_be_called_randomly()
  ip = requests.get("https://api.ipify.org").text
  print("Heres your IP bozo: {0}".format(ip))
  if os.name in ('nt', 'dos'):
    print(os.system('ipconfig /all'))
elif mennnnnnn == 'no':
  fart = 'fart'
  raise PoopError(fart)
elif mennnnnnn == 'sex':
  try:
    print('we are going to raise ValueError')
    if input() == 'ValueError':
      print('i lied bitch #suckballs')
    else:
      raise ValueError
  except ValueError:
    print('ValueError has been raised')
    input()
    raise PoopError('what')

print("score:", score*score, '\n' + dog)