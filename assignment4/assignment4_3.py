#Write a program which contains filter(), map() and reduce() in it. Python application which
#contains one list of numbers. List contains the numbers which are accepted from user. Filter
#should filter out all such numbers which greater than or equal to 70 and less than or equal to
#90. Map function will increase each number by 10. Reduce will return product of all that
#numbers. 


import functools
    
chkfun=lambda no1:70<=no1<=90
gun=lambda no:no+10
learn=lambda no1,no2:no1*no2 


def main():
    array=[]
    print("enter the number of elements")
    value1=int(input())
    for i in range (value1):
        print("enter the number:",i+1)
        value2=int(input())
        
        array.append(value2)
    print("you enter the data of your array is:",array)    
    
    fun=list(filter(chkfun,array))
    print("after fiter data is",fun)
    
    mun=list(map(gun,fun))
    print("after map data is :",mun)
    
    output=functools.reduce(learn,mun)
    print("after reduce is:",output)

if __name__=="__main__":
    main()