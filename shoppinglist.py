def show_help():
#print help keys
    print (" write every yhings you need to buy")
    print ("use 'DOWN' for end your list")
    #have help command
    print("use 'HELP' command")
    #have show command
    print("use 'SHOW' command")

def show_list():
    print("heres your list >>")  
    for item in shopping_list:
        print(item)


def add_to_list(new_item):
     #add new item to list    
    shopping_list.append(new_item)
    print ("add {}. list now has {}item.".format(new_item,len(shopping_list)))
#make list
shopping_list = []

show_help()

#code refactoring
#ask for new item
while True:
    new_item = input(" > ")

    #key for quit the app
    if new_item == 'DOWN':
        break
    elif new_item == 'SHOW':
        show_list()
        continue
    elif new_item == 'HELP':
        show_help()
        continue

    add_to_list(new_item)   
    

