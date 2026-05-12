class FreqStack:

    def __init__(self):
        self.s = []
        self.mp = defaultdict(int)

    def push(self, val: int) -> None:
        self.s.append(val)
        self.mp[val] += 1

    def pop(self) -> int:
        maxFreq = max(self.mp.values())
        
        for i in range(len(self.s)-1, -1, -1):
            val = self.s[i]

            if self.mp[val] == maxFreq:
                self.s.pop(i)
                
                self.mp[val] -= 1

                if self.mp[val] == 0:
                    del self.mp[val]

                return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()