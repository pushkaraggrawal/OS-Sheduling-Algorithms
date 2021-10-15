
U = 60

class Process:
    def __init__(self,basePriority,groupID):
        self.base=basePriority
        self.groupID=groupID
        self.priority=basePriority
        self.CPU=0
        self.GCPU=0
        
weights=[0.5,0.5]
   
def floor(n):
    return n-n%1

def chooseProcess(processes):
    m = processes[0].priority
    x=processes[0]
    for p in processes:
        if (p.priority<m) :
           m = p.priority 
           x=p
    return x

def execute(processes):
    exe = chooseProcess(processes)
    groupexe=exe.groupID
    for p in processes:   
        if(p.groupID==groupexe):            
            p.GCPU=floor(p.GCPU/2)+floor(U/2)
        else:            
            p.GCPU=floor(p.GCPU/2)    
    for p in processes:
        p.CPU = floor(p.CPU/2)
    exe.CPU+=floor(U/2)
    for p in processes:
        p.priority = p.base+floor(p.CPU/2) + floor(p.GCPU/(4*weights[p.groupID]))
    i=0
    for p in processes:
        print(f"Process--No:{i+1}--Priority:{p.priority}--CPU:{p.CPU}--GCPU{p.GCPU}\n")
        
        i+=1
    print("************************************************************")
        
        
if __name__ == "__main__":
    processes = []
    processes.append(Process(60,0))
    processes.append(Process(60,1))
    processes.append(Process(60,1))
    
    
    for i in range(5):
        execute(processes)