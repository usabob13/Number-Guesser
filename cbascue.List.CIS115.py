#Codie Bascue, Lab, Wk.6, CIS115, DeVry University

#Start by giving a welcome message
print("Welcome to the shopping list program")
print()

#set variable for shopping list
shoppingList = ["bananas", "apples"]

#create menu
print("1. Add an item")
print("2. List all items")
print("3. Delete an item")
print("4. Exit")

#define the add item function
def add_item(shoppingList):
    newItem = input("Please enter the new item you would like to add: ")
    print()
    addition = shoppingList.append(newItem)
    print(newItem," was added to the list!")

#define the display the list function
def list_items(shoppingList):
    for item in shoppingList:
        print(shoppingList.index(item) + 1, ":", item)

#define the delete an item function
def delete_item(shopping_list):
    numberDel = int(input("Which number to delete: "))
    print()
    if numberDel < 1 or numberDel > len(shopping_list):
        print("Invalid number\n")
    else:
        itemDel = shoppingList.pop(numberDel - 1)
        print(itemDel," was deleted\n")

#define the main function
def main():
    while True:
        print()
        option = int(input("Please pick a menu option: "))
        print()
        if option == 1:
            add_item(shoppingList)
        elif option == 2:
            list_items(shoppingList)
        elif option == 3:
            delete_item(shoppingList)
        elif option == 4:
            print("Thank you for using the list program! Have a great day!")
            break
        else:
            print("Not a valid command, please try again.")


if __name__ == "__main__":
    main();
    

