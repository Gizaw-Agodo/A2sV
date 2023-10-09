class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        splitedV4 = queryIP.split('.')
        splitedV6 = queryIP.split(':')

        isV4 = True
        isV6 = True

        if len(splitedV4) == 4:
            for split in splitedV4:
                if not split.isdigit():
                    isV4 = False
                    break

                if len(split) > 1 and split[0] == "0":
                    isV4 = False
                    break
                if int(split) < 0 or int(split) > 255:
                    isV4 = False
                    break
        else:
            isV4 = False

        if len(splitedV6) == 8:
            for splited in splitedV6:
                
                if len(splited) < 1 or len(splited) > 4:
                    isV6 = False
                    break
                
                for char in splited:
                    if not ('0' <= char <= '9' or 'a' <= char <= 'f' or 'A' <= char <= 'F'):
                        isV6 = False
                        break    
        else:
            isV6 = False

        if isV4 :
            return "IPv4"
        elif isV6 :
            return 'IPv6'
        else:
            return 'Neither'



        

        
