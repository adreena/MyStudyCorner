# ---------------------------------
# DFS
# time: O(N * 2^N) 
#.  - DFS solves in V+E time but when copying path to paths we lose another V+E time so if V+E is N, O(N)
#.  - and as for backtracking on all V is 2^V we either choose the path or not so O(2^V)
# space: O(N*2^N) recursion of n consecutive calls for 2^N 
# ---------------------------------
def DFS_find_all_paths(a, b, path):
    visited[a] = True
    path.append(a)
    if a == b:
        paths.append(list(path)) # N time step to append 
    else:
        for c in graph[a]:
            if not visited[c]:
                DFS_find_all_paths(c,b,path)

    path.pop()
    visited[a] = False
    
graph = defaultdict(lambds:[]) # build the graph
visited = {} # dict of nodes
paths = []
DFS_find_all_paths(a, b, [])

# ---------------------------------
# BFS
# time: O(N*2^N) N: paths
# space: O(N*2^N) keeping all paths
# ---------------------------------
def BFS_find_all_paths(a, b, graph):
    paths = []
    path = [a]
    visited = set()
    q = [path]
    while len(q)>0:
        path = q.pop(0)
        if path[-1]==b:
            paths.append(path)
        else:
            for c in graph[paht[-1]]:
                if c not in visited:
                    q.append(path+[c])
                    visited.add(c)
    return paths
                   
    
    
    
    
    
    
    
    