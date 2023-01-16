class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True 

        s1, s2 = list(sentence1.split()), list(sentence2.split())
        m, n = len(s1), len(s2)
        if m < n: 
            s1, s2 = s2, s1 
            m, n = n, m 

        if n == 1: 
            return s2[0] == s1[0] or s2[0] == s1[-1]

        i, j = 0, m-1 
        a, b = 0, n-1 
        while i < j:     
            if a > b: 
                return True         
            if s1[i] == s2[a]: 
                i += 1 
                a += 1 
            elif s1[j] == s2[b]: 
                j -= 1 
                b -= 1 
            else: 
                return False  
        
        return a > b

if __name__ == "__main__": 
    s = Solution() 

    sentence1 = "A A"
    sentence2 = "A aA"
    assert not s.areSentencesSimilar(sentence1, sentence2)

    sentence1 = "hsYZKp Cn eE"
    sentence2 = "hsYZKp eE"
    assert s.areSentencesSimilar(sentence1, sentence2)

    sentence1 = "a BaabbAABbBbbaAb"
    sentence2 = "a BbbA baaaaBaAabB bbab AaAB"
    assert not s.areSentencesSimilar(sentence1, sentence2)

    sentence1 = "Eating right now"
    sentence2 = "Eating"
    assert s.areSentencesSimilar(sentence1, sentence2)

    sentence1 = "A B C D B B"
    sentence2 = "A B B"
    assert s.areSentencesSimilar(sentence1, sentence2)

    sentence1 = "c h p Ny"
    sentence2 = "c BDQ r h p Ny"
    assert s.areSentencesSimilar(sentence1, sentence2)

    sentence1 = "Ogn WtWj HneS"
    sentence2 = "Ogn WtWj HneS"
    assert s.areSentencesSimilar(sentence1, sentence2)

    sentence1 = "of"
    sentence2 = "A lot of words"
    assert not s.areSentencesSimilar(sentence1, sentence2)

    sentence1 = "My name is Haley"
    sentence2 = "My Haley"
    assert s.areSentencesSimilar(sentence1, sentence2)