# O(N)
# O(N)
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for d in path:
            if d:
                if d=='.':
                    continue
                elif d == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(d)
        return '/'+'/'.join(stack)