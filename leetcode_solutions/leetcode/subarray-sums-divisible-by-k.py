class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dct=defaultdict(int)
        dct[0]=1
        s=0
        
        for n in nums:
            s=(s+n)%k
            dct[s]+=1
            
        return sum(v*v-v for v in dct.values())>>1