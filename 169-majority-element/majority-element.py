class Solution(object):
    def majorityElement(self, nums):
        count = 0
        x = None
        for num in nums:
            if count == 0:
               x= num  
            if num == x:
               count+=1
            else:
               count-=1
        return x
           
                 

           