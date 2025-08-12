n = int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

#2nd pattern
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


#3rd pattern
n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()


#4th pattern
n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()


#5th pattern
n = int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

#6th pattern
n = int(input())
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*n-2*i-1):
        print("*",end=" ")
    print()