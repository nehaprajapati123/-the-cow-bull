def fun(list1):
    print("choose 5 numbers from the given list")
    print(list1)
    import random
    list2=[]
    for i in range(5):
        list2.append(random.choice(list1))
    print(list2)
    j=0
    bull=0
    cow=0
    not1=0
    bull1=[]
    cow1=[]
    not2=[]
    while j<len(list2):
        number=int(input("enter your number"))
        position=int(input("enter your number's position"))
        if list2[j]==number:
            if j+1==position:
                bull=bull+1
            else:
                cow=cow+1
        else:
            not1=not1+1
        j=j+1
    bull1.append(bull)
    print("bull:-",bull1)
    if bull==5:
        print("you are winner")
    cow1.append(cow)
    print("cow:-",cow1)
    not2.append(not1)
    print("not exist:-",not2)

fun([0,1,2,3,4,5,6,7,8,9])
