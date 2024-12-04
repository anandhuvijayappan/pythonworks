class bank:

    acno=str

    balance=int

    ac_type=str

    cusomer_name=str

    def __init__(self,acno,balance,ac_type,customer_name):

        self.acno=acno

        self.balance=balance

        self.ac_type=ac_type

        self.cusomer_name=customer_name

    def deposit(self,amount):

        self.balance+=amount

        print("Your A/C ",self.acno," has credit with amount Rs ",amount,"on ##/##/####. Avl Bal Rs ",self.balance,"")

    def print_details(self):

        print("Name : ",self.cusomer_name,"\nA/C No : ",self.acno,"\nA/C type : ",self.ac_type,"\nBalance : ",self.balance,)


customer1=bank(123456789,1000.50,'Savings','John Doe')

#customer1.print_details()

customer1.deposit(2485)