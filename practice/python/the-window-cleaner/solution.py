def longest_unique_substr(s):
  char_index = {}
  left = 0
  max_len = 0
  
  for right, letter in enumerate(s):
    if letter in char_index and char_index[letter]>=left:
      left = char_index[letter] + 1
    char_index[letter] = right
    
    char_len = right - left +1
    
    if char_len > max_len:
      max_len = char_len
  return max_len
