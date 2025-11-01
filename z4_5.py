def odwracanie(L: list, left, right):
	L_odwr=[]
	for x in range(0, right-left+1):
		L_odwr.append(L[right-x])

	L[left:right+1]=L_odwr

	print(L)

odwracanie([1,4,5,6,7,8], 1, 4)
