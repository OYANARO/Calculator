primer = input("Введите пример: ")
m = " "
y = ["+","-","/","*"]
if m in primer:
    x = primer.split(" ")
    x[0],x[2] = int(x[0]),int(x[2])
    if y[0] in x:
        print(x[0]+x[2])
    elif y[1] in x:
        print(x[0]-x[2])
    elif y[2] in x:
        if x[2] == 0:
            print("На ноль делить нельзя")
        else:
            print(x[0]/x[2])
    elif y[3] in x:
        print(x[0]*x[2])
else:
    x = primer
    if y[0] in x:
        x = primer.split("+")
        x[0],x[1] = int(x[0]),int(x[1])
        print(x[0]+x[1])
    elif y[1] in x:
        x = primer.split("-")
        x[0],x[1] = int(x[0]),int(x[1])
        print(x[0]-x[1])
    elif y[2] in x:
        x = primer.split("/")
        x[0],x[1] = int(x[0]),int(x[1])
        if x[1] == 0:
            print("На ноль делить нельзя")
        else:
            print(x[0]/x[1])
    elif y[3] in x:
        x = primer.split("*")
        x[0],x[1] = int(x[0]),int(x[1])
        print(x[0]*x[1])