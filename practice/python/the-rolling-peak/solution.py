
def max_avg_subarray(nums, k):
  
  average:int = -999
  
  if len(nums) < k: 
    return None
  
  for i in range(len(nums)-k+1):
    avg = sum(nums[i:i+k])/k
    if avg > average:
       average = avg
       
  return average
  
  
