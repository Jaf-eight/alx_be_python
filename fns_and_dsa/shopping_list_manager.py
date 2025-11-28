
if choice == '1':
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' added to the shopping list.")

elif choice == '2':
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' removed from the shopping list.")
    else:
        print(f"Item '{item}' not found in the shopping list.")

elif choice == '3':
    if shopping_list:
        print("Current Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")
