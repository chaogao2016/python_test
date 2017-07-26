from sys import exit

from random import randint

def death():
    quips = ["You died. You kinda suck at this.",
            "Nice job, you died ... jackass.",
            "Such a luser.",
            "I have a small puppy that's better at this."]
    print quips[randint(0,len(quips) - 1)]
    exit(1)

def central_corridor():
    print "The Gothons of Planet percal #25 have invaded your ship and destroyed"

    print "your entire crew. You are the last surviving member and your last"

    print "mission is to get the neutron destruct bomb from the Weapons Armory."

    print "put it in the bridge, and blow the ship up after getting into an "

    print "escape pod."

    print "\n"

    print "You're running down the central corridor to the Weapons Armory when"

    print "a Gothon jups out , red scaly skin,dark grimy teeth, and evil clown costume"

    print "flowing around his hate filled body. He's blcoking the door to the"

    print "Armory and about to pull a weapon to blast you."

    action = raw_input("> ").strip()

    if action == "shoot!":
        print "Quick on the draw yu yank out yourbaster and fire it at the Gothon."

        print "His clown costume is flowing and moving around "
