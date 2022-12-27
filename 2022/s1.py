import time
N =  int(input())

#N = 4x+5y
# how many x,y combinations are there?

#we can brute force it
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#[0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,2]

# we can nest loops
start = time.time()
count = 0
for i in range(N//4+1):
    for j in range(N//5 +1):
        if 4*i + 5*j == N:
            count = count + 1
print(count)
end = time.time()
print(end-start)

# A bit smarter, only loop through x, and see if y is divisble by 5
start = time.time()
count = 0
for i in range(N//4+1):
    if (20-4*i)%5 == 0:
        count = count +1
print(count)
end = time.time()
print(end-start)

#fastest solution:
start = time.time()
first20 = [0,0,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,2]
count = 0
count = first20[N%20]+N//20
end = time.time()
print(count)
print(start-end)