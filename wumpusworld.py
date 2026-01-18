class cellState:
    def __init__(self,loc,isWumpus=False,isPit=False,isStench=False,isBreeze=False,isGold=False,forward=None,left=None,right=None,back=None):
        self.L=loc
        self.W=isWumpus
        self.S=isStench
        self.P=isPit
        self.B=isBreeze  
        self.G=isGold
        self.forward=forward
        self.left=left
        self.right=right
        self.back=back        
def setBoard():
    board=cellState([0,0])
    PitsLoc=[]
    WumpusLoc=[]
    inp=int(input("Enter the number of sides for the board"))
    numberofPits=int(input("Enter number of pits"))
    WumpusLoc=[int(input("Enter location of Wumpus"))]
    for idx in range(numberofPits):
        loc=int(input("Enter location of Pit",idx+1,sep=''))
        Pits+=[loc]
    for i in range(inp):
        for j in range(inp):
            currnode=cellState([i,j])
    for col in range(inp):
        for row in range(inp):
            currnode=cellState([row,col])
            if row!=inp-1:
                currnode.forward=cellState([row+1,col])
            if row!=0:
                currnode.back=cellState([row-1,col])
            if col!=inp-1:
                currnode.left=cellState([row,col+1])
            if col!=0:
                currnode.right=cellState([row,col-1])
            if 10*(row+1)+col+1 in PitsLoc:
                currnode.P=True
                try:
                    currnode.forward.B=True
                    currnode.back.B=True
                    currnode.left.B=True
                    currnode.right.B=True
                except:
                    pass
            if 10*(row+1)+col+1==WumpusLoc[0]:
                currnode.W=True
                try:
                    currnode.forward.S=True
                    currnode.back.S=True
                    currnode.left.S=True
                    currnode.right.S=True
                except:
                    pass
setBoard()

            
