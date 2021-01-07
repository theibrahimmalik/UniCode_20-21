class Solution:
    
    def get_recipient(self, message, position):
        word = []
        words = []
        condition = False
        
        for letter in message:
            if letter == '@':
                condition = True
                
                
                
"""
word = []
words = []
condition = false 

for characters in message
    if character == @
        condition True
    
    while condition
        if character is letters, numbers, underscores or hypthens
            append to list
        else 
            condition False
            words.append(word)

wordslength 
if position > worldslength
    return ""
else
    return words[position]
"""
