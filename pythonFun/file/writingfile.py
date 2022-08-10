f = open("hello.txt", "w")
a=int(input("enter line"))
for i in range(1,a+1):
    f.write("hello python")
    f.write("*-*")
    f.write("\n")

    f.close()
    h=("file,handling")
    print(h.split(','))