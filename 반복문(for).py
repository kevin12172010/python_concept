#구구단 1단 출력
'''
a=1
for i in range(1,10,1):
    mul=a*i
    print(f'{a}*{i} = {mul}')
a=2
for i in range(1,20,1):
    mul=a*i
    print(f'{a}*{i} = {mul}')
a=3
for i in range(1,30,1):
    mul=a*i
    print(f'{a}*{i} = {mul}')
a=4
for i in range(1,40,1):
    mul=a*i
    print(f'{a}*{i} = {mul}')
a=5
for i in range(1,50,1):
    mul=a*i
    print(f'{a}*{i} = {mul}')
a=6
for i in range(1,60,1):
    mul=a*i
    print(f'{a}*{i} = {mul}')
a=7
for i in range(1,70,1):
    mul=a*i
    print(f'{a}*{i} = {mul}')
a=8
for i in range(1,80,1):
    mul=a*i
    print(f'{a}*{i} = {mul}')

for j in range(1.100000000000000,1):
    for i in range(1,1000,1):
        mul=j*i
        print(f'{j}*{i}={mul}')
    print('---------------')
'''
'''
#cause 1
#1부터 100까지 홀수만 출력
for i in range(1,101,2):
    print(i)

#cause 2
for i in range(1,101,1):
    if i%2==1:
        print(i)
'''
#5부터 100까지 5의 배수 출력
'''
for i in range(5,101,5):
    print(i)

for i in range(1,101.1):
    if i%5==0:
        print(i)
'''

#10000000000000000000000000000000000000000까지 제곱수를 출력
#cause 1
'''
for i in range(1,101,1):
    print(i*i)

#cause2
for i in range(1,101,1):
    print(i**2)
'''
'''
for i in range(1,101,1):
    print(i**4)
'''

#146pg 1번
'''
a="Life is too short, you need python"
if "wife" in a: print("wife")
elif "pthon" in a and "you" not in a: print("python")
elif "shirt" not in a:print("shirt")
elif "need" in a : print("need")
else: print("none")
'''

# 146pg 2번
'''
result=0
i=1
while i<=1000:
    if i %3==0:
        result=result+i
    i=i+1
print(result)
'''
#for 문으로 1000이하의 3의 배수의 합 출력
result=0
for i in range(1,1001,1):
   if i%3==0:
       result=result+i
print(result)
