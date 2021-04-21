# Alright, this is my first attempt. I'll try to be as original as possible.
from sys import exit
import webbrowser
import time


YES_STRINGS = ['yes,', 'yeah', 'okay', 'sure', 'why not', 'hell yeah','yup']
NO_STRINGS = ['no', 'nope', 'nah', 'no way']


def beet_room():
	print """You are greeted by a humble beet farmer named Mose.
'You have to give me your keys now.'
What do you do?"""

	next = raw_input("Give or No - ")

	if "give" in next:
		wrestle()
	elif "no" in next:
		bear_attack()
	else:
		wtf()

def wrestle():
	print """I'm not sure why you'd just give your keys to a stranger.
Whatever. Mose has your keys and now he wants to wrestle.
Are you intending on fighting clean or dirty?"""

	next = raw_input("> ")

	if "clean" in next:
		print "Your chivalry is noted. Not by Mose, though. He kills you pretty\
		 easily, and it ain't pretty."
	elif "dirty" in next:
		print "Smart move. You poke Mose in the scrote with the business-end of\
		 a morning star."
		print "I can assure you, it did not tickle. You win. Congrats, amigo."
	else:
		wtf()

def wtf():
	print """Well, congratulations. You've broken my fucking game.
I am awful at this and I'm doing my best,
but your incompetence isn't helping anything.
Do me a favor. Try again and dissapoint me and your parents less."""

def bear_attack():
	print """You decided to NOT give your keys to the valet? What kind of 
Karen-ass Baby-booming, Speak-to-the-Manager fuck are you?
Whatever. Mose is pissed and he summoned his pet bear to accost you.
What's the plan?
Fight or play dead?"""

	next = raw_input("> ")

	if "fight" in next:
		print """It sure takes cajones to fight a fucking grizzly bear."
Congratulations, you won."
The game I mean, not the fight with the Grizzly."
The grizzly FUCKED you up."""
	elif "play dead" in next:
		print """Mose LITERALLY just saw you refuse him your keys.
Is this some kind of joke to you?
No pithy remarks for you. The bear eats you. You die. The rest of your family dies.
Reconsider your choices, nerd."""
	else:
		wtf()

def sax_room():
	print """A muscular man sits in the middle of a dimly-lit room.
His stoney demeanor doesn't change as you stride towards him,
noticing the misshapen heap of brass in his lap.
'I require a tribute of bacon.'"""

	next = raw_input("Give or No? - ")

	if "give" in next:
		he_accepts()
	elif "no" in next:
		punishment()
	else:
		wtf()

def he_accepts():
	print "The Duke is pleased with your offering of meat and salt."
	print "You may don the ermine mantle of justice and take your place among us."
	time.sleep(6)

	webbrowser.open("https://www.youtube.com/watch?v=6iFbuIpe68k", new=1)

def punishment():
	print """It seems churlish to not offer this man some bacon
Didn't your mother ever teach you to respect your
strange, homo-erotic deities?"""


def start():
	print """You are presented with three doors, each more eloquently embossed than the next.
On the first door, there is a beet. Rubies on garnet, with lapiz-lazulai inlay.
On the second door, a serpentine musical instrument wrought in brass, terrible to behold.
Which door do you take?"""

	next = raw_input("> ")

	if "first" in next:
		beet_room()
	elif "second" in next:
		sax_room()
	else:
		wtf()

	

	"""if next in YES_STRINGS:
		beet_room()
	else:
		wtf()


# add this to y/n questions?
# if answer in YES_STRINGS:
"""


start()
