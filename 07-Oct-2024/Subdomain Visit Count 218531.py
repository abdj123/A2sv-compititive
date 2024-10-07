# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ls = defaultdict(int)
        res = []

        for i in cpdomains:
            a = i.split()[-1]
            val = i.split()[0]
            a = a.split('.')
            prefix = a[-1]
            ls[a[-1]] += int(val)
            for j in range(len(a) - 2, -1, -1):
                prefix = f"{a[j]}." + prefix
                ls[prefix] += int(val)
        
        for k,v in ls.items():
            res.append(f"{v} {k}")
        
        return res