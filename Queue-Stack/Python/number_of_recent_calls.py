class RecentCounter:

    def __init__(self):
        self.maxx = []
        

    def ping(self, t: int) -> int:
        curmin, curmax = t-3000, t
        if not self.maxx:
            self.maxx.append(curmax)
            return 1
        self.maxx.append(curmax)
        while curmin > self.maxx[0]:
            self.maxx.pop(0)
        return len(self.maxx)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)