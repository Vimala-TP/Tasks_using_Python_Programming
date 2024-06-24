#Module File of name Menu
def ServiceMenu():
    print("""\n---Services Available---
1.Shopping
2.Verification
3.Billing
4.Exit""")
    return int(input("Select the option what you wanted to do = "))
def ShoppingMenu():
    print("""\n---Shopping Process---
1.Grocerry
2.Kitchen
3.Clothes
4.To move to Service Menu""")
    return int(input("\nEnter the kind of item you want to purchase = "))
def GrocerryMenu():
    print("""\n----Grocerry Items---
1.Sugar = 1kg = 40Rs
2.Rice  = 1kg = 60Rs
3.Dhall = 1kg = 50Rs
4.Salt  = 1kg = 30Rs
5.To move to Shopping Menu""")
    print("\nTo Add enter +quantity_required and to remove -quantity_required")
    return int(input("Enter the items you required = "))
def KitchenMenu():
    print("""\n----Kitchen Items---
1.Spoon         = 1 pack  = 60Rs
2.Plates        = 1 plate = 100Rs
3.Kitchen Towel = 1 roll  = 80Rs
4.Cutting board = 1 board = 220Rs
5.To move to Shopping Menu""")
    print("\nTo Add enter +quantity_required and to remove -quantity_required")
    return int(input("Enter the items you required = "))
def ClothesMenu():
    print("""\n----Clothes---
1.Jacket       = 1 jacket    = 1950Rs
2.T-Shirt      = 1 Shirt     = 500Rs
3.Towel        = 1 Towel     = 150Rs
4.HandKerchief = 1 Kerchief  = 60Rs
5.To move to Shopping Menu""")
    print("\nTo Add enter +quantity_required and to remove -quantity_required")
    return int(input("Enter the items you required = "))
