class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visitCount = defaultdict(int)
        for domain in cpdomains:
            countDomain = domain.split()
            visits = int(countDomain[0])
            temp = []
            for domain in reversed(countDomain[1].split(".")):
                temp.append(domain)
                currDomain = ".".join(reversed(temp))
                visitCount[currDomain] += visits
                
        resultArr = []
        for domain in visitCount:
            resultArr.append(str(visitCount[domain])+" "+domain)
            
        return resultArr