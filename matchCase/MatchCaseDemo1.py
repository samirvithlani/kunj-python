choice = int(input(f"Enter 1 for add\nEnter 2 for sub\nEnter "))

match choice:
    case 1:
        print("inside add:")
    case 2:
        print("sub")
    case _:
        print("default")          

        