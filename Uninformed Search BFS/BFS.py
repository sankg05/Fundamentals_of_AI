#Python program to implement BFS

def BFS(adj, s):

	i_count = 0
	v_count = 0

	flag = False
	visited = []
	inqueue = []
	depth = [0 for i in range(12)]
	
	inqueue.append(s)
	depth[int(s)]=0
	
	while inqueue!=[]:
		d = inqueue[0]
		inqueue.remove(d)
		visited.append(d)
		v_count += 1
		
		for i in adj[int(d)-1]:
			
			if i not in visited and i not in inqueue:
				inqueue.append(i)
				i_count += 1
				
				depth[int(i)-1] = depth[int(d)-1] + 1
				
				
				if i==goal_state:	
					print(i, goal_state)
					print('Inqueue:', inqueue, 'Visited:', visited)
					print('Goal state has been found: ', goal_state)
					inqueue = []
					flag = True
					break
					
		if flag:
			break
		print('Inqueue:', inqueue, 'Visited:', visited)
	print('Depth of all nodes:', depth)
	print('Depth of goal state:', depth[int(goal_state)-1])
	print('No. of nodes in open queue', i_count)
	print('No. of nodes in visited queue', v_count)

adj = [['2', '5'], ['3', '6'], ['4'], ['8'], ['9'], ['5', '7', '10'], ['3', '11'], ['7', '12'], ['10'], ['11'], ['12'], []]
s = input('Enter the source vertex\n')
goal_state = input('Enter the goal_state\n')
BFS(adj, s)
