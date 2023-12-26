class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        visits = {}

        for cp in cpdomains:
            l = cp.split(' ')
            value = l[0]
            domain = l[1]

            subdomains = domain.split(".")
            
            for i in range(len(subdomains)):
                sub = '.'.join(subdomains[i:])


                if sub not in visits:
                    visits[sub] = value
                else:
                    visits[sub] = str(int(visits[sub]) + int(value))
                
        for k, v in visits.items():
            res.append(v+' '+k)

        return res