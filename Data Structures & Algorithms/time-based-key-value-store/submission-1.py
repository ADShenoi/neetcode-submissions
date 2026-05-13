class TimeMap:

    def __init__(self):
        self.mp = {} # {key:{timestamp:value}}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = {timestamp:value}
        else:
            val_dict = self.mp[key]
            val_dict[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        key_val_pairs_dict = self.mp[key]
        sorted_items = sorted(key_val_pairs_dict.items(), key=lambda x:x[0])
        res = ''
        for ts, val in sorted_items:
            if ts <= timestamp:
                res = val
            else:
                break
        return res
            