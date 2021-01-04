class Cipher:
    
    def halliday(self, inStr):
        shift = 13
        outStr = ""
        for i in range(len(inStr)):
            inChr = inStr[i]
            inN = ord(inChr)
            if inChr.isalpha():
                if inN > 96 and inN < 123:
                    low = 97
                elif inN > 64 and inN < 91:
                    low = 65
                    
                outN = inN-shift
                while outN < low:
                    outN += 26
                outChr = chr(outN)
            else:
                outChr = inChr
                
            outStr += outChr
            
        return outStr
