h_cost = [12, 10, 16, 15, 12, 7, 11, 15, 11, 4, 1, 0] #heuristic for every node
goal_state = 12

def cost(u, k, h_cost, adj, opened, f_cost): #Function to calculate the f_cost for the node required
	i = 0
	for j in range(len(adj[u])):
		if adj[u][j][0]==k:
			i = j
			break

	u_gcost = f_cost[u-1] - h_cost[u-1]
	k_gcost = adj[u][i][1]
	g = u_gcost + k_gcost
	h = h_cost[k-1]
	f = g + h
	return f

def tracePath(c, opened, closed):
	path = [goal_state]
	return path

def display_f(opened, f_cost):
	l = []
	for i in range(len(opened)):
		l.append(f_cost[opened[i]-1])
	print('F_costs:', l)

def minimumNode(opened, f_cost): #Function to find the node with the minimum f_cost
	val = 10**7
	mini = 0

	for i in range(len(opened)):
		if val > f_cost[opened[i]-1]:
			val = f_cost[opened[i]-1]
			mini = opened[i]
		elif val == f_cost[opened[i]-1]:
			g1 = f_cost[opened[i]-1] - h_cost[opened[i]-1]
			g2 = f_cost[mini-1] - h_cost[mini-1]
			if g1 < g2:
				mini = opened[i]
			else:
				continue
	return mini
			
def A_star(s, adj):
	#Initialization
	opened = []
	f_cost = [10**7 for i in range(12)]
	closed = []
	flag = False
	f_cost[s-1] = h_cost[s-1]

	#Appending
	opened.append(s)
	print('Opened_A*: ', opened)
	display_f(opened, f_cost)
	print('Closed: ', closed)
	print()
	#while loop to check for adjacent nodes of s(current) node
	while opened!=[]:

		#finding the node with the minimum f_cost
		mini = minimumNode(opened, f_cost)
		u = mini
		if u in opened:
			opened.remove(u)
			closed.append(u) #add u to closed because now we will expand its children nodes
		
		#this loop is to check and append unvisited nodes in opened array that are successors of node 'u'
		for k in range(len(adj[u])):
			x = adj[u][k] 
			if x[0] not in closed and x[0] not in opened: 
				opened.append(x[0])	
				f_cost[x[0]-1] = cost(u, x[0], h_cost, adj, opened, f_cost) 

				if x[0]==goal_state:
					print('Goal state reached with cost: ', f_cost[goal_state-1])
					print('Opened_A*:', opened)
					display_f(opened, f_cost)
					print('Closed:', closed)
					path = tracePath(f_cost[goal_state-1], opened, closed)
					#print('Path:', path)
					print()
					print('No. of nodes in opened:', len(opened))
					print('No. of nodes in closed:', len(closed))
					#print('Depth: ', len(path))
					flag=True
					opened=[]
					break

		if flag:
			break
		print('Opened_A*:', opened)
		display_f(opened, f_cost)
		print('Closed:', closed)
		print()
			
#Adjacency List defintion
adj = {
	1: [[2, 2], [5, 1]],
	2: [[3, 1], [6, 3]],
	3: [[4, 2]],
	4: [[8, 1]],
	5: [[9, 1]],
	6: [[5, 5], [7, 1], [10, 4]],
	7: [[3, 3], [11, 10]], 
	8: [[7, 5], [12, 15]],
	9: [[10, 4]], 
	10: [[11, 3]], 
	11: [[12, 1]], 
	12: []
}
A_star(1, adj)
