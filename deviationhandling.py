#creating the function
def num_valid():
    #expectinal handling inside while loop
    while True:
        try:
            num1=int(input("Input the first Number:"))
            num2=int(input("Input second Number:"))
                #checking if entered number is between 0-256
            if (num1>0 and num1<256) and (num2>0 and num2<256):
                break
            else:
                print("Enter the numbers between 0-256")
                continue
        except ValueError:
            print("Only numbers are allowed")
            continue
        else:
            break
    return num1,num2


