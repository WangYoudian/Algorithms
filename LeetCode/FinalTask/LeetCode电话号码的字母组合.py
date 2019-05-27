# 17 https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []

        if "0" in digits or "1" in digits:
            return []

        key_hm = {}
        key_hm['2'] = "abc"
        key_hm['3'] = "def"
        key_hm['4'] = "ghi"
        key_hm['5'] = "jkl"
        key_hm['6'] = "mno"
        key_hm['7'] = "pqrs"
        key_hm['8'] = "tuv"
        key_hm['9'] = "wxyz"

        # Initialize the mapping hashmap of char strings for phone number
        output = [key for key in key_hm[digits[0]]]

        # Iterate through each number provided in the digits
        for index in range(1, len(digits)):
            number = digits[index]
            # exclude the invalid digits such as 0 and 1

            # Create the permutation of possible options
            options = []
            for key in key_hm[number]:
                options += [option+key for option in output]
            output = options

        return output        

if __name__ == '__main__':
    solution = Solution()
    # data
    digits = "2345"

    output = solution.letterCombinations(digits)
    print(output)
    # sort the list to make it lexicographical 
    output = sorted(output, key=lambda x:x[0], reverse=False)
    print(output)

# 
# 0和1是否判定为非法输入？
# 似乎在OJ中并没有这样的测试用例