grade = []
sort = [0]

def highFinder(scores = []):
    topScore = 0
    for i in scores:
        if i > topScore:
            topScore = i
    return topScore

def lowFinder(scores = []):
    lowScore = 100
    for i in scores:
        if i < lowScore:
            lowScore = i
    return lowScore

def avgFinder(scores = []):
    total = 0
    x = 0
    for i in scores:
        x = x + 1
        total = total + i
        
    avgScore = int(total / x)
    return avgScore

def sortItOut (highScore, sort = [], grades = []):
     sort[0] = highScore
     for i in range(0, numofstud):
          for x in range(0, numofstud):
               if grade[x] > sort[i] and grade[x]!=highscore and grade[x] < sort[i-1]:
                    sort[i] = grade[x]
     return sort

while True:
    numofstud = int(input("How Many Students took this test ?:"))
    
    i = 0
    while i < numofstud:
        question = "What is the grade of student number " + str(i) + "?:" 
        grade.append(i)
        sort.append(i)
        grade[i] = int(input(question))
        i = i + 1
        
    highscore = highFinder(grade)
    
    lowscore = lowFinder(grade)
            
    avgscore = avgFinder(grade)
    
    sort = sortItOut(highscore, sort, grade)

    for i in range(0, numofstud):
        print( grade[i])
        
    print("The highest grade is ", highscore)
    print("The lowest grade is ", lowscore)
    print("The average grade is ", avgscore)
    
    for i in range(0, numofstud):
        print( sort[i])
        
