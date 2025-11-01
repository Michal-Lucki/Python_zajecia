flattened=[]
def flatten(sequence):
	global flattened
	for x in sequence:
		if isinstance(x, (list,tuple)):
			flatten(x)
		else:
			flattened.append(x)
	return flattened

sekwencja=(0,1,[2,[3,4,(5,6),7],6,()],(5,(4,(3,2),1)),0)

print(flatten(sekwencja))