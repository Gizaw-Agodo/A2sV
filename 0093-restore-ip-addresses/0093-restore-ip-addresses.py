class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_ips = []
        def backtrack(ip_config, start):
            if ip_config:
                if len(ip_config[-1]) > 1 and ip_config[-1][0] == "0" :
                    return
                elif int(ip_config[-1]) > 255:
                    return
            if len(ip_config) == 4:
                if start == len(s):
                    valid_ips.append(".".join(ip_config))
            
            for i in range(start, min(start + 3,len(s))):
                ip_config.append(s[start:i+1])
                backtrack(ip_config, i + 1)
                ip_config.pop()
                            
                         
        backtrack([], 0)
        return valid_ips
                
        
            
    