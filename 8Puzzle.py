
def printState(State):
    for i in State:
         print(i)


def changeValRight(State):
    x=0
    y=0
    while x<3:
        while y<3:#tirar esses whiles aqui e passar endereço do role
                  # to precisando economizar os espaços
            if (State[x][y]==0): 
                aux =State[x][y+1]
                State[x][y]=aux
                State[x][y+1]=0
                return 
            y=y+1
        y=0
        x=x+1
            

def changeValLeft(State):
    x=0
    y=0
    while x<3:
        while y<3:
            if (State[x][y] == 0) :
                aux =State[x][y-1]
                State[x][y]=aux
                State[x][y-1]=0
                return
            y=y+1
        y=0
        x=x+1
            

def changeValUp(State):
    x=0
    y=0
    while x<3:
        while y<3:
            if (State[x][y]==0):

                aux =State[x-1][y]
                State[x][y]=aux
                State[x-1][y]=0
                return
            y=y+1
        y=0    
        x=x+1
            

def changeValDown(State):
    
    x=0
    y=0
    while x<3:
        while y<3:
            if (State[x][y]==0):
                aux =State[x+1][y]
                State[x][y]=aux
                State[x+1][y]=0
                return
            y=y+1
        y=0
        x=x+1


def createState(initialState):
    matxOriginal=initialState
    x=0
    y=0
    while x <3:
        while y<3:
            if(initialState[0][0] == 0) :
                changeValRight(initialState)
                printState(initialState)
                changeValLeft(initialState)
                print('\t')
                changeValDown(initialState)
                printState(initialState)

                return
            elif(initialState[0][1] == 0) :
                changeValRight(initialState)
                print('\t')
                changeValDown(initialState)
                print('\t')
                changeValLeft(initialState)
                return
            
            elif(initialState[0][2]==0):
                changeValLeft(initialState)
                print('\t')
                changeValDown(initialState)
                return

            elif(initialState[1][0]==0):
                changeValUp(initialState)
                print('\t')
                changeValRight(initialState)
                print('\t')
                changeValDown(initialState)
                return

            elif(initialState[1][1]==0):
                changeValUp(initialState)
                print('\t')
                changeValRight(initialState)
                print('\t')
                changeValDown(initialState)
                print('\t')
                changeValLeft(initialState)
                return

            elif(initialState[1][2]==0):
                changeValUp(initialState)
                print('\t')
                changeValDown(initialState)
                print('\t')
                changeValLeft(initialState)
                return

            elif(initialState[2][0]==0):
                changeValUp(initialState)
                print('\t')
                changeValRight(initialState)
                return

            elif(initialState[2][1]==0):

                changeValUp(initialState)
                printState(initialState)
                changeValDown(initialState)

                changeValRight(initialState)
                printState(initialState)
            
                changeValLeft(initialState)
                printState(initialState)
                return

            elif(initialState[2][2]==0):
            
                changeValUp(initialState)
                printState(initialState)
                changeValDown(initialState)
                print('\t')
                changeValLeft(initialState)
                printState(initialState)
                changeValRight(initialState)
                return
            y=y+1
        y=0
        x=x+1
    


matx=[[1,2,3],[4,7,8],[5,6,0]]
printState(matx)
print('\t')
createState(matx)
                
                


            