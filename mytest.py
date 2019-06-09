if __name__ == '__main__':
#experiment1
    import math

    radius =float(input("please input the circle's radius r = "))
    area =math.pi*radius*radius
    h = float(input("please input the hight h = "))
    print("the volume is ",area*h)

#experiment2
    num = int(input("please input a num to judge if it is a prime number num = "))
    flag = int(0)
    for i in range(2,num-1):
        if(num%i!=0):
            flag=1
    if(flag==1):
        print("this num is prime number")
    else:
        print("this num isn't prime number")