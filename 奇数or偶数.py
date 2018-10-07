def jo():
    '''判断一个数是技术还是偶数.'''
    while True:
        try:
            number1=int(input("input a number:"))
            print(number1)
            if number1%2==0:
                print("%10d is a 偶数"%number1)
                break
            elif number1%2==1:
                print("%10d is a 技术"%number1)
                break
            else:
                number12=int(input("input a zirangshu:"))
        except:
            number12=int(input("input a zishu:"))
if __name__=="__main__":
    jo()