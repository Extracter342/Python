def Gmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)


def isgreater(a,b):
    if(a>b):
         print("a is greater")
    else:
            print("b is greater")



a = int(input("enter the number : "))
b = int(input("enter the number : "))
isgreater(a,b)
Gmean(a,b)



c = 51
d = 50
isgreater(c,d)
Gmean(c,d)