#def convert_temperature(celsius):
    #fahrenheit =("Temp in fahrenheit", fahrenheit)

while True:
    try:
        celsius = float(input("Enter temperature in celsius"))
        fahrenheit = (celsius * 9/5) + 32
        print("Temp in fahrenheit" , fahrenheit)
        #convert_temperature(fahrenheit)

    except Exception as e:
        print("Actual Error is ",e)

    choice = input("Do you want to convert again? yes/no")
    
    if choice == "no":
        print("ok bye")
        break


    elif choice == "yes":
        continue

    else:
        print("only just yes  or no")
        


        




        
             
        

    




