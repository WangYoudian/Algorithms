class Solution:
    # The tricky part of this problem is making sure each recursive case 
    # returns a list and lists, and that you can build the solution from 
    # the list of lists from the child call.
    def permute(self, nums : list) -> list:
        res = []
        if len(nums)==0:
            return [res]

        for i in range(len(nums)):
            permute_str = nums[:i] + nums[i+1:]
            child_permutation = self.permute(permute_str)
            for lst in child_permutation:
                res.append([nums[i]]+lst)
        return res

if __name__ == '__main__':
    solution = Solution()
    # data
    nums = [1,2,3,3,4,5]

    print(solution.permute(nums))