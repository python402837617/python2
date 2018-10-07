def kb():
    '''把千克变bang'''
    try:
        kg=float(input("please input how __kg"))
        bang=kg/1000
    except ValueError:
        print("valueerror")
    finally:
        print("%0.2f kg about %0.5f bang"%(kg,bang))
if __name__=="__main__":
    kb()