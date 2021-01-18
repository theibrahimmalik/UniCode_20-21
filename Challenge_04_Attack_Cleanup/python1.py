class AttackCleanup:
    
    def restore_data(self, message):
        
        finalMessage = []
        isNumber = False
        actualNumber = 0
        
        for character in message:
            while isNumber:
                for i in range(actualNumber-1):
                    if character == 'g':
                        finalMessage.append('t')
                    elif character == 't':
                        finalMessage.append('g')
                    elif character == 'x':
                        finalMessage.append('c')
                    elif character == 'z':
                        finalMessage.append('a')
                        
                isNumber = False
                    
            if character == 'g':
                finalMessage.append('t')
            elif character == 't':
                finalMessage.append('g')
            elif character == 'x':
                finalMessage.append('c')
            elif character == 'z':
                finalMessage.append('a')
            elif character.isdigit():
                actualNumber = int(character)
                isNumber = True
                
                
        str1 = ''.join(finalMessage)
        return str1
        


m1 = AttackCleanup()
m1.restore_data('gtxgtxzg3z8g4txz3g3z')


"""
number = False
actualNumber = 0
for loop message
    while number:
        for i in actualNumber:
            if characterEncoded:
                list.append(appendChatacterDecodedinList)
        number = False
    if characterCoded:
        appendCharacterDecodeinList
    elif number:
        number = true:
        

input:
- zgtxtxzgtxtxz
-  gtxgtxzg3z8g4txz3g3z

the problem questions are getting more and more vague.
it's literally solve for "string1" -> "string1 output", "string2" -> "string2 output"

possible solutions:
-	Regex
-	Just for loop it and use lists 
-	Hashmaps/key-value pairs 

Input/Before = Output/After 
g = t
t = g
x = c
z = a

"""

"""

60% solution
"""
