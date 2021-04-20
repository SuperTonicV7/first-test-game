# Alright, this is my first attempt. I'll try to be as original as possible.
from sys import exit

YES_STRINGS = ['yes,', 'yeah', 'okay', 'sure', 'why not', 'hell yeah','yup']


def beet_room():
	print "You are greeted by a humble beet farmer named Mose."
	print "'You have to give me your keys now.'"
	print "What do you do?"

	next = raw_input("> ")

	if "give" in next:
		wrestle()
	else:
		bear_attack()

def wrestle():
	print "I'm not sure why you'd just give your keys to a stranger."
	print "Whatever. Mose has your keys and now he wants to wrestle."
	print "Are you intending on fighting clean or dirty?"

	next = raw_input("> ")

	if "clean" in next:
		print "Your chivalry is noted. Not by Mose, though. He kills you pretty easily, and it \
		ain't pretty."
	elif "dirty" in next:
		print "Smart move. You poke mose in the scrote with the business-end of a morning star."
		print "I can assure you, it did not tickle. You win. Congrats, amigo."
	else:
		wtf()

def wtf():
	print "Well, congratulations. You've broken my fucking game."
	print "I am awful at this and I'm doing my best,"
	print "but your incompetence isn't helping anything."
	print "Do me a favor. Try again and dissapoint me and your parents less."

def bear_attack():
	print "You decided to NOT give your keys to the valet? What kind of Karen-ass Baby-booming \
	Speak-to-the-Manager fuck are you?"
	print "Whatever. Mose is pissed and he summoned his pet bear to accost you. What's the plan?"
	print "Fight or play dead?"

	next = raw_input("> ")

	if "fight" in next:
		print "It sure takes cajones to fight a fucking grizzly bear."
		print "Congratulations, you won."
		print "The game I mean, not the fight with the Grizzly."
		print "The grizzly FUCKED you up."
	elif "play dead" in next:
		print "Mose LITERALLY just saw you refuse him your keys."
		print "Is this some kind of joke to you?"
		print "No pithy remarks for you. The bear eats you. You die. The rest of your family dies."
		print "Reconsider your choices, nerd."

def start():
	print "You are presented with three doors, each more eloquently embossed than the next."
	print "On the first door, there is a beet. Rubies on garnet, with lapiz-lazulai inlay."
	print "This is the only fucking door available during this demo."
	print "Do you take the door?"

	next = raw_input("> ")

	if next in YES_STRINGS:
		beet_room()
	else:
		wtf()


# add this to y/n questions?
# if answer in YES_STRINGS:


start()