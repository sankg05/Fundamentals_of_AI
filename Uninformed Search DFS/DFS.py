#Code to implement the Water jug problem using DFS
def DFS(s, opened, closed, goal_state, a, b, paths):
    if s in closed:
        return
    elif s==goal_state:
        print('Reached goal state: ', s)
        return
    else:
        print()
        print('Current node: ', s)
        print()
        closed.append(s)
        if s in opened:
            opened.remove(s)
            
        print('Closed: ', closed)
        
        if s[0]==0 and s[1]==0:
            if [4, s[1]] not in closed and [4, s[1]] not in opened:
                opened.append([4, s[1]])
            if [s[0], 3] not in closed and [s[0], 3] not in opened:
                opened.append([s[0], 3])
            
            print('Opened: ', opened)
            DFS([4, s[1]], opened, closed, goal_state, a, b, paths)
            DFS([s[0], 3], opened, closed, goal_state, a, b, paths)
        elif s[0]==0 or s[1]==0:
            if s[0]==0:	#[0,3]
                if [a, s[1]] not in closed and [a, s[1]] not in opened:
                    opened.append([a, s[1]])
                if [0, 0] not in closed and [0, 0] not in opened:
                    opened.append([0, 0])
                if [s[1], 0] not in closed and [s[1], 0] not in opened:
                    opened.append([s[1], 0])
                
                print('Opened: ', opened)
                DFS([a, s[1]], opened, closed, goal_state, a, b, paths)
                DFS([0, 0], opened, closed, goal_state, a, b, paths)
                DFS([s[1], 0], opened, closed, goal_state, a, b, paths)
                
            elif s[1]==0:	#[4,0]
                if [0, 0] not in closed and [0, 0] not in opened:
                    opened.append([0, 0])
                if [s[0], b] not in closed and [s[0], b] not in opened:
                    opened.append([s[0], b])
            
                if s[0]>b:	#[4, 0]-> [1, 3]
                    if [s[0]-b, b] not in closed and [s[0]-b, b] not in opened:
                        opened.append([s[0]-b, b])
                    
                    print('Opened: ', opened)
                    DFS([0, 0], opened, closed, goal_state, a, b, paths)
                    DFS([s[0], b], opened, closed, goal_state, a, b, paths)
                    DFS([s[0]-b, b], opened, closed, goal_state, a, b, paths)
                    
                    
                else:	#[1, 0]->[0, 1]
                    if [0, s[0]] not in closed and [0, s[0]] not in opened:
                        opened.append([0, s[0]])
                        
                    print('Opened: ', opened)
                    DFS([0, 0], opened, closed, goal_state, a, b, paths)
                    DFS([s[0], b], opened, closed, goal_state, a, b, paths)
                    DFS([0, s[0]], opened, closed, goal_state, a, b, paths)
        else:
            if [0, s[1]] not in closed and [0, s[1]] not in opened:
                opened.append([0, s[1]])
            if [s[0], 0] not in closed and [s[0], 0] not in opened:
                opened.append([s[0], 0])
            
            x = min(s[0], b-s[1])
            y = min(a-s[0], s[1])

            if [s[0]-x, s[1]+x] not in closed and [s[0]-x, s[1]+x] not in opened:
                opened.append([s[0]-x, s[1]+x])
            if [a-s[0], s[1]] not in closed and [a-s[0], s[1]] not in opened:
                opened.append([a-s[0], s[1]])
            
            print('Opened: ', opened)
            DFS([0, s[1]], opened, closed, goal_state, a, b, paths)
            DFS([s[0], 0], opened, closed, goal_state, a, b, paths)
            DFS([s[0]-x, s[1]+x], opened, closed, goal_state, a, b, paths)
            DFS([s[0]+y, s[1]-y], opened, closed, goal_state, a, b, paths)


s = [0, 0]
opened = []
closed = []
goal_state = [2, 0]
paths = {}
a, b = 4, 3
DFS(s, opened, closed, goal_state, a, b, paths)
