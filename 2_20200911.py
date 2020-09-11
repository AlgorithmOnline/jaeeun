test_case_num = int(input())
test_list =[]
for test in range(test_case_num):
        test_list.append(list(map(int, input().split())) )
         
num =1 
for train in test_list:
    train = [ i for i in train if i%2 ==1 ]
    print( "#"+str(num)+" "+str(sum(train)) )
    num+=1
