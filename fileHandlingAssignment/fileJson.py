import json

#open the file in the read mode using context manager.
#Hence no need to close the file- this will be handled automatically.
#Using json module from the python- load() help to read the json from the File and stored that data as python object (list)
#To calculate the number of books len() is used
def readJson():
    with open("inventory.json","r") as file: 
        inventory = json.load(file)
        print(f"Initial Total Number of Books : {len(inventory)}")




def saveJson():
    new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
    # Open file with read mode and load the json data into python object
    with open ("inventory.json","r") as file:
        inventory = json.load(file)
    #Open file in Write mode , adding the new data into the python list using append()
    #using dump() python data is converted to Json and placed in the file.
    #indent is used for formatting purpose (indentation space)
    with open("inventory.json","w") as file:
        inventory.append(new_book)
        json.dump(inventory,file,indent=4)





def printJson():
    #read the data from the json file . Used for loop to iterate into each data.
    #using print(f ) datas are printed in a expected format
    with open ("inventory.json","r") as file:
        inventory = json.load(file)
        for data in inventory:
            print(f"Title: {data["title"]} | Author: {data["author"]} | Price: ${data["price"]}")



readJson()
saveJson()
printJson()