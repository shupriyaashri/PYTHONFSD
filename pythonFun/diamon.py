def fetdiamond(num):
    i,j,flag=1,num//2,False
    while i>0:
    print(" " * j,"*" *i)
    if i<num and not flag:
        i,j=i+2,j-1
        else:
            flag,i,j=true,i-2,j+1

def greetuser(user="subi",message="hello,how are you"):
    return f"{user} {message}"

def perform(function=getdiamond,title="somethings"):
    print(greetuser(title))
    function(5)

def anotheroperation(val):
    print(f"i have num{val}")

perform(title="operation")
