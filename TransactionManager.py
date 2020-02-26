from datetime import date
import sys, pickle



class Transaction:
    def __init__(self, amount, isDeposit, description, BAT, ID):
        self.amount = amount
        self.isDeposit = isDeposit
        self.description = description
        self.BAT = BAT
        self.dateOfTransaction = str(date.today().strftime("%d/%m/%Y"))
        self.next = None
        self.ID = ID

    def getDateOfTransaction(self):
        return self.dateOfTransaction
    
    def getAmount(self):
        return self.amount

    def getBAT(self):
        return self.BAT

    def getNext(self):
        return self.next

    def getID(self):
        return self.ID

    def isDeposit(self):
        return self.isDeposit

    def getDescription(self):
        return self.description

    def setAmount(self, newAmount):
        self.amount = newAmount

    def setBAT(self, newBAT):
        self.BAT = newBAT

    def setDescription(self, newDescription):
        self.description = newDescription

    def setNext(self, transaction):
        self.next = transaction

    def outputDetails(self):
        print("Amount: " + str(self.getAmount()), "Date:" + self.dateOfTransaction,\
              "\nType:", "Deposit" if self.isDeposit == True else "Withdrawal",\
              "\nBalance after transaction: " + str(self.getBAT()),\
              "\nID: " + str(self.getID()),\
              "\nDescription: " + self.getDescription() + "\n")
        
        


def calculateBAT(isDeposit, amount, previousBAT):
    BAT = None
    if(isDeposit):
        BAT = round(previousBAT + amount, 2)
    elif(not isDeposit):
        BAT = round(previousBAT - amount, 2)
    return BAT


def addTransaction(amount, isDeposit, description, rootTransaction):
    ID = rootTransaction.getID() + 1
    current = rootTransaction
    while(current.getNext() != None):
        ID += 1
        current = current.getNext()
        
    BAT = calculateBAT (isDeposit, float(amount), current.getBAT())
    newTransaction = Transaction(amount, isDeposit, description, BAT, ID)
    current.setNext(newTransaction)

def clearTransactions(rootTransaction):
    confirmation = None
    while(confirmation != "YES" and confirmation.lower() != "no"):
        confirmation = input("Are you sure you want to clear all transactions? 'YES/NO'\n")      
    if(confirmation == "YES"):
        startingBalance = None
        while(type(startingBalance) != float):
            try:
                startingBalance = float(input("What is the starting amount of your new transaction chain?"))
            except:
                print("ERROR: Amount must be an integer of float value")
        rootTransaction.setAmount(0)
        rootTransaction.setDescription("ROOT")
        rootTransaction.setBAT(startingBalance)
        rootTransaction.setNext(None)
        rootTransaction.dateOfTransaction =  str(date.today().strftime("%d/%m/%Y"))
    else:
        return

def printTransactions(rootTransaction):
    current = rootTransaction
    while(current != None):
        current.outputDetails()
        current = current.getNext()


def getAmountFromUser():
    amount = None
    while(type(amount) != float):
        try:
            amount = float(input("Enter the amount"))
        except:
            print("ERROR: Amount must be an integer of float value")
    return amount

def checkIfDeposit():
    deposit = True
    while(True):
        isDeposit = input("Is this a deposit(D) or withdrawal(W)?")
        if(isDeposit == "W"):
            deposit = False
            return deposit
        elif(isDeposit == "D"):
            return deposit
    
    

def getDescriptionFromUser():
    description = input("Describe the transaction")
    return description

def editTransaction(rootTransaction):
    try:
        ID = input("Enter the ID of the transaction you want to edit\n") 
        if(not ID.isnumeric()):
            raise Exception("A non-numeric value was entered as an  ID")
        else:
            ID = int(ID)
    except Exception as error:
        print(error)
        return

    currentTransaction = rootTransaction
    while(currentTransaction != None):
        if(currentTransaction.getID() == ID):
            break
        currentTransaction = currentTransaction.next
    if(currentTransaction == None):
        print("Transaction not found")
        return
    currentTransaction.outputDetails()
    choice = input("What would you like to edit?\n\t1. Amount \n\t2. Description")
    if(choice == "1"):
        amount = currentTransaction.getAmount()
        try:
            newAmount = int(input("What would you like the new amount to be?"))
            currentTransaction.amount = newAmount
        except ValueError as error:
            print(error)
            return
        if(currentTransaction.isDeposit):
            amountDifference = round((newAmount - amount), 2)
            temp = currentTransaction
            while(temp != None):
                temp.BAT += amountDifference
                temp = temp.next
        else:
            amountDifference = round((newAmount - amount), 2)
            temp = currentTransaction
            while(temp != None):
                temp.BAT -= amountDifference
                temp = temp.next
        print("Amount sucessfully edited")
    if(choice == "2"):
        description = input("Enter your new description:\n")
        currentTransaction.setDescription(description)
        print("Description succesfully edited")
            
    

def deleteTransaction(rootTransaction):
    try:
        ID = int(input("Enter the ID of the transaction you want to delete\n"))
    except:
        print("ID must be a numerical value")
        return
        
    currentTransaction = rootTransaction
    previousTransaction = None
    found = False
    while(currentTransaction != None):
        if(currentTransaction.getID() == ID):
            found = True
            break
        previousTransaction = currentTransaction
        currentTransaction = currentTransaction.next
    if(found):
        if(currentTransaction.isDeposit == True):
            amount = currentTransaction.getAmount()
            temp = currentTransaction
            while(currentTransaction != None):
                currentTransaction.BAT = round(currentTransaction.BAT - amount, 2)
                currentTransaction.ID = currentTransaction.getID() - 1
                currentTransaction = currentTransaction.next    
            previousTransaction.next = temp.next   
        else:
            amount = currentTransaction.getAmount()
            temp = currentTransaction
            while(currentTransaction != None):
                currentTransaction.BAT = round(currentTransaction.BAT + amount, 2)
                currentTransaction.ID = currentTransaction.getID() - 1
                currentTransaction = currentTransaction.next
            previousTransaction.next = temp.next
            
        

def getBalance(rootTransaction):
    current = rootTransaction
    while(current.getNext() != None):
        current = current.getNext()
    return current.getBAT()


def menu(rootTransaction):
    while(True):
        choice = input("\nWhat would you like to do?\n\t1. Add a transaction\
                        \n\t2. Print Transactions\n\t3. Clear transactions\n\t4. Show balance\
                        \n\t5. Delete transaction \n\t6. Edit transaction \n\t7. Exit")
        if(choice == "1"):
            amount = getAmountFromUser()
            isDeposit = checkIfDeposit()
            description = getDescriptionFromUser()
            addTransaction(amount, isDeposit, description, rootTransaction)
            
        elif(choice == "2"):
            printTransactions(rootTransaction)

        elif(choice == "3"):
            clearTransactions(rootTransaction)

        elif(choice == "4"):
            print("\nCurrent Balance: £" + str(getBalance(rootTransaction)) + "\n")

        elif(choice == "5"):
            deleteTransaction(rootTransaction)

        elif(choice == "6"):
            editTransaction(rootTransaction)

        elif(choice == "7"):
            file = open("rootTransaction.dat", "wb")
            pickle.dump(rootTransaction, file)
            file.close()
            return
        
def main(): 
    file = open("rootTransaction.dat", "rb")
    rootTransaction = pickle.load(file)
    file.close()
    menu(rootTransaction)


    


if (__name__ == "__main__"):
    main()


        
