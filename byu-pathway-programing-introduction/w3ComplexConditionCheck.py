print("\t\tPlease provide answer from 1 to 10 to the following questions:\n\n")

loan = int(input("How large is the loan? "))
credit = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
payment =  int(input("How large is your down payment? \n\n"))

if loan >= 5:
    if credit >= 7 and income >= 7:
        print("yes")

    if credit >=7 or income >=7 and payment >=5 :
        print("yes")
    else:
        print("no")

    if(credit <7 or income <7):
         print("no")
else:
    if credit < 4:
         print("no")
    elif income >=7 or payment >=7:
         print("yes")
    elif income >4 and payment >=4:
         print("yes")
    else:
         print("no")
