def getans(n):
	S=set()
	for i in range(n):
		k,v=raw_input().split(' ')
		if not k in S:
			S.add(k)
			print k,v
getans(int(raw_input()))