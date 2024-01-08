#The missionary -cannibal problem
bank1 = ['c', 'c', 'c', 'm', 'm', 'm']
boat = []
bank2 = []
n = len(bank1)
side = 1

def Checker(boat, bank1, bank2):
    countm1 = boat.count('m')+bank1.count('m')
    countc1 = boat.count('c')+bank1.count('c')
    countm2 = boat.count('m')+bank2.count('m')
    countc2 = boat.count('c')+bank2.count('c')
    
    if side==1 and countm1<countc1 and countm1!=0:
        return 1
    elif side==2 and countm2<countc2 and countm2!=0:
        return 1
    else:
        return 0
        
def display(boat, bank1, bank2):
    print('Boat: ', boat)
    print('Bank 1:', bank1)
    print('Bank 2:', bank2)

while(bank1!=[] and len(bank2)!=6):
    print('------------------------------------------------------------\n')
    if Checker(boat, bank1, bank2)==1:
        print('Move not possible. The missionaries have been outnumbered. You lose. Try again')
        break
        
    else:
        if side == 1:
            display(boat, bank1, bank2)
            print('We are at bank 1')
            s = input('Enter the combination you wish to put on the boat. We are leaving bank 1\n')
            boat = list(s)
            
            print('Boat is leaving bank 1')
            for i in range(len(boat)):
                bank1.remove(boat[i])
            display(boat, bank1, bank2)
            
            for i in range(len(boat)):
                bank2.append(boat[i])
            boat = []
            
            if Checker(boat, bank1, bank2)==1:
                print('Move not possible. The missionaries have been outnumbered. You lose. Try again')
                break
            print('We are at bank 2')
            display(boat, bank1, bank2)
            side = 2
                
        elif side==2:
            s = input('Enter the combination you wish to put on the boat. We are leaving bank 2\n')
            boat = list(s)
            
            for i in range(len(boat)):
                bank2.remove(boat[i])
            display(boat, bank1, bank2)
            
            n_boat = len(boat)
            for i in range(n_boat):
                bank1.append(boat[i])
            boat = []
            display(boat, bank1, bank2)
            print('Boat is leaving')
            side = 1
            
if len(bank2)==6:
    print('Congratulations! You win!')