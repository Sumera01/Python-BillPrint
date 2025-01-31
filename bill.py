print("Welcome to Sumaira's  Restaurant")

todo = int(input("Enter -->\t1 to display menu -- \t2 to order -- \t3 to calculate bill: "))
menu = {"Burger": 70, "Sandwich": 80, "Veg_Roll": 150, "Fries": 40, "MoMos": 150, "Zinger": 150, "Chicken_Roll": 180, "Sikkh_Kebab": 130, "Shawarma": 100}
ordered={}
total=0

while todo != 3:
    if todo == 1:
        option = input("Enter\nV for vegetarian \nN for non-vegetarian \nA for all: ")
        print("--" * 20)
        print("------------------Menu------------------")
        if option.upper() == "V":
            print("\n\tBurger        -- 70 \n\tSandwich      -- 80 \n\tVeg_Roll      -- 150 \n\tFries         -- 40")
            print("--" * 20)
        elif option.upper() == "N":
            print("\n\tMoMos         -- 150\n\tZinger        -- 150 \n\tChicken_Roll  -- 180 \n\tSikkh_kebab   -- 130 \n\tShawarma      -- 100\n")
            print("--" * 20)
        elif option.upper() == "A":
            print("\n\tBurger        -- 70 \n\tSandwich      -- 80 \n\tVeg_Roll      -- 150 \n\tFries         -- 40"
                  "\n\tMoMos         -- 150\n\tZinger        -- 150 \n\tChicken_Roll  -- 180 \n\tSikkh_Kebab   -- 130 \n\tShawarma      -- 100\n")
            print("--" * 20)
        else:
            print("Please enter a valid option: V, N, or A")

    elif todo == 2:
        print("Your Order:")
        a = int(input("Enter 1 to order and 0 to stop: "))
        while a == 1:
            order = input("Enter the item you want to order given above (as given above): ")
            if order in menu :
                ordered[order] = menu[order]
                total += menu[order]
                print("Added item -> ",order,"to your Order!")
            else:
                print("Wrong Name Try again!")
            a = int(input("Enter 1 to order and 0 to stop: "))
    todo = int(input("Enter -->\t1 to display menu -- \t2 to order -- \t3 to calculate bill: "))

print("\n------ Your Bill ------")
print("\nItem\t\t\t\t\tPrice")
print("-" * 35)
for key in ordered:
    if key=="Chicken_Roll" or key=="Sikkh_Kebab":
        print(key, "\t\t\t", ordered[key])
    elif key == "Veg_Roll" or key == "Shawarma" or key == "Sandwich":
        print(key, "\t\t\t\t", ordered[key])
    else:
        print(key,"\t\t\t\t\t",ordered[key])

print("-" * 35)
print("\t\t\tTotal Bill:",total)
print("------------------------------")
print("\n\nThank you Visit Again!.")

