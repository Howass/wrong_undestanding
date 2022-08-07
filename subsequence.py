//check if str s is in str t or not
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind=t.index(s[0])
        t=t[ind:]
        while(True):
            flag=0
            for i in range(len(s)-1):
                print(i)
                if (t[i]!=s[i]):
                    flag=1
            if(flag==0):
                return True
            t=t[1:]
            if (s[0] not in t):
                return False
            ind=t.index(s[0])
            t=t[ind:]


            
