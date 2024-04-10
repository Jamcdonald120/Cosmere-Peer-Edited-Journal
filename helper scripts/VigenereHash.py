class Alphabet:
	def __init__(this, alpha):
		this.toUpper=True
		this.alphabet=alpha
		this.lookup=dict()
		this.len=len(this.alphabet)
		for i in range(len(alpha)):
			this.lookup[alpha[i]]=i
	def ord(this,symbol):
		if this.toUpper:
			symbol=symbol.upper()
		return this.lookup[symbol]
	def chr(this,num):
		return this.alphabet[num]
def uniqueChar(input):
	map={}
	for c in input:
		if c in map:
			map[c]+=1
		else:
			map[c]=1
	for k in sorted(map):
		
		print (k,map[k])
alpha=Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ_#0123456789=+-*/%&.,?()[]\"';:|@")	
#alpha=Alphabet("AB_#12")
def cypher(a,b):
	ia=0;
	ib=0;
	if(isinstance(a,int)):
		ia=a
	else:
		ia=alpha.ord(a)
	if(isinstance(b,int)):
		ib=b
	else:
		ib=alpha.ord(b)	
	#print("cypher",b,a,alpha.chr((ia+ib)%alpha.len))
	return alpha.chr((ia+ib)%alpha.len)
	
	
def v1(initial,text):
	rollingKey=initial
	for c in text:
		rollingKey+=cypher(c,rollingKey[0])
		rollingKey=rollingKey[1:]
	return rollingKey
	
def v2(initial,text):
	rollingKey=initial
	holder=initial[-1]
	for c in text:
		#print(c)
		key=cypher(holder,rollingKey[0])
		holder=cypher(c,key)
		
		rollingKey+=holder
		rollingKey=rollingKey[1:]
		#print(rollingKey,holder,"\n")
	return rollingKey

def v3(initial,text):
	pages=text.split("<<PAGE>>_")
	i=1
	runningKey=initial
	for page in pages:
		runningKey=v2(runningKey,page)
		print(i,len(page),runningKey)
		i+=1
	
#print(v1("azby","RomeWasntBuiltInADay"))#6ZWM
#print(v1("azby","SomeWarnsBuiltInADay"))#6ZWM
#print(v2("azby","RomeWasntBuiltInADay"))#4PID
#print(v2("azby","SomeWarnsBuiltInADay"))#4GBX
#print(v2("B_1A","A_1B#2A"))
file="\n".join(open("input.txt").readlines());
v3("ANYTHING_NOT_SET_IN_METAL_CANNOT_BE_TRUSTED",file)
uniqueChar(file);
