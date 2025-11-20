import random

again = "y"

while again =="y":


    print("Generated Number")
    
    print(random.randint(1,6))
    
    again =input("Do you want to continue(y,n):")
    
    if again == "n":
        print("Thank you for your time")
        break
    
    
    
