class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l,m,r = 0,1,len(nums)-1
        sort = sorted(nums)
        output = []

        while l < r and l < m:
            while m < r: 
                total = sort[l] + sort[m] + sort[r]   
                if(total < 0):
                    m+=1
                elif(total > 0):
                    r-=1
                elif(total == 0):
                    output.append([sort[l],sort[m],sort[r]])
                    while(m < r and sort[m] == sort[m+1]):
                        m += 1
                    m += 1


            
            while(l < r and sort[l] == sort[l+1]):
                l += 1
            l += 1
            m,r = l+1, len(nums)-1    
        return output
            




        