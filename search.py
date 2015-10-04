# Search - Regression Testing (runs w/ feedback)
# 09.27.2015
# -notes from (09_masterMind.py)

##Test Cases:
##*simple find, not in list, list empty, case sensitive
##*bounds: fist in list, last in list
##*list even, odd


nice_words = sorted(['apple','banana','zebra','phlebotomist'])

# A binary search; like dictionary halving
def search(target, dataSet):
    current = int(len(dataSet) / 2)
    lowerBound = 0
    upperBound = len(dataSet) -1

    # List Empty
    if len(dataSet) == 0:
        print ('target:', target, '\n', 'found: dataSet is empty') 
        return 'dataSet is empty'
    
    while dataSet[current].lower() != target.lower(): # Case Sensitive
        #print('current = ' + str(current) + ', bounds = ' + str(lowerBound) + '-' + str(upperBound))
        
        if dataSet[current].lower() > target.lower(): # Case Sensitive
            upperBound = current-1
        
        if dataSet[current].lower() < target.lower(): # Case Sensitive
            lowerBound = current + 1
            
        previous = current
        current = int(lowerBound + ((upperBound - lowerBound) / 2))
        
        # target not in dataSet
        if current == previous: # no change => done halving
            # TESTING: target not in list
            # comment out for regular function use
            print('target:', target + '\n', 'found: not in dataSet') 

            return False

    # TESTING: found target
    # comment out for regular function use
    print('target:', target, '\n', 'found:', dataSet[current])        

    return True
  

# REGRESSION TESTING
def testSearch():
    target = 'banana monkey banana BANANA apple zebra'.split()
    passCount = 0
    failCount = 0
    testCaseList = [
        {'target': target[0], 'dataSet': nice_words, 'testName': 'simple find', 'expected': True},
        {'target': target[1], 'dataSet': nice_words, 'testName': 'not in dataSet', 'expected': False},
        {'target': target[2], 'dataSet': [],        'testName': 'dataSet empty', 'expected': 'dataSet is empty'},
        {'target': target[3], 'dataSet': nice_words, 'testName': 'case sensitive', 'expected': True},
        {'target': target[4], 'dataSet': nice_words, 'testName': 'bounds_first in list', 'expected': True},
        {'target': target[5], 'dataSet': nice_words, 'testName': 'bounds_last in list', 'expected': True}
    ]

    for i in range(len(testCaseList)):
        actual = search(target[i], testCaseList[i]['dataSet'])
        if actual == testCaseList[i]['expected']:
            passCount += 1
            print('  test:', testCaseList[i]['testName'])
            print('Result: Passed\n')
        else:
            failCount += 1
            print('  test:', testCaseList[i]['testName'])
            print('Result: FAIL')
            print('dataSet = ')
            print(testCaseList[i]['dataSet'])
            if actual: print(', returned: True\n')
            if not actual: print('returned: False\n')

    #test for list that has odd number of words
    oddList = nice_words[:]
    oddList.append('jason')
    oddList = sorted(oddList)
    if search('jason', oddList):
        passCount += 1
        print('  test: odd size dataSet')
        print('Result: Passed\n')
    else:
        failCount += 1
        print('test: odd size dataSet')
        print('Result: Failed\n')

    print(str(passCount) + ' test(s) passed')
    print(str(failCount) + ' test(s) failed')


testSearch()

