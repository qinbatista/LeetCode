from ast import main


class SolutionEasy:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index1, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums):
                thissum = nums[index1]+nums[index2]
                print(thissum)
                print(str(index1)+" "+ str(index2))
                print(str(value1)+" "+ str(value2))
                if thissum == target and index1 != index2:
                    return [index1, index2]

if __name__ == "__main__":
    print(SolutionEasy().twoSum([3, 2, 4], 6))