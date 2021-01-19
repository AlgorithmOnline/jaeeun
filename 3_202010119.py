HH, MM = map(int, input().split())
total=HH*60+MM-45+24*60
print((total//60)%24,total%60)

