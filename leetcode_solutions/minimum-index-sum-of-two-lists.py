class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minsum, hashmap, out = float("inf"), {}, []
        for i in range(len(list1)):
            hashmap[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in hashmap:
                currsum = j + hashmap[list2[j]]
                if currsum < minsum:
                    minsum = currsum
                    out = []
                    out.append(list2[j])
                elif currsum == minsum:
                    out.append(list2[j])
        return out