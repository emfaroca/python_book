stuff = ('hello', 'world', 'bye', 'now')

stuff['bye'] = 'goodbye'

print(stuff)

#this doesn't work bc tuples are immutable

stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
