import random 
class Codec:
    def __init__(self): 
        self.dataBase = {}

    def encode(self, longUrl: str) -> str: 
        while True:
            key = random.randrange(6)
            if key not in self.dataBase:
                self.dataBase[key] = longUrl
                return "http://tinyurl.com/" + str(key)

    def decode(self, shortUrl: str) -> str: 
        i = shortUrl.rfind("/")
        key = int(shortUrl[i + 1:])
        return self.dataBase[key]