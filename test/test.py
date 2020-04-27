#!/usr/bin/python3
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
print()
print(x)
fo = open("data.txt","r")
line = fo.readline();
print(line)
fo.close()