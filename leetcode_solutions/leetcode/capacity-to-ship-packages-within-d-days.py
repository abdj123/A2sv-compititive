class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right, best = max(weights), sum(weights), -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # compute the number of days it is giong to take us to transport the packages
            # calculated_day
            calculated_day = 1
            counter = 0
            for i in range(len(weights)):
                counter += weights[i]
                if counter > mid:
                    calculated_day += 1
                    counter = weights[i]
                
                    
            
            if calculated_day > days:
                left = mid + 1
            else:
                right = mid - 1
                best = mid
                
        return best
            
  




        
        

        