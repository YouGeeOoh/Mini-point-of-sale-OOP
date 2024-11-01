# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

       
class Products:
    def __init__(self, name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def getProductName(self):
        return self.name
    
    def getProductPrice(self):
        return self.price
    
    def getProductQuantity(self):
        return self.quantity
    
    def updateQuantity(self, quantity):
        self.quantity = quantity


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.products = []

    def addProduct(self, product):
        self.products.append(product)
        self.saveToFile()
        print(f"Product {product.getProductName()} succesfully Added!\n")

    def getAllProduct(self):
        return self.products          

    def getProduct(self, name):
        if len(self.products) == 0 :
            return "Product not found"
        else:
            for product in self.products:
                if name == product.getProductName():
                    return product
            
                return "Product not found"

    def deleteProduct(self, produc):
        try:
            file = open(self.filename, 'w')
            for product in self.products:
                if(product != produc):
                    line = f"{product.getProductName()} {product.getProductPrice()} {product.getProductQuantity()}\n"
                    file.write(line)
                
            file.close()
        except FileNotFoundError:
            file = open(self.filename, 'x')
    
        file.close()

    
         #return self.products.remove(product)

    def saveToFile(self):
        try:
            file = open(self.filename, 'w')
            for product in self.products:
                line = f"{product.getProductName()} {product.getProductPrice()} {product.getProductQuantity()}\n"
                file.write(line)
                
            file.close()
        except FileNotFoundError:
            file = open(self.filename, 'x')
    
        file.close()

    def loadFromFile(self):
        try:
            file = open(self.filename, 'r')
            data =  file.read()
            #print(data)
            if not data:
                print("Empty data!")
            else:
                lines = data.split('\n')
                for line in lines:
                    if line:
                        newData = line.split(' ')
                        print(newData)
                        product = Products(newData[0], newData[1], newData[2])
                        self.products.append(product)
            file.close()
        except FileNotFoundError:
            file = open(self.filename, 'x') 
            self.products.clear()
            file.close()

def shopOperation():
        notSucessful = True
        while notSucessful:
            print("*** Welcome to Our Shop ***")
            print("\t 1 -> To Add a Product to stock")
            print("\t 2 -> To sell a Product")
            print("\t 3 -> To view a Product ")
            print("\t 4 -> To delete a Product")
            print("\t 5 -> To exit")

            try:
                action = int(input(" Please choose a value: "))
            except ValueError:
                print("Please key a number")
                # action = int(input(" Please insert a number"))
            else:
                notSucessful = False
                return action
            

def readInput(message):
        notSucessful = True
        while notSucessful:    
            try:
                action = int(input(message))
            except:
                print("Please key in a number")
            else:
                notSucessful = False
                return action
            
database = Database("product.txt")
database.loadFromFile()

running = True

while running:
    action = shopOperation()

    if action == 1:
        name = input("Enter product name: ")
        response = database.getProduct(name)
        if response != "Product not found":
            print ("product is in stock already")
        else:
            price = float (readInput("input the price: "))
            quantity = readInput("Enter the quantity: ")
            product = Products(name, price,quantity)
            database.addProduct(product)
    elif action == 2:
      try:
          name = input("Enter the product name: ") 
          response = database.getProduct(name)
          sell = database.getAllProduct()
          normalPrice = float(response.getProductPrice())
          normalQuantity = int(response.getProductQuantity())
    
          if response != "Product not found":
             try:
                 price = float(readInput("Input price to buy: "))
            
                 if price == normalPrice:
                    
                     quantity = readInput("Enter quantity: ")
                     if quantity < normalQuantity:
                         normalQuantity -= quantity
                         response.updateQuantity(normalQuantity)
                         total = price * quantity
                         print(f"Your total cost for buying {quantity} {name} is {float(total)}")
                         print ("Thank You for patronising us!")
                     else:
                         print("We do not have up to this quantity")
                 elif (price < normalPrice):
                     print("low price")
                     print(price, "price", type(price))
                 elif (price > normalPrice):
                     print("Higher than the price")
             except:
                  print("please input a number")
          else: 
              print(f"We do not have {name} in stock now")
      except:
            print("Input a product in the database")
      
    elif action == 3: 
        products = database.getAllProduct()
        print("Name\t\tPrice\t\tQuantity")
        for product in products:
            print(f"{product.getProductName()}\t\t{product.getProductPrice()}\t\t{product.getProductQuantity()}")
    elif action == 4:
        try:
            name = input("Enter product name: ")
            response = database.getProduct(name)
            maindb = database.getAllProduct()
            print(response)
            
            products = database.products
            
            if response != "Product not found":
                products.remove(response)
                database.deleteProduct(response)  
        except:
            print("Input correctly")
    elif action == 5:
        print("Exitting! \nThanks for checking on us.")
        running = False
    else:
        print("Wrong input!\nPrint numbers from 1 - 5")