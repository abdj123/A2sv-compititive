class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def checker(md):
            _max = 0
            sm = 0
            parts = 0
            ind = 0 
            while ind<leng:
                sm += nums[ind]
                if sm>md:
                    _max = max(_max,sm-nums[ind])
                    parts+=1
                    sm = nums[ind]
                ind+=1
                if ind==leng:
                    _max = max(_max,sm)
                    if sm<=md:
                        parts+=1
                if parts>k:
                    return [False]
            return [True,_max]

        pre = [0]
        leng = len(nums)

        for i in range(leng):
            pre.append(pre[-1]+nums[i])

        l = max(nums)
        r = pre[-1]
        ans = r
        while l<=r:
            mid = (l+r)//2
            chk = checker(mid)
            if chk[0]:
                ans = min(ans,chk[1])
                r = mid - 1
            else:
                l = mid + 1
        
        return ans