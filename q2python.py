class Solution:

    def devvie(self, input):

        self.cords = input 
        
        coordinate = [0, 0]
        direction = ['north', 'east', 'south', 'west']
        currentDirection = direction[0]
        
        
        for command in self.cords:
            if command == 'L':
                currentDirection = direction[direction[currentDirection]-1]
            elif command == 'R':
                currentDirection = direction[direction[currentDirection]+1]
                
            elif command == 'F':
                if currentDirection == 'north':
                    coordinate[1]+=1
                elif currentDirection == 'east':
                    coordinate[0]+=1
                elif currentDirection == 'south':
                    coordinate[1]-=1
                elif currentDirection == 'west':
                    coordinate[0]-=1
                else:
                    break
            else:
                break
        
        counter = 0 
        
        
        if coordinate == [0, 0]:
            return 0
        
        while coordinate[0] != 0:
            if coordinate[0] < 0:
                while currentDirection != 'east':
                    if currentDirection == 'north':
                        currentDirection = direction[direction[currentDirection]+1]
                        counter+=1
                    elif currentDiection == 'south':
                        currentDirection = direction[direction[currentDirection]-1]
                        counter+=1
                    else:
                        currentDirection = direction[direction[currentDirection]-1]
                        counter+=1
                
                coordintate[0]+=1
                counter+=1
                
                
            elif coordinate[0] > 0:
                while currentDirection != 'west':
                    if currentDirection == 'north':
                        currentDirection = direction[direction[currentDirection]-1]
                    elif currentDirection == 'south':
                        currentDirection = direction[direction[currentDirection]+1]
                    else:
                        currentDirection = direction[direction[currentDirection]-1]
                
                coordinate[0]-=1
                counter+=1 
                
        while coordinate[1] != 0:
            if coordinate[1] < 0:
                while currentDirection != 'north':
                    if currentDirection == 'west':
                        currentDirection = direction[direction[currentDirection]+1]
                        counter+=1
                    elif currentDirection == 'east':
                        currentDirection = direction[direction[currentDirection]-1]
                        counter+=1 
                    else:
                        currentDirection = direction[direction[currentDirection]-1]
                        counter+=1 
                        
                coordinate[1]+=1
                counter+=1
                
            elif coordinate[1] > 0:
                while currentDirection != 'south':
                    if currentDirection == 'west':
                        currentDirection = direction[direction[currentDirection]-1]
                        counter+=1
                    elif currentDirection == 'east':
                        currentDirection = direction[direction[currentDirection]+1]
                        counter+=1
                    else:
                        currentDirection = direction[direction[currentDirection]+1]
                        counter+=1
                
                coordinate[1]-=1
                counter+=1 
                
        print(counter)
                
                
one = Solution()
one.devvie("RF")
print(one.counter)
