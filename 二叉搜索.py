def  ercha(target,list):
    left=0
    right=len(list)-1
    while left<right:
        middle=(left+right)//2
        if target==list[middle]:
            return middle
        elif target<list[middle]:
            right=middle-1
        elif target>list[middle]:
            left=middle+1
    return "no"
l=[20,44,48,55,62,66,74,88,93,99]
print(ercha(44,l))
def bx(target,list):
    left=0 
    right=len(list)
    if target>="Maaaaaa":
        left=len(list)//2-1
        while left<right:
            middle=(left+right)//2
            if target==list[middle]:
                return middle
            elif target<list[middle]:
                right=middle-1
            else:
                left=left+1
        return "no\tno\tno"
    else:
        right=len(list)//2-1
        while left<right:
            middle=(left+right)//2
            if target==list[middle]:
                return middle
            elif target<list[middle]:
                right=middle-1
            else:
                left=left+1
        return "no\tno"
l2=["Adas","Bob","Mili","Smith"]
print(bx("Mili",l2))