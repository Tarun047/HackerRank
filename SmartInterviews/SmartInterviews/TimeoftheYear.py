import time
t = int(input())
while t:
    print(time.strftime("%d-%^b-%Y %A",time.gmtime(int(input()))))
