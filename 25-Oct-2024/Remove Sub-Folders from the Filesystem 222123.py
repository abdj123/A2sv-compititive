# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        res = set()

        folder.sort()

        for i in folder:
            flag = False
            for k, v in enumerate(i):
                if v == "/":
                    if i[:k] in res:
                        flag = True
                        break
            if not flag:
                res.add(i)

        return list(res)
