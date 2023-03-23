# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

# Two Pointer 
def pairWithSum(arr, targetSum):
    left, right= 0, len(arr)-1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            return left, right
        if currentSum > targetSum:
            right -=1
        else:
            left +=1
    return [-1,-1]

# Hash Table
# def pairWithSumm(arr, targetSum):
#     nums = {}
#     for i, num in enumerate (nums):
#         if targetSum - num = 


def main():
    print (pairWithSum([1,2,3,4,6],6))


main()