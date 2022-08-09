##x=132
##y=0
##print(x*y)
##x='hello  world'
##print('H ' in x)
##
##
##x=False
##y=True
##print('x or y', x or y)
##x1=6
##y1=7
##print(x1 is not y1)
##
##no=400
##print("the decimal value of",no,"is:")
##print(bin(no),"in binary.")
##a=3+7j
##print(type(a))
##
##a=3.3
##print(type(a))
##a='jeswin'
##b='raja'
##c=a+ "   "+b
##print(c)
##print(a.title())
##a=["physics","chemistry",1999,2021,]
##b=[1,2,3,4,5,6]
##print("a [0]=",a [0])
##print("b [2:4]=",b[2:4]
##      )
##a=["physics",1991,2021]
##print("value avaible at index 2")
##print( [a])
##
##print("new Value avaible index 2=2001")
##b=[2001]
##print([b])
##a=[1,2,3,4,5]
##print (a)
##del a [3]
##print ()
##print (a)
##a=[1,2,3,4,5]
##a.append(7)
##print(a)
##a.extend([9,8,6])
##print(a)
##a=("maths","tamil","english")
##b=(1,2,3,4,5,6,7)
##c=('a','b','c')
##print("a[1]=",a[1])
##print("b[2;6]=",b[2:6])
##a=(1,8,8)
##b=("tamil","english","maths")
##c=a+b
##print(c)
##a=(1,2,3,4,5,6,7)
##print (len(a))
##a={'a':33,'b':33,'e':{'c':55,'d':99}}
##print( a['e'])
##no=5
##if no>=0:
##    print(no,"is a postive number")
##elif no==0:
##    print("zero")
##
##else:
##    print(no ,"is a negative number")

##a=0
##while(a<8):
##    print("the a is=",a)
##    a+=1
##print("good bye")
##a=4
##while a<2:
##    print(a)
##    a+=1
##else:
##    print("a is no longer less than 4")
##numbers=[1.5,2.5,56,78,5]
####sum=0
##for val in numbers:
##    sum=sum+val
##
##print("the sum is" ,sum)
##a=('jeswin','raja')
##for i in range   (len(a)):
##    print("I like",a[i])
##a=[1,2,3,4,5,6,7,8,9]
##for s in a:
##    print (s)
##else:
##    print("no items left")
##
##for i in range(1,6):
##    for j in range (i):
##        print("*",end='')
##    print()
##i=7
##while(i>0):
##    j=7
##    while(j>1):
##        print("%",end='')
##        j=j-1
##    i=i-1
##    print()
##a="jeswin"
##for i in a:
##    if i=='s':
##        continue
##    print('current i :',i)
##a="jeswinraja"
##for i in a:
##    if (i=='s'):
##        break
##print("current i =",i)
##
##a='lijovijay'
##for i in a:
##    print("i:",i)
##    pass
##print('last i:',i)
##def jeswin(name):
##    print("welcome to" + name) 
##jeswin("python")    
##def lijo(C):
##    return 5*
##C
##print(lijo(15))
##def vijay(a):
##    if (a==3):
##        return "jeswin"
##    if (a==6):
##        return "jeeva"
##x=int (input("enter a value betwen 3 and 6 :"))
##print(x,"in words",vijay (x))
##def raja (state = "kanniyakumkari"):
##    print("i am going to "+ state)
##raja( "ooty")
##raja("nagercoil")
##def s(x,y=10):
##    return x*y
##print( s (16))
##print(s(5,98))
##def h (a,b=5,v=78):
##    print('a is ',a,'and b is ',b,'and v is ',v,',h is',a*b-v)
##h(2,3)          
##h(a=6,b=8)
##s=56
##def call():
##    print("s inside",s)
##call()
##print("s outside",s)
##def dispvalue():
##    global x
##    x+=4
##    print("value of x in dispvalue fuction is",x)
##    return None
##x=3
##dispvalue()
##x=5
##def call():
##    x=10
##    print("x:",x)
##call()
##print("x:",x)
#labmda
##a=lambda x:x+7
##print(a(3))
##a=[1,2,3,4,5,8,6]
##b=list(filter(lambda x:(x%2==0),a))
##print (b)
##def a(x):
##    return x%2==0
##even=filter(a,range(1,8))
##print (list (even))
##a=[1,2,3,7,6,4,8]
##s=list (map(lambda x:x*2,a))
##print(s)
##def a(x):
##    return x+x
##a=map(a,range(1,11))
##print(list(a))
##from functools import reduce
##list=[2,3,4,5]
##print(reduce(lambda a,b:a+b,list))

