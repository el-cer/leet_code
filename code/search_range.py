
class Solution:
    def searchRange(self, nums, target):
        result_indices = [index for index in range(len(nums)) if target == nums[index]] or [-1, -1]  
        if len(result_indices)>1:
            return print(result_indices)
        elif len(result_indices)==1:
            result_indices = [result_indices[0],result_indices[0]] 
            return print(result_indices)       
             
sol = Solution()
sol.searchRange([1,2,3],target=3)


