class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokens.get(tokenId, -1) == -1: 
            return 
        if self.tokens[tokenId] <= currentTime:
            self.tokens.pop(tokenId)
        else: 
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0 
        for k, v in self.tokens.items(): 
            if v > currentTime: 
                cnt += 1 
        return cnt

if __name__ == "__main__": 
    authenticationManager = AuthenticationManager(5)
    authenticationManager.renew("aaa", 1)
    authenticationManager.generate("aaa", 2)
    assert authenticationManager.countUnexpiredTokens(6) == 1
    