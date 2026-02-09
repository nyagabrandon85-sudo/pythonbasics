"""
while loop-iterates through a block of code as long condition is true
while condition:
    #block of loop
"""
    #print python programming 5 times
x=1
while x<=5:
    print("python programming")
    x=x+1 #x=x+1

#print 0..7
y=0
while y<=7:
    print("The number is",y)
    y+=1

#print 20..30 break at 25
y=20
while y<=30:
    print("The number is",y)
    if y==25:
        break
    y+=1
