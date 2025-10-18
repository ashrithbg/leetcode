class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        components = n
        size = [1]*n
        parent = [i for i in range(n)]
        def find(x):
            while x!=parent[x]:
                x=parent[x]
            return x

        for t,u,v in logs:
            rootu = find(u)
            rootv = find(v)
            if rootu!=rootv:
                if size[rootu]<size[rootv]:
                    parent[rootu] = rootv
                    size[rootv]+=size[rootu]
                else:
                    parent[rootv] = rootu
                    size[rootu]+=size[rootv]
                components-=1
                if components == 1:
                    return t
        return -1
