num = float(input("请输入一个数:"))
if num%2==0:
    if num%5==0:
        print("{}可以整除2，也可以整除5".format(num))
    else:
        print("{}可以整除2，但不可以整除5".format(num))

else:
    if num%5==0:
        print("{}可以整除5，但是无法整除2".format(num))
    else:
        print("{}不可以整除5，也不可以整除2".format(num))