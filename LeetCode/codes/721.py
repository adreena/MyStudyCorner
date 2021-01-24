# time O(V+E)
#space O(V+E)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph= defaultdict(lambda:set())
        owner = defaultdict(lambda:None)
        for account in accounts:
            o = account[0]
            for email1 in account[1:]:
                owner[email1]=o
                for email2 in account[1:]:
                    if email1!=email2:
                        graph[email1].add(email2)
                        graph[email2].add(email1)
        
        output = []
        visited = set()
        for e, o in owner.items():
            if e not in visited:
                q = [e]
                emails = [e]
                while q:
                    top = q.pop(0)
                    visited.add(top)
                    for nxt in graph[top]:
                        if nxt not in visited:
                            q.append(nxt)
                            visited.add(nxt)
                            emails.append(nxt)

                
                emails.sort()
                output.append([o]+emails)
        return output