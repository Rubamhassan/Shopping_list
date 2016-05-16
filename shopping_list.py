"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.
"""
shopping_list = []


def add_shopping_list(item):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "Here's your updated list", sorted_shopping_list()
    else:
        print "This item %s already exists!" % (item)


def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list


def remove_item(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed. Here's your updated list" % (item), sorted_shopping_list()
    else:
        print "%s was not on the list." % (item)


def replace_item(old_item, new_item):
    old_item = old_item.lower()
    new_item = new_item.lower()

    if old_item in shopping_list:
        item_index = shopping_list.index(old_item)
        print "%s has replaced %s in the list." % (new_item, old_item)
    else:
        print "%s is not in the list." % (old_item)

def menu():
    print "1 to add to the list"
    print "2 to sort the list"
    print "3 to replace and item"
    print "4 to remove and item"
    options=int(raw_input("choose a number:  "))
    return options


def main():
    option = menu()
    while True:
        if option > 0 and option < 5:
            if option == 1:
                item = raw_input("what would you like to add?   ")
                add_shopping_list(item)
            elif option == 2:
                print sorted_shopping_list()
            elif option == 3:
                old_item = raw_input("what would you like to take out?  ")
                new_item = raw_input("what would you like to add in?  ")
                replace_item(old_item, new_item)
            else:
                item = raw_input("what would you like to take out?  ")
                remove_item(item)

            option = menu()
        else:
            print "your list is done"
            break 

if __name__=="__main__":
    main()
    
# # TEST FUNCTIONS
# # 1 - add 4 times to your shopping list
# add_shopping_list("apple")
# add_shopping_list("steak")
# add_shopping_list("beef")
# add_shopping_list("mustard")

# # 2 - Add an item that is already in the list. what happens?
# add_shopping_list("apple")

# # 3 - Remove an item on your list
# remove_item("apple")

# # 4 - Remove an item that is not in the list. what happens?
# remove_item("chicken")

# # 5 - you've changed your mind on one of your items. you want to substitute it with something else.
# replace_item("mustard", "ketchup")
