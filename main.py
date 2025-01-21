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
      return 2 * c   #This will be called when a is not bigger than b or c, and if b is not bigger than c, in other words when c is the largest

answer1 = function2(3, 2, 1)  #answer1 = 1
answer2 = function2(2, 3, 1)  #answer2 = 4
answer3 = function2(2, 1, 3)  #answer3 = 6
print()

from typing import Optional
def checked_access(L:list[int], idx:int) -> Optional[int]:
   test = idx >= 0 and idx < len(L)    #This values whether or not the integer sent can possibly be used as an index
   if test:    #This checks whether the variable test is true or false
      return L[idx]
   else:
      return None

first = checked_access([1, 0, 1], 9)   #first = None
second = checked_access([1, 0, 1], 2) #second = 1
print()


def length_sum(L:list[str]) -> int:
   if len(L) > 2:
      result = len(L[0]) + len(L[1]) + len(L[2])   #the 'first' call (4 + 2 +  3 = 9),
   elif len(L) > 1:
      result = len(L[0]) + len(L[1])     #the 'third' call(7 + 4 = 11)
   elif len(L) > 0:
      result = len(L[0])   #the 'second' call (11),
   else:
      result = 0
   return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

def suprising(L:list[str], other:str) -> list[str]:
   L.append(other.upper())
   return L

words = ["this", "is", "confusing", "code."]
first = suprising(words, "Avoid")
second = suprising(words, "such.")
      #words = ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
      #first = second = ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
      #first and second are both linked to the value of words,which was changed throughout the code.
print()