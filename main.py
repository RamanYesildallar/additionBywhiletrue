def adDition():
    myList = []





    while True:

        num=int(input("numbers:"))
        myList.append(num)
        result = 0
        if num==0:
            for i in myList:
                result+=i
            print(result)
            break


# For using code use this function
adDition()
