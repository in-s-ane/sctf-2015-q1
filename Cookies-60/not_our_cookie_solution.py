def gendp(x):
	values = {} #it maps the ordered pair (numpieces, prevmove) to 0 (you win if you start the turn on this condition)
		        #and 1 (you win the game if you start the turn on this condition)
	for i in range(0,x+1):
		values[(0,i)]=0 #if you have 0 pieces and its your turn, you autolose
	for i in range(1,50): #m range appears to be 2 through 49
						#so, this is an impartial game (it doesnt matter whose turn it is, you can make the same moves)
						#Say you're in state A. If you can get to a losing state (value of 0) in one move, you'll make that move. That 
						#forces the other player to lose. So if you can get to a losing state, A -> 1, and becomes a winning move
						#If, however, you can't ever get to a losing state in one move, that means no matter what you do, the other 
						#player is going to win. So A -> 0
		for j in range(0,x+1): # your prevmove is always in the range 0-k (0 implies starting position)
			#so i = current pilesize
			#j=prevmove
			win=0
			for k in range(1,x+1):
				if(k==j or k>i):
					#you can't make a move here!
					continue
				else:
					if values[(i-k,k)]==0:
						win=1
			values[(i,j)]=win
	return values


f=open('cookies.txt','r')
f.readline()
count=0
cases=[]
for line in f:
	t=line.split()
	cases.append((int(t[1]),int(t[0])))
cases=sorted((cases))
k=0
values = {}
count=0
times=0
for x in cases:
	times+=1
	if x[0]!=k:
		values=gendp(x[0])
		if(x[0]==3):
			print (values)
		k=x[0]
	if(values[x[1],0]==0):
		print (str(x[1])+" "+str(x[0]))
	count+=values[(x[1],0)]
print(count)