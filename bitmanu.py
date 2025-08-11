n = int(input())
binaryString = ""
while(n!=0):
    rem = n%2
    binaryString+=str(rem)
    n = n//2
print(binaryString[::-1])


#left shift
class solution:
    def checkKthBit(self, n, k):
        if((n&(1<<k)==0)):
            return False
        return True