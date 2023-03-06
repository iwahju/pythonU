# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

def pairWithSum (arr, targetsum):
    left, right = 0, len(arr)-1
    while left < right: 
        currentSum = arr[left] + arr[right]
        if currentSum == targetsum:
            return [left,right]
        if currentSum > targetsum:
            right -=1
        else:
            left +=1
    return print ("error")



def main():
    print (pairWithSum([1,2,3,4,6],6))


main()