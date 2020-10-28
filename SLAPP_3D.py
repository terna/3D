import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import numpy.random as npr
import numpy as np

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
        self.z=npr.random_sample()

    
    def move(self):
        self.x=npr.random_sample()
        self.y=npr.random_sample()
        self.z=npr.random_sample()
        
    def changeBreed(self):
        self.breed=npr.randint(0,2)
        
    def reportPos(self):
        return self.x, self.y, self.z
    
    def reportBreed(self):
        return self.breed

def updateData():
    global ax,IPy,dots
    
    b0=b1=0
    for i in range(len(agList)):
        if agList[i].reportBreed() == 0: b0+=1
        if agList[i].reportBreed() == 1: b1+=1

    #with matplotlib 3.3.2 set_3d_properties requires vectors with shape so we need to use 
    # the numpy arrasy structure
    xList0=np.array([0.0]*b0)
    yList0=np.array([0.0]*b0)
    zList0=np.array([0.0]*b0)
    xList1=np.array([0.0]*b1)
    yList1=np.array([0.0]*b1)
    zList1=np.array([0.0]*b1)
    
    i0=i1=-1
    for i in range(len(agList)):
        x,y,z=agList[i].reportPos()
        if agList[i].reportBreed() == 0:
            i0+=1
            xList0[i0]=x
            yList0[i0]=y
            zList0[i0]=z
        if agList[i].reportBreed() == 1:
            i1+=1
            xList1[i1]=x
            yList1[i1]=y
            zList1[i1]=z
                        
    if IPy:
        dots[0].set_data(xList0, yList0)
        dots[0].set_3d_properties(zList0)
        dots[1].set_data(xList1, yList1)
        dots[1].set_3d_properties(zList1)

    else:
        ax.plot3D(xList0,yList0,zList0,'ro')
        ax.plot3D(xList1,yList1,zList1,'bo')        
            
    
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
        fig = plt.figure(figsize=(7,7))
        ax = p3.Axes3D(fig)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_zlim(0, 1)
        if IPy: dots = ax.plot3D([],[],'ro',[],[],'bo')
    
    if not IPy:
        plt.gca().cla()
        ax.set_xlim(0,1)
        ax.set_ylim(0,1)
        ax.set_zlim(0,1)

    updateData()
    
    if IPy:
        if t==1: ax.set_title(str(t)+" initial frame",loc='left')
        if t>1 and t<nCycles: ax.set_title(str(t),loc='left')
        if t==nCycles: ax.set_title(str(t)+" final frame",loc='left')
    else:
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