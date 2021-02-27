#1.Write a program which contains one lambda function which accepts one parameter and return
#power of two. 

sum=lambda no1,no2:no1*no2

def main():
    print("enter the first number")
    x=int(input())
    print("enter the second number")
    y=int(input())
    
    
    ret=sum(x,y)    
    
    print("multiplication is",ret)
if __name__=="__main__":
    main()
    
   