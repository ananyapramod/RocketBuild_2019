def getans(n):
	S=set()
	for i in range(n):
		k=raw_input()
		if k in S:
			print "YES"
		else:
			print "NO"
			S.add(k)
getans(int(raw_input()))