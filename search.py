# Jason-Judah Collaboration - Search function
# 09.26.2015

nice_words = sorted(['apple','banana','zebra','phlebotomist'])

def binarySearch(target, dataSet):
    current = int(len(dataSet) / 2)
    lowerBound = 0 # "aardvark"
    upperBound = len(dataSet) -1 # "zymurgy"
    
    while dataSet[current] != target:
        print('current = ' + str(current) + ', bounds = ' + str(lowerBound) + '-' + str(upperBound))
        
        if dataSet[current] > target:
            upperBound = current-1
        
        if dataSet[current] < target:
            lowerBound = current + 1
            
        previous = current
        current = int(lowerBound + ((upperBound - lowerBound) / 2))
        
        # target not in dataSet
        if current == previous: # no change => done halving
            return False
            
    return True
  
  
print(binarySearch('Jason', nice_words))          
    
        
