#Python program to implement IDA*

#Setting some global variables to save their values from memory loss due to recursion
F_NEW = 10**7
FLAG = False
PATH = []

#Function to find the f_cost for current iteration
def F_cost(u, s, adj, f_cost, nodes): 
    i = nodes.index(s) #index of s in f_cost
    y = 0 #index of u node along with its path cost in the adjacency list

    for x in range(len(adj[s][1])):
        if adj[s][1][x][0]==u:
            y = x
            break

    s_gcost = f_cost[i] - adj[s][0] #Calculating g_cost for s node
    g = s_gcost + adj[s][1][y][1] #Adding g(s) + g(u)
    h = adj[u][0] #heuristic cost of node u
    f = g + h
    return f

#Function to ensure that the IDA* algorithm starts from the start node again in the new iteration after backtracking 
def backtrack(s, adj, f_cost, nodes, path, f_values): #Only to set the f_cost of start node
    global F_NEW
    F_NEW = 10**7

    global FLAG

    global PATH

    l = IDA_star(s, '', adj, f_values[0], f_values[1], f_cost, nodes, path)
    print('f_bound, f_new:', l[3], l[4])
    
    if FLAG:
        print('\n------------------------------------------------------------------------------------------------')
        print('Final path: ', PATH)
        print('Cost to reach goal state: ', f_cost[7])
        print('Goal state reached. End of program.')
    else:
        backtrack(s, adj, f_cost, nodes, [], [l[4], 10**7])


#IDA* function - Add every new node to opened before checking condition of f_bound, set f_new before checking f_bound
def IDA_star(s, u, adj, f_bound, f_new, f_cost, nodes, path):
    global F_NEW

    global FLAG

    global PATH
    #Updating the costs and limits of the current node and current iteration
    if s!='S':
        f = F_cost(s, u, adj, f_cost, nodes)
    else:
        #Start of new iteration
        print('-------------------------------------------------New Iteration---------------------------------------------')
        f = f_cost[0]

    #Base condition
    if f > f_bound:
        #Calculating f_new
        f_new = min(f, f_new)
        F_NEW = min(F_NEW, f_new)

        #Initial print statements
        print('Current node: ', s)
        print('F-limit: ', f_bound, '\tF-new: ', F_NEW)
        print('Path:', path)
        print()

        #Backtracking because base condition wasn't satisfied
        l = [s, '', adj, f_bound, F_NEW, f_cost, nodes, path]
        return l
    
    #if f_cost is within f_bound, then expand children
    else: 
        #Adding the node to the path
        path.append(s)

        #Initial print statements
        print('Current node: ', s)
        print('F-limit: ', f_bound, '\tF-new: ', F_NEW)
        print('Path:', path)
        print()

        #Setting f_cost for the current node
        i = nodes.index(s)
        f_cost[i] = f

        #Checking if goal state reached while staying within f_bound
        if s=='G':    
            FLAG = True
            PATH = path.copy()
            l = [s, 'G', adj, f_bound, F_NEW, f_cost, nodes, path]
            return l
        
        #In case goal state is not found while keeping within f_bound
        else:
            #To look for children of current node
            for k in range(len(adj[s][1])):

                #Updating f_new 
                if f!=f_bound and f>f_bound:
                    f_new = min(f, f_new)
                    F_NEW = min(F_NEW, f_new)
                else:
                    f_new = f_new

                #Calling the next child of the current node recursively
                l = IDA_star(adj[s][1][k][0], s, adj, f_bound, F_NEW, f_cost, nodes, path)

                #Since we backtracked, the child we just explored will not be in the path, hence we pop it out of the path
                if adj[s][1][k][0] in path:
                    path.pop(-1)
                
                #To backtrack to print the final statements since goal state has been found
                if FLAG:
                    l = [s, 'G', adj, f_bound, F_NEW, f_cost, nodes, path]
                    return l

            #To avoid NoneType error and to maintain values of variables in the recursion stack for now
            l = [adj[s][1][k][0], s, adj, l[3], l[4], f_cost, nodes, path]
            return  l


#Initialization of the graph and other variables
adj = {
    'S': [6, [['A', 2], ['B', 3]]],
    'A': [4, [['C', 3]]],
    'B': [4, [['C', 1], ['D', 3]]],
    'C': [4, [['D', 1], ['E', 3]]],
    'D': [3.5, [['F', 2]]],
    'E': [1, [['G', 2]]],
    'F': [1, [['G', 1]]],
    'G': [0]
}
nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
f_cost = [10**7 for i in range(8)]
s = input('Enter the start node\n').upper()
f_cost[0] = adj[s][0]
path = []
f_values = [0, 10**7] #[<f_bound>, <f_new>]
backtrack(s, adj, f_cost, nodes, path, f_values)

'''
For loop for all the adjacent nodes
Recursive function call with start node and end node


If s is 'S', then new iteration starts.. Print current node, f-new, f-bound
If s == 'S', set f-bound = f-new
Calculate f for node s
Check if f > f-bound, if so, return
Else, expand children of s

'''