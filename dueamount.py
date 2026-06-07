def dueamount(Billamount, Billpayed):
    return Billamount - Billpayed
Bill = int(input("Enter the bill amount: "))
Payed = int(input("Enter the amount that has been payed: "))
print("Due amount: ", dueamount(Bill, Payed))