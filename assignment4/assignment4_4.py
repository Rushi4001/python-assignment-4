#Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which are even. Map function will calculate its square.
#Reduce will return addition of all that numbers.
import functools
a=lambda no:(no%2==0)

b=lambda no:no*no

c=lambda no1,no2:no1+no2


def main():
    array=[]
    print("enter the number of element you want to print")
    num=int(input())
    for i in range (num):
        print("enter the number",i+1)
        value=int(input())
        array.append(value)
    print("array=",array)
    
    data=list(filter(a,array))
    print("filter data=",data)
    
    newdata=list(map(b,data))
    print("map data=",newdata)
    
    our=functools.reduce(c,newdata)
    print("reduce =",our)

if __name__=="__main__":
    main()