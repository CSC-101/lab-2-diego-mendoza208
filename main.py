# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."
   return message


message = welcome_message("dmendo64@calpoly.edu")
print(message)

def smallest(n: float, m:float) -> float:
   if n < m:
      return n    #This statement is not evaluated for either calls
   else:
      return m

first = smallest(3,2)      #first = 2
second = smallest(2,2)     #second = 2, this is reasonable since this function determines the lowest value between 2 inputs, in this case it fits the criteria
print()



def function2(a:int, b:int, c:int) -> int:
   if a>b and a >c:
      return a - b   #This will be called in general whenever a is the greatest numerically
   elif b > c:
      return b + c   #This will be called whenever b is greater than c and if the last expression wasn't evaluated, or when a is not greater than b and c
   else:
      return 2 * c

answer1 = function2(3, 2, 1)
answer2 = function2(2, 3, 1)
answer3 = function2(2, 1, 3)
print()