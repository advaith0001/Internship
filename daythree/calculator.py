again="y";

while again =="y":
    try:
        num1 = int(input("eneter the first number:"))
        num2 = int(input("enter the second number: "))

        Result=0

        choice = input("enter a choice (+-*/) : ")

        match choice :
            case "+":
                Result= num1+num2
                print(f"the result is : {Result}")
                
            case "-":
                Result = num1-num2
                print(f"the result is : {Result}")
                
            case "*":
                Result = num1*num2
                print(f"the result is : {Result}")
                
            case "/":
                Result= num1/num2
                print(f"the result is : {Result}")
                
            case _:
                print("choose a valid operand")
                
                
        again =input("Do you want to continue (y/n)")
         
        if (again =="n"):
            break
        
    except ZeroDivisionError:
        print("Cannot be divided by zero")
        
    except ValueError:
        print("Enter an integer ")
            
       

