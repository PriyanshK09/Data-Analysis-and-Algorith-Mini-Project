from collections import defaultdict, deque
class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.inters = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance,inter):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance
        self.inters[(from_node, to_node)] = inter


def dijkstra(graph, initial):
    vis = {initial: 0}
    path = {}

    nodes = set(graph.nodes)
    while nodes:
        m_nde = None
        for node in nodes:
            if node in vis:
                if m_nde is None:
                    m_nde = node
                elif vis[node] < vis[m_nde]:
                    m_nde = node
        if m_nde is None:
            break

        nodes.remove(m_nde)
        cur_wgt = vis[m_nde]

        for edge in graph.edges[m_nde]:
            try:
                weight = cur_wgt + graph.distances[(m_nde, edge)]
            except:
                continue
            if edge not in vis or weight < vis[edge]:
                vis[edge] = weight
                
                path[edge] = m_nde
                
    
    return vis, path


def short_pth(graph, vis,paths,origin, destination):
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return vis[destination], list(full_path)

def minflw_inter(graph,path):
    c = []
    min_inter = 0
    max_inter = 0
    for i in range(1,len(path)):
        c.append(graph.distances[(path[i-1],path[i])])
        min_inter = min_inter+g.inters[(path[i-1],path[i])][0]
        max_inter = max_inter+g.inters[(path[i-1],path[i])][1]
    return min(c),[min_inter,max_inter]

def update_graph(g,min_flow,path):
    for i in range(1,len(path)):
        dist = g.distances[(path[i-1],path[i])] - min_flow
        if(dist == 0):
            g.edges[path[i-1]].remove(path[i])
            g.distances.pop((path[i-1],path[i]),None)
            g.inters.pop((path[i-1],path[i]),None)
        else:
            g.distances[(path[i-1],path[i])] = dist
            g.add_edge(path[i],path[i-1],min_flow,g.inters[(path[i-1],path[i])])
            
if __name__ == '__main__':
    graph = Graph()

    g = Graph()
    task = {}
    g.add_node('s')
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')
    g.add_node('e')
    g.add_node('f')
    g.add_edge('s', 'a', 5, [3, 5])
    g.add_edge('s', 'b', 5, [2, 4])
    g.add_edge('s', 'c', 5, [2, 4])
    g.add_edge('a', 'e', 3, [2, 4])
    g.add_edge('b', 'c', 3, [1, 3])
    g.add_edge('b', 'f', 7, [3, 5])
    g.add_edge('b', 'e', 3, [2, 4])
    g.add_edge('c', 'f', 5, [2, 4])
    g.add_edge('e', 'd', 8, [0, 2])
    g.add_edge('f', 'e', 1, [1, 3])
    g.add_edge('f', 'd', 7, [1, 3])

    task.update({'t1': [5, 6]})
    task.update({'t2': [2, 24]})
    task.update({'t3': [6, 10]})
    
    v,p=dijkstra(g,'s')
    paths = {}
    count=1
    while p:
        if 'd' in p:
            c,path = short_pth(graph,v,p,'s', 'd')
            min_flow,inter = minflw_inter(g,path)
            uncert = 0
            paths.update({count:[path,min_flow,inter,min_flow,uncert]})
            print("paths ", paths)
            update_graph(g,min_flow,path)
            count+=1
            v,p=dijkstra(g,'s')
        else:
            break
    else:
        print("no more paths")

    print("\n The paths and their max flow : ")
    for i in range(1,len(paths)+1):
        print("\n ",i,"\t",paths[i][0], "\t -> min flow : ",paths[i][1],"\t inter : ",paths[i][2])
    
    temp = sorted(task.items(), key=lambda e: e[1][1])
    sort = []
    for key, value in temp:
       sort.append(key)

    tempPath = paths
    ip = 1
    unallocatedTask = []
     
    
    for i in range(0,len(sort)):
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("For task : %d." % (i+1))
        tkfl = task.get(sort[i])[0]
        print("Task flow is :",tkfl)
        stopFlag = 0
        while int(tkfl) > 0 :
            
            
            deadline = task.get(sort[i])[1]
            print("paths => ", paths)
            inter = paths[ip][2]
            if int(deadline) < int(inter[0]) or int(deadline) > int(inter[1]):
                ip = ip + 1
                if i >= len(sort) or ip >= len(paths):
                    print("Task : ", (i+1) , "cannot be allocated in the remaining paths.")
                    ip = 1
                    unallocatedTask.append(sort[i])
                    break
                continue
            
            print("Allocating in the path : ", ip , paths[ip])
            tkfl = int(tkfl)
            
            if tkfl >= paths[ip][3]:
                tkfl = tkfl - paths[ip][3]
                paths[ip][3] = 0
                print("Updating in the path : ", ip , paths[ip])
                if(tkfl <0):
                    tkfl = 0
                ip=ip+1
                if ip > len(paths):
                    stopFlag = 1
                    break
            else:
                print("in else")
                paths[ip][3] = abs(tkfl-paths[ip][3])
                print("updating in the path : ", ip , paths[ip])
                tkfl = 0
            
        if stopFlag == 1:
            print("No more paths to allocate")
            break
    print("Unallocated tasks are ; ",unallocatedTask)
    print("Paths status ",paths)
    
    
    for i in range(0,len(unallocatedTask)):
        ab=0
        uncert = []
        for j in range(1,len(paths)+1):
            inter = paths[j][2]
            tdline = task.get(unallocatedTask[i])[1]
            flow = paths[j][1]
            bl=int(tdline)
            br=bl
            al=int(inter[0])
            ar=int(inter[1])
            ra = int((ar - al)/2)
            rb = int((br - bl)/2)
            if ar < bl:
                ab = 1
            elif ((al<=bl) & (bl<=ar) & (ar<br)):
                ab = -1
            elif ((ra == rb) & (al == bl)):
                ab = 0.5
            elif ((bl<=al) & (al<ar) & (ar<=br) & (rb > ra)):
                ab= (br - ar)/(2*(rb - ra))
            eij = flow * (br - ar) * ab
            print("Uncertainty")
            print(eij)
            paths[j][4] = eij
            uncert.append(eij)
        print("For the task ",unallocatedTask[i])
        
        uncert.sort() 
        print("\nPaths with their corresponding uncertainty value : " , paths)
        print("Sorted uncertainty values : " , uncert)
        pat=[]
        for it in range(0,len(uncert)):
            for jt in range(1,len(paths)+1):
                if(uncert[it] == paths[jt][4]):
                    pat.append(jt)
                    break
                
        tkfl = task.get(unallocatedTask[i])[0]
        ip = 0
        while int(tkfl) > 0:
            if tkfl >= paths[pat[ip]][3]:
                tkfl = tkfl - paths[pat[ip]][3]
                paths[pat[ip]][3] = 0
                print("updating in the path : ", ip , paths[pat[ip]])
                if(tkfl < 0):
                    tkfl = 0
                ip=ip+1
                if ip > len(paths):
                    stopFlag = 1
                    break
            else:
                print("in else")
                paths[pat[ip]][3] = abs(tkfl-paths[pat[ip]][3])
                print("updating in the path : ", ip , paths[pat[ip]])
                tkfl = 0   
        if( stopFlag == 1 and tkfl > 0):
            print("Task cannot be completely allocated")
            print("Remaining flow in the network is ",tkfl)
        else:
            print("Task allocated")
