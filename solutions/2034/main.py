from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.price = SortedList()
        self.time_price_map = {}
        self.max_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.time_price_map: 
            self.price.discard(self.time_price_map[timestamp])
        self.price.add(price)
        self.time_price_map[timestamp] = price 
        self.max_timestamp = max(timestamp, self.max_timestamp)

    def current(self) -> int:
        return self.time_price_map[self.max_timestamp]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]

if __name__ == "__main__":
    obj = StockPrice()
    obj.update(1, 10)
    param_2 = obj.current()
    print(param_2)
    param_3 = obj.maximum()
    print(param_3)
    param_4 = obj.minimum()
    print(param_4)
