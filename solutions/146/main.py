class LRUCache:
    counter = 0 

    def __init__(self, capacity: int):
        self.dict = {}
        self.used_record = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        LRUCache.counter += 1 
        val = self.dict.get(key, -1)
        if val != -1: 
            self.used_record[key] = LRUCache.counter 
        return val 

    def put(self, key: int, value: int) -> None:
        LRUCache.counter += 1 
        if key not in self.dict and len(self.dict) == self.capacity:
            record = list(self.used_record.values())
            least_used = record.index(min(record))
            # reset timer and delete entry
            k = list(self.used_record.keys())[least_used] 
            del self.used_record[k] 
            k = list(self.dict.keys())[least_used]
            del self.dict[k] 
              
        self.dict[key] = value
        self.used_record[key] = LRUCache.counter   

if __name__ == "__main__": 
    obj = LRUCache(10)
    
    operations = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    inputs = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    
    results = []
    
    for i in range(len(operations)):
        
        operation = operations[i]
        input_values = inputs[i]
        
        if operation == "put":
            obj.put(input_values[0], input_values[1])
            results.append(None)
        elif operation == "get":
            value = obj.get(input_values[0])
            results.append(value)

        print(f"i = {i}, opt = {operation}, values = {input_values}, result {results[i]}")