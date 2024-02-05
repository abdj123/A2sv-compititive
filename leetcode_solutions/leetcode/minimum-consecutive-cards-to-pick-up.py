class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if(len(set(cards))==len(cards)):
            return -1
        dic={}   
        res=1000000
        for i in range (len(cards)):
            if cards[i] not in dic:
                dic[cards[i]]=i
            else:
                if res>(i-(dic[cards[i]])):
                    res=(i-dic[cards[i]])
                dic[cards[i]]=i
        return res+1