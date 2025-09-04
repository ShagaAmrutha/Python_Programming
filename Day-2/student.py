stdNo=input("enter std number")
Name=input("enter std name")
m1=int(input("enter marks 1"))
m2=int(input("enter marks 2"))
m3=int(input("enter marks 3"))
tm=(m1+m2+m3)
avg=round((tm/3),2)
print(f"std name {Name}\n std num {stdNo}\n total marks{tm}\n avg {avg}")
def grade(m):
    if(m>40 and m<=50):
        print("C grade")
    elif(m>50 and m<=70):
        print("B grade")
    elif(m>70 and m<=80):
        print("A grade")
    elif(m>80):
        print("distinction")
    elif(m<=40):
        print("fail")
grade(m1)
grade(m2)
grade(m3)