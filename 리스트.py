'''
list1=["abc", "dfg", "hij", 123, 456]
list1[1]='choe'
print(list1)
'''
#변수 이름을 "arr" 로 하고 아래 리스트를 대입(저장)하시오.
arr=[4,8,12,16,20,24,28,32]

#32=4*8
'''
arr1=[]
a=1
while True:
    if a==9:break
    arr1.append(4*a)
    a=a+1
print(arr1)    
'''
'''
arr[12341241,1234132431243214,3243214231423,4234123341234,1234123421342134,14324213423432,431241234312432141324,123431241324,324132432,14124,2314,123,4,1234,2134,32,4,2314,32,43,241,24,324,123,4,1234,21,21,34,213,42,14,12,42,314,123,4,1234,123423143214,1234321431242342134123,42314123421342134,3254776654,56789876543,4567890,16416456464895,4985689458975689569856,956958452659842698456,5846589658,87898965662,36898796532,35744752585696369,1234567890]
size=len(arr)#리스트의 크기 변화
print(size)
idx=0#인덱스 변수
while True:
    idx1=idx+1
    if idx==size:break
    if arr[idx]>arr[idx1]:
        tmp=arr[idx]
        arr[idx]=arr[idx1]
        arr[idx1]=tmp
    idx=idx+1
    print(arr)
print('-----------------')
print(sorted(arr))
'''

# 내생일 요일 찾기
'''
import datetime
today= datetime.datetime.now()
print(today)
print(f'오늘은 {today.year}년도 입니다')
print(f'오늘은 {today.month}월 입니다.')
print('태어난 날의 요일 맞추기')
y=int(input('년입력: '))
m=int(input('달입력: '))
d=int(input('일입력: '))

date=datetime.datetime(y,m,d)

if date.weekday()==0: print('월')
elif date.weekday()==1: print('화')
elif date.weekday()==2: print('수')
elif date.weekday()==3: print('목')
elif date.weekday()==4: print('금')
elif date.weekday()==5: print('토')
elif date.weekday()==6: print('일')
'''
import random
com=random.choice('RSP')
print(cpm)
