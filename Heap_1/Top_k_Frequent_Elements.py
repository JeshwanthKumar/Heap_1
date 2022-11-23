#Time_Complexity: O(n)
#Space_Complexity: O(n) - Size of hashmap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}    #Initialize a hashmap
        result = [] #Initialize result
        
        bucket = [[]for i in range(len(nums)+1)]    #Initialize a bucket with empty arrays for the length of nums+1
        
        for num in nums:    #Continue till nums
            if num in hashmap:  #If num in hashmap then add 1 to that element in hashmap
                hashmap[num] += 1
            else:   #Else initialize 1 to that element in the hashmap
                hashmap[num] = 1
        
        for key, val in hashmap.items():    #For every key and values in hashmap
            bucket[val].append(key) #Append the key to that value in the bucket
            
            
        for i in range(len(bucket)-1, -1, -1):  #Continue till the length of bucket from reverse
            if len(bucket[i]) > 0:  #If the length of bucket of that index is greater than 0
                result += bucket[i] #Add result with that element in the bucket
                k -= len(bucket[i]) #Subtract k with the length of bucket
            if k == 0:  #If k is equal to 0 break
                break
                
        return result   #Return result