class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [[value, timestamp]]
        else:
            self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap: return ""
        
        key_vals = self.hashmap[key]
        lo, hi = 0, len(key_vals) - 1
        res = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if key_vals[mid][1] <= timestamp:
                lo = mid + 1
                res = key_vals[mid][0]
            
            else:
                hi = mid - 1
        
        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)