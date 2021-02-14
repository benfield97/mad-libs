nouns = []
names = []

noun = input('Gimme a noun ')
nouns.append(noun)
name = input("Gimme a name ")
names.append(name)
superlative = input("Gimme a word ending with 'est' ")
profession = input("Gimme a profession ")
name = input("Gimme another name ")
names.append(name)
noun = input("Gimme another noun ")
nouns.append(noun)
adjective = input("Gimme another adjective ")
animal = input("Gimme an animal ")
verb = input("Gimme a verb ")


story = f"""This is the story of a {nouns[0]} named {names[0]}, {names[0]} was the {superlative} {profession} in the world.
One day {names[0]} decided that they didn't want to be a {nouns[0]} anymore and so they went to their friend {names[1]}, 
who was a {nouns[1]}, {names[1]} told {names[0]} that all they needed to do was get a {adjective} {animal} and {verb} at it aggressively.

"""

print(story)
