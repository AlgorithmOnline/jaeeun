"""

퀵정렬을 구현해 문제풀이를 진행했다.
퀵정렬은 피봇을 기준으로 왼쪽에는 작은 값, 오른쪽에는 큰값을 오게 만들어 재귀를 통해 정렬하는 것이다.

"""
import sys
arr=[]
n = int(input())
for i in range(n):
    arr.append(int(input()))
def quickSort(left, right,arr):
    # left 가 클 경우 종료
    if left>=right:
        return 
    i = left
    j = right
    pivot = arr[(lrft+right)//2]
    # i,j 가 교차하면 종료한다.
    while(i<=j):
        # i 가 작은거라면 통과, 아니라면 멈춘다. -> 교환해야함.
        while(arr[i]<pivot):
            i+=1
        # j가 큰거라면 통과 아니라면 멈춘다-> 교환
        while(arr[j]>pivot):
            j-=1
        if(i<=j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1
    quickSort(left, j,arr)
    quickSort(i,right,arr)
quickSort(0,n-1,arr)
for i in range(n):
    print(arr[i])

