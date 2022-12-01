#Basic Python Interactive Calculator by Monti

#Intro
print("\n\tHey! I have a question for you!\n")

#Vars/inputs
fav_num = input("What's your favorite number?\n ")

math_prob = input("\nWould you like to do a quick math problem with your favorite number " + fav_num + "? yes or no\n ")

opti = "add, subtract, multiply, divide or exponent"

# If they choose to not do a math problem
if math_prob == "no":
    print("Okay! That's cool! " + fav_num + " is still Awesome!")
    exit()

# If they choose to do a math problem
if math_prob == "yes":
    pick = input("\nCool! Do you want to add, subtract, multiply, divide or exponent?\n ")
#Additon    
if pick == "add":
    m_input = input("\nGreat! Give me a number to " + pick + "!\n ")
    print("\nYour favorite number " + fav_num + " plus " + m_input + " equals....")
    print(int(fav_num) + int(m_input))
#Substraction    
elif pick == "subtract":
    m_input = input("\nNice! Give me a number to " + pick + "!\n ")
    print("\nYour favorite number " + fav_num + " subtracted from " + m_input + " equals....")
    print(int(fav_num) - int(m_input))
#Multiplication
elif pick == "multiply":
    m_input = input("\nAwesome! Give me a number to " + pick + "!\n ")
    print("\nIf you " + pick + " your favorite number " + fav_num + " times " + m_input + ", it equals....")
    print(int(fav_num) * int(m_input))
#Division    
elif pick == "divide":
    m_input = input("\nDivision it is! Give me a number to " + pick + "!\n ")
    print("\nIf you " + pick + " your favorite number " + fav_num + " by " + m_input + ", it equals....")
    print(int(fav_num) / int(m_input))
#Exponents    
elif pick == "exponent":
    m_input = input("\nThis will be fun! Give me a number to use to make an " + pick + "!\n ")
    print("\nYour favorite number " + fav_num + " to the power of " + m_input + " equals....")
    print(int(fav_num) ** int(m_input))
#Input isn't yes or no    
else:
    print("\nSorry! You have to choose " + opti + ".")
    again = input("\nWant to try again? yes or no\n ")
    if again == "no": #Doesnt attempt 2nd try, ends program
        print("\nOkay! That's cool! " + fav_num + " is still Awesome!")
        exit()

    if again == "yes": #Gives a 2nd try
        pick = input("\nChoose add, subtract, multiply, divide or exponent.\n ")
        if pick == "add": #Addition
            m_input = input("\nGreat! Give me a number to " + pick + "!\n ")
            print("\nYour favorite number " + fav_num + " plus " + m_input + " equals....")
            print(int(fav_num) + int(m_input))
    #Substraction
        elif pick == "subtract":
            m_input = input("\nNice! Give me a number to " + pick + "!\n ")
            print("\nYour favorite number " + fav_num + " subtracted from " + m_input + " equals....")
            print(int(fav_num) - int(m_input))
    #Multiplication
        elif pick == "multiply":
            m_input = input("\nAwesome! Give me a number to " + pick + "!\n ")
            print("\nIf you " + pick + " your favorite number " + fav_num + " times " + m_input + ", it equals....")
            print(int(fav_num) * int(m_input))
    #Division
        elif pick == "divide":
            m_input = input("\nDivision it is! Give me a number to " + pick + "!\n ")
            print("\nIf you " + pick + " your favorite number " + fav_num + " by " + m_input + ", it equals....")
            print(int(fav_num) / int(m_input))
    #Exponents
        elif pick == "exponent":
            m_input = input("\nThis will be fun! Give me a number to use to make an " + pick + "!\n ")
            print("\nYour favorite number " + fav_num + " to the power of " + m_input + " equals....")
            print(int(fav_num) ** int(m_input))
    #Any user input ends the program with a message
        else:
            print("Again... The options are " + opti + ".")
            nope = input("\nDo you STILL want to try again?\n ")
            if nope == "yes":
                print("\nEhh! Maybe you should try again later...")
                exit()
            elif nope == "no":
                print("\nYeah! I agree...")
            else:
                print("\nHmmm... I don't know...")
        