##def addseq(x):
##    if x==1:
##        return 1
##    else:
##        return x+addseq(x-1)
##print("the sum of first 10 sequence number is ",addseq(10))
#modulus
##import calendar
##year=int(input("enter year :"))
##calendar.prcal(year)
##import datetime
##x=datetime.datetime.now()
##print(x)

##class rect:
##    a=7
##    b=8
##c=rect()
##print(c.a+c.b)
##class rect:
##    a=9
##    b=6
#print((rect.a*rect.b))
##print(rect.__name__,rect.__base__)
##print(rect.b__dict__)
##class rect:
##    a=7
##    b=6
##    
##    def rectarea(self):
##        return self.a*self.b
##r=rect()
##print("area of rectangle",r.rectarea())
##class person:
##    
##    def __init__(self,name,age):
##        self.name =name
##        self.age=age
##p1=person("john",30)
##print(p1.name)
##class rect:
##    def __init__(self,x=6,y=5):
##        self.a=x
##        self.b=y
##    def rectarea(self):
##        return self.a*self.b
##r=rect()
##s=rect(4,8)
##print(r.rectarea())
##print(s.rectarea())
##class rect :
##    def __init__(self,a,b):
##        self.j=a
##        self.e=b
##    def __str__(self):
##        return "j is%d, e is%d"%(self.j,self.e)
##    def rectangle (self):
##        return (self.j*self.e)
##r=rect(8,23)
##print(r)
##class book:
##    price=525
##    @classmethod
##    def display(cls):
##        print(cls.price)
##    def show(self,x):
##        self.price=x
##        print(self.price)
##b=book()
##c=book()
##book.display()
##b.display()
##b.show(527)
##c.display()
##
##class  jeswin:
##    @staticmethod
##    def raja():
##        I=50
##        print("length is",1)
##jeswin.raja()
##r=jeswin()
##r.raja()
##class jeswin:
##    def __init__(self,x,y): 
##        self.a=x
##        self.b=y
    #def jeswin(self):
##        return self.a*self.b
##r=jeswin(52,5)
##s=r
##print(r.jeswin())
##print(s.jeswin())
##class rect:
##    n =0
##    def __init__(self,x,y):
##        rect.n+=1
##        self.a=x
##        self.b=y
##    def __del__(self):
##        rect.n-=1
##        class_name=self.__class__.__name__
##        print(class_name,'destoryed')
##    def rectarea(self):
##        print("area of rectangle is",self.a*self.b)
##    def noofobject(self):
##        print("number of object",rect.n)
##r=rect(2,6)
##r.rectarea()
##s=rect(5,3)
##s.rectarea()
##r.noofobject()
##del r
##s.noofobject
##del s
##class add:
##    __a=2
##    __b=4
##    c=__a+__b
##    def adder(self):
##        return f"the sum is(self.c)"
##add.__a=10
##print(add.__a)
##class worker:
##    def __init__(self,c,n,s):
##        self.code=c
##        self.name=n
##        self.salary=s
##    def showworker(self):
##        print(self.code)
##        print(self.name)
##        print(self.salary)
##class officer(worker):
##    def __init__(self,c,n,s):
##        worker.__init__ (self,c,n,s)
##        self.hr=s*60/100
##        worker.showworker(self)
##        print(self.hr)
##class manager(worker):
##    def __init__(self,c,n,s):
##        worker.__init__(self,c,n,s)
##        self.hr=s*60/100
##        self.da=s*80/100
##    def showworker(self):
##        worker.showmanager(self)
##        print(self.hr)
##        print(self.da)
##w=worker(100,'jeswin',5000)
##o=officer(200,'raj',6000)
##m=manager(300,'raja',7000)
##print(w.showworker)
###print(o.showofficer)
              
##    
##    
##class aji:
##    def __init__(self,name,age,rollno):
##        self.name:name
##        self.age:age
##        self.rollno:rollno
##    def __get__(self,aji,jeswin,age):
##        return self.name,self.age,self.rollno
##        print(self.name)
##        print(self.age)
##        print(self.rollno)
##        return
##    def __set__(self,jeswin,age):
##        self.age=age
##    class raj:
##        c=("anu",20,1125)
##    d=raj()
##    print(d.c)
##    d.c=30
##    print(d.c)
from tkinter import*
from PIL import Image ,ImageTk
a=Tk()
a.title("jeswin")
a.geometry("400x300")
b=Label(a,text="username")
b.place(x=20,y=20)
e=Entry(a,bd=5)
e.place(x=100,y=20)
photo=PhotoImage(file="button.png")

Button(a,image=photo).pack(side=BOTTOM,pady=20)
a.mainloop()
