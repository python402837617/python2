#非闭包
start=0
def go(step):
    global start
    now=start+step
    start=now
    return start
print(go(2))
print(go(3))

#闭包
def f(position):
    def go(step):
        nonlocal position
        now=position+step
        position=now
        return position
    return go
now_position=f(0)
print(now_position(2))
print(now_position(3))     