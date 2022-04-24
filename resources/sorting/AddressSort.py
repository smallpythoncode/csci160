def printList (message, theList):
   print (message)
   for value in theList:
      print (value)
   print()
   
def mySort (theList):
   for numOfPasses in range (0, len(theList) - 1):
      for index in range (len(theList) - 1 - numOfPasses):

         firstNumber, firstStreet = theList[index].split(" ", 1)
         secondNumber, secondStreet = theList[index + 1].split(" ", 1)
         if int(firstNumber) > int(secondNumber):
            
            temp = theList[index]
            theList[index] = theList[index + 1]
            theList[index + 1] = temp

def main():
   addresses = [
      '900 University Ave', 
      '2400 University Ave', 
      '1500 University Ave', 
      '60 University Ave']
   
   printList ("Before sort ", addresses)
   mySort (addresses)
   printList ("After sort ", addresses)

main()
