class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        res = ""
        values = self.store.get(key,[])
        l,r = 0, len(values) - 1
        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
    
    def get_backwards_implementation(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        for i in range(len(self.store[key]) - 1, -1, -1):
            if self.store[key][i][1] <= timestamp:
                return self.store[key][i][0]
        
        return ""