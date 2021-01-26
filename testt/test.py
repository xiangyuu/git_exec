"""
測試用例
"""

#計算
def count(x,y):
    c=0
    while c<700000:
        x+=1
        y+=1
        c+=1

#IO
def io():
    write()
    read()

def write():
    f=open("test","w")
    for i in range(180000):
        f.write("hello world\n")
    f.close()
def read():
    f=open("test")
    lines=f.readlines()
    f.close()