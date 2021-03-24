#Problem Given
#Convert a string containing only lower case letter to a string with upper case
#It is expected to solve the problem within O(sizeof(str) 
#Auxilary Space O(1)

#function to convert string into upper
def to_upper(str):
        #temp will store the intger value of 1st letter of the string 
        temp = 0        
        #loop will run till the end of string
        for i in range(len(str)):
            #ord converts the char into its equivalent integer value
            #ord(str[0]) - 32, so we will get ASCII value of upper case
            temp  = ord(str[0])-32
            #storing string in the same string but removing the first element
            str = str[1::]
            #chr converts integer into its equivalent char value
            #adding or concatenating the str and temp together then storing it in str
            str = str+chr(temp)
        
        #return str    
        return str

if __name__ == "__main__":
    n = input()
    print(to_upper(n))