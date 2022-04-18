def printList (message, theList):
   print (message)
   for index in range (len(theList)):
      print (format (index, "4d"), end= '')
   print()
   for value in theList:
      print (format (value, ">4s"), end= '')
   print()
   print()
   
def mySort (theList):
   #what items should be compared
   for numOfPasses in range (0, len(theList) - 1):
      listInOrder = True
      for index in range (len(theList) - 1 - numOfPasses):
         #the comparison
         if theList[index].lower() < theList[index + 1].lower():
            listInOrder = False
            #the swap, if needed
            temp = theList[index]
            theList[index] = theList[index + 1]
            theList[index + 1] = temp
            #what items should be compared
      if listInOrder:
         #print ("Breaking at pass ", numOfPasses + 1)
         break 
      #printList ("After pass " + str(numOfPasses + 1), theList)

def mySort2 (theList):
   for indexToPutInPlace in range (0, len(theList) - 1):
      for index in range (indexToPutInPlace + 1, len(theList)):
         if theList[indexToPutInPlace].lower() > theList[index].lower():
            temp = theList[index]
            theList[index] = theList[indexToPutInPlace]
            theList[indexToPutInPlace] = temp
   
      
def binarySearch (theList, letterToFind):
   low = 0
   high = len(theList) - 1
   while low <= high:
      mid = (low + high) // 2
      if letterToFind.lower() < theList[mid].lower(): #looking to the "left"
         high = mid - 1
      elif letterToFind.lower() > theList[mid].lower(): #looking to the "right"
         low = mid + 1
      else:
         return True
   return False   
         

def main ():
   #values = ["r", "n", "M", "g", "w", "E", "a", "D", "l", "s", "T", "c", "k", "B", "q" ]
   
   #printList ("Initial list ", values)
   #values.sort()
   #printList ("After builtin sort ", values)
   
   #set values back to the original order
   #values = ["r", "n", "M", "g", "w", "E", "a", "D", "l", "s", "T", "c", "k", "B", "q" ]
   #printList ("Back to the original list ", values)
   #mySort (values)
   #printList ("After our sort ", values)
   #mySort (values)
   values = ["r", "n", "M", "g", "w", "E", "a", "D", "l", "s", "T", "c", "k", "B", "q" ]
   #printList ("Back to the original list ", values)
   mySort2 (values)
   printList ("After our sort2 ", values)
   print ("Is B in the list? ", binarySearch(values, "B"))
   print ("Is o in the list? ", binarySearch(values, "o"))

   
main()   
   
              
              