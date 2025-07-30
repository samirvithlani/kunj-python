season ="monsoon"

match season:
    case "monsoon":
        print("monsoon season")
    case "summer":
        print("summer season")    


flag = input("enter y for yes and n for no")        

match flag:
    case "y" | "yes" | "YES" :
        print("yes")
    case "n":
        print("no")    