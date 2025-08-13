class solution:
    def generate(self,ind,curr_subset,ans,nums):
        if(ind == len(nums)):
            ans.append(curr_subset.copy())
            return 
        curr_subset.append(nums[ind])
        self.generate(ind+1,curr_subset,ans,nums)
        curr_subset.pop()
        self.generate(ind+1,curr_subset,ans,nums)
    def subsets(self,nums: list[int]) -> list[list[int]]:
        curr_subset = []
        ans = []
        ind = 0
        self.generate(ind,curr_subset,ans,nums)
        return ans
ob=solution()
nums = [1,2,3]
print(ob.subsets(nums))