from queue import PriorityQueue

class Graph_Path:
	def __init__(self, triang):
		self.x = triang.x
		self.y = triang.y
		self.triangles = triang.triangles
		self.neighbors = triang.neighbors
		
	def center_of_gravity(self, i):
		t=self.triangles[i]
		x=(self.x[t[0]]+self.x[t[1]]+self.x[t[2]])/3
		y=(self.y[t[0]]+self.y[t[1]]+self.y[t[2]])/3
		return x,y
		
	cg = center_of_gravity
	
	def center_of_gravity_3(self, i):
		t=self.triangles[i]
		x=self.x[t[0]]+self.x[t[1]]+self.x[t[2]]
		y=self.y[t[0]]+self.y[t[1]]+self.y[t[2]]
		return x,y
		
	cg3 = center_of_gravity_3
	
	def cost(self, i, j):
		cg1=self.cg(i)
		cg2=self.cg(j)
		dcgx = cg1[0]-cg2[0]
		dcgy = cg1[1]-cg2[1]
		return (dcgx**2 + dcgy**2)**(0.5)
		
	def cost_3(self, i, j):
		cg1=self.cg3(i)
		cg2=self.cg3(j)
		dcgx = cg1[0]-cg2[0]
		dcgy = cg1[1]-cg2[1]
		return (dcgx**2 + dcgy**2)**(0.5)
		
heuristic = Graph_Path.cost

def a_star_search_G(triang, start, goal):
	frontier = PriorityQueue()
	frontier.put((0,start))
	graph = Graph_Path(triang)
	came_from={}
	cost_so_far={}
	came_from[start]=None
	cost_so_far[start]=0
	trigo = triang.triangles[goal]
	print(trigo)
	# goal_cg3 = (graph.x[trigo[0]]+graph.x[trigo[1]]+graph.x[trigo[2]],graph.y[trigo[0]]+graph.y[trigo[1]]+graph.y[trigo[2]])
	goal_cg3 = graph.cg3(goal)
	def heuristic(i):
		cg1=graph.cg3(i)
		dcgx = cg1[0]-goal_cg3[0]
		dcgy = cg1[1]-goal_cg3[1]
		return (dcgx**2 + dcgy**2)**(0.5)
	
	while not frontier.empty():
		current= frontier.get()[1]
			
		if current==goal:
			break
			
		# print(graph.neighbors[current])
		for next in graph.neighbors[current]:
			if came_from[current]==next or next == -1:
				continue
			# print(next)
			new_cost = cost_so_far[current] + graph.cost_3(current,next)
			# print(new_cost)
			if next not in cost_so_far or new_cost< cost_so_far[next]:
				cost_so_far[next]=new_cost
				#Change heuristic
				priority = new_cost + heuristic(next)
				# print("priority ", priority )
				frontier.put((priority, next))
				came_from[next] = current
				
	return came_from, cost_so_far