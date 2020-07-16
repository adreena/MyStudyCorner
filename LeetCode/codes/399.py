# time: O(k(V+E)) k number of queries and V+E BFS
# space: O(V+E) size of graph

from collections import defaultdict

def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    graph = defaultdict(lambda:[])
    for eq, val in zip(equations, values):
        graph[eq[0]].append([eq[1], val])
        graph[eq[1]].append([eq[0], 1./val])
    answers = []
    for query in queries:
        if query[0] not in graph or query[1] not in graph:
            answers.append(-1.0)
        else:
            q = [(query[0],1.)]
            visited = set()
            found = False
            while q:
                cur, val = q.pop(0)
                if cur == query[1]:
                    answers.append(val)
                    found = True
                    break
                for nxt, nxt_val in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append([nxt, val*nxt_val])

            if not found:
                answers.append(-1.0)
    return answers
