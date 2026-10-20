class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for wrd in strs:
            new_str += (str(len(wrd))+"#"+wrd)
        return new_str

    def decode(self, s: str) -> List[str]:
        l = 0 
        r = 1 
        res = []
        while r < len(s):
            while s[r] != "#":
                r += 1
            
            #get word length
            wrd_len = s[l:r]
            print(wrd_len)
            l = r  + 1
            r = l + int(wrd_len)

            # get word 
            wrd = s[l:r]
            res.append(wrd)

            l = r

        return res