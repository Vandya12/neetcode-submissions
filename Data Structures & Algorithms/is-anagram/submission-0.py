class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        for j in t:
            freq[j]=freq.get(j,0)-1
        for _,val in freq.items():
            if val!=0:
                return False
        return True