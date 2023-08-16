def main(nums):

    if not nums:
        return 0
    #The variable l_pointer is initialized to 1. 
    #This variable will be used to keep track of the length of the array without duplicates.
    l_pointer = 1 
    for r_pointer in range(1, len(nums)):
        #loop compares each element with the previous one(r_pointer - 1).
        if nums[r_pointer] != nums[r_pointer - 1]:
            #If the current element is different from the previous element(i.e., it's not a duplicate),
            #the l_pointer is incremented. This essentially counts the number of unique elements in the array.
            nums[l_pointer] = nums[r_pointer]
            #After the loop completes, the function returns the value of l_pointer,
            #which represents the length of the array without duplicates.
            l_pointer += 1
       
    return l_pointer

nums = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5]
results = main(nums)
print("Removed Dulicates:", results)
print("Modified Array:", nums[:results])  # Printing the array without duplicates
