case = 0
while 1:

    L, P, V = map(int, input().split(" "))
    if L ==0 and P ==0 and V == 0:
        break
    case+=1
    moc= V // P
    namuji= V % P
    # 이렇게 조건을 나눠야한다는 것을 몰라서 2번이나 틀림. 주의를 기울여서 overflow 에 대해서 생각을 해야한다.
    if namuji< L:
        print("Case "+str(case)+": "+str(moc * L +namuji))
    else:
        print("Case "+str(case)+": "+str(moc * L +L))
