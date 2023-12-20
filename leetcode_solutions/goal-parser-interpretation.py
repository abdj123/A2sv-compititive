class Solution:
    def interpret(self, command: str) -> str:
        # dict={"G":"G","(":"o","(al)":"al"}
        res=""
        i=0
        # for i in range(len(command)):
        while(i<len(command)):
            if(command[i]=="G"):
                res+="G"
                i+=1
            elif(command[i:i+2]=="()"):
                res+="o"
                i+=2
            else:
                res+="al"
                i+=4
        return res
        