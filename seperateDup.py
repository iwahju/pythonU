# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once. 
# The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of O(1).
# Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

def remove(self, nums: list[int])-> int:
    l,r = 0,1
    while r in range (len(nums)):
        if nums[l] == nums[r]:
            r+=1
            print (l,r)
        else:
            nums[l+1] = nums[r]
            l +=1
            r+=1
    return l+1 





def main():
    print (remove[1,1,2])

main()
