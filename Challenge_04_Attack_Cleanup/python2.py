import re
class AttackCleanup:

    def restore_data(self, message):
        x = re.findall(r'[A-Za-z]|-?\d+\.\d+|-?\d+|', message)

        num = 1

        str = ""

        for i in x:
            j = 0

            if i.isnumeric():
                num = int(i)
            else:
                while j < num:
                    if i == "z":
                        str += "a"
                    elif i == "g":
                        str += "t"
                    elif i == "t":
                        str += "g"
                    elif i == "x":
                        str += "c"

                    j += 1
                num = 1
        
        return str
        
        
        """
        100% solution 
        """
