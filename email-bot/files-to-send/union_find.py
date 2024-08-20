class UnionFind:
    def __init__(self, size : int) -> None:
        self.sets = size
        self.ppt = []
        self.sizes = []
        self.rank = []

        for i in range(self.sets):
            self.ppt.append(i)
            self.sizes.append(1)
            self.rank.append(0)
    
    def find(self, start : int) -> int:
        if self.ppt[start] != start:
            return self.find(self.ppt[start])
        
        return self.ppt[start]
    
    def merge(self, a : int, b : int) -> None:
        rt1 = self.find(a)
        rt2 = self.find(b)

        if rt1 == rt2:
            return
        
        if self.sizes[a] < self.sizes[b]:
            a, b = b, a
        
        elif self.sizes[a] == self.sizes[b]:
            if self.rank[a] < self.rank[b]:
                a, b = b, a
            
            elif self.rank[a] == self.rank[b]:
                if a < b:
                    a, b = b, a
        
        self.ppt[b] = a
        self.sizes[a] += self.sizes[b]
        self.rank[a] += 1
        self.sets -= 1
    
    def rank_set(self, set : int) -> int:
        return self.rank[set]
    
    def size_set(self, set : int) -> int:
        return self.sets[set]
    
    def numb_sets(self) -> int:
        return self.sets