# Problem: Find the minimum element in an array
# Approach: Traverse the array and keep track of the smallest value seen so far.
# Time Complexity: O(n)
# Space Complexity: O(1) where do i need to add it 

arr = [7,4,3,9,2,8]
min_value = arr[0]

for i in arr:
      if i < min_value:
            min_value = i 
        
print('Lowest Value:', min_value)
