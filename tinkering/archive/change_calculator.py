cost_of_item = round(float(input("Cost of item: ")), 2)
tender = round(float(input("Tender rendered: ")), 2)

if tender < cost_of_item:
    print(f"That is not enough tender. Please render an additional "
          f"${cost_of_item - tender:.2f} in tender.")
if tender == cost_of_item:
    print("A perfect amount of tender was rendered! No rendering of change "
          "required!")

# global coin variables
# change = 0
# dollars = 0
# quarters = 0
# dimes = 0
# nickels = 0
# pennies = 0
if tender > cost_of_item:
    change = round(tender - cost_of_item, 2)
    print(f"Change to be rendered: ${change}\nThis will come as:")

    dollars = int(change)
    change = round((change - dollars) * 100)
    quarters = change // 25
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    pennies = change % 5

    if dollars > 0:
        if dollars == 1:
            print(f"\t{dollars} dollar")
        else:
            print(f"\t{dollars} dollars")
    if quarters > 0:
        if quarters == 1:
            print(f"\t{quarters} quarter")
        else:
            print(f"\t{quarters} quarters")
    if dimes > 0:
        if dimes == 1:
            print(f"\t{dimes} dime")
        else:
            print(f"\t{dimes} dimes")
    if nickels > 0:
        if nickels == 1:
            print(f"\t{nickels} nickel")
        else:
            print(f"\t{nickels} nickels")
    if pennies > 0:
        if pennies == 1:
            print(f"\t{pennies} penny")
        else:
            print(f"\t{pennies} pennies")

"""If pennies (or any other coin variable) were needed to be used elsewhere 
outside the if block, it would need to made a global variable (see above)."""
# print(pennies)
