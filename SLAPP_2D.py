import matplotlib.pyplot as plt
import numpy.random as npr

def checkRunningInIPython():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False
    
IPy=checkRunningInIPython()

# Create a named display, if in iPython
if IPy: myDisplay = display(None, display_id=True)

agList=[]
nAg=100
nCycles=10
dots=ax=fig=0 #to avoid an error of referencing without assignement


class AgBase():
    def __init__(self):
        self.breed=npr.randint(0,2)
        self.x=npr.random_sample()
        self.y=npr.random_sample()
    
    def move(self):
        self.x=npr.random_sample()
        self.y=npr.random_sample()
        
    def changeBreed(self):
        self.breed=npr.randint(0,2)
        
    def reportPos(self):
        return self.x, self.y
    
    def reportBreed(self):
        return self.breed

def updateData():
    global ax,IPy,dots
    xList0=[]
    yList0=[]
    xList1=[]
    yList1=[]
    
    for i in range(len(agList)):
        x,y=agList[i].reportPos()
        if agList[i].reportBreed() == 0:
            xList0.append(x)
            yList0.append(y)
        if agList[i].reportBreed() == 1:
            xList1.append(x)
            yList1.append(y)

    if IPy:
        dots[0].set_data(xList0, yList0)
        dots[1].set_data(xList1, yList1)
    else:
        ax.plot(xList0,yList0,'ro',xList1,yList1,'bo')
            
    
# simulation
def simulation(t):
    global agList, nAG
    if t==1:
        # create agents
        for i in range(nAg):
            a=AgBase()
            agList.append(a)
        
    for i in range(len(agList)):
            agList[i].move()
            agList[i].changeBreed()
    print("end cycle",t,"of the simulation")


def animation(t):
    global ax,fig,dots,IPy
    if t==1:
        # prepare graphic space
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        if IPy: dots = ax.plot([],[],'ro',[],[],'bo')
    
    
    if not IPy:
        plt.gca().cla()
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)

    updateData()
    if t==1: ax.set_title(str(t)+" initial frame")
    if t>1 and t<nCycles: ax.set_title(str(t))
    if t==nCycles: ax.set_title(str(t)+" final frame")
        
    if IPy: myDisplay.update(fig)
    else: fig.canvas.draw()

    plt.pause(0.3)
    print("end cycle",t,"of the animation")

for t in range(1,nCycles+1):
    simulation(t)
    animation(t)

    
if not IPy: input("Enter to finish")