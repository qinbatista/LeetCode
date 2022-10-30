from ast import main


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                thissum = nums[index1] + nums[index2]
                print(thissum)
                print(str(index1) + " " + str(index2))
                print(str(value1) + " " + str(value2))
                if thissum == target and index1 != index2:
                    return [index1, index2]

    def addTwoNumbers(self, l1: list, l2: list):
        import numpy as np

        l2.reverse()
        l3 = np.add(l1, l2)
        sum_l1 = 0
        for index, i in enumerate(l3):
            sum_l1 = sum_l1 + i * (10 ** (len(l3) - index - 1))
        return sum_l1

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output,r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output


if __name__ == "__main__":
    # print(SolutionEasy().twoSum([3, 2, 4], 6))
    # print(SolutionEasy().addTwoNumbers([3, 2, 4], [6, 6, 4]))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkwe"))
