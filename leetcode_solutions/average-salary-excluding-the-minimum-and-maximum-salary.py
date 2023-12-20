class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)
        temp=salary[1:n-1]
        return sum(temp)/len(temp)
        