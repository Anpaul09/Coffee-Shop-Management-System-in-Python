SMLCUP_SIZE = 9
MEDCUP_SIZE = 12
LRGCUP_SIZE = 15
SMLCUP_CHARGE = 1.75
MEDCUP_CHARGE = 1.90
LRGCUP_CHARGE = 2.00

def MenuPrinter():
    print("\n1: Enter 1 to order coffee.")
    print("2: Enter 2 to check the total money made up to this time.")
    print("3: Enter 3 to check the total amount of coffee sold up to this time.")
    print("4: Enter 4 to check the number of cups of coffee of each size sold.")
    print("5: Enter 5 to print the data.")
    print("9: Enter 9 to exit the program.")

def getCoffeeOrder(small_count, medium_count, large_count, total_money, total_coffee):
    overall_cost = 0
    overall_coffee = 0
    while True:
        print("\n1: Enter 1 to buy coffee in a small cup size (9 oz)")
        print("2: Enter 2 to buy coffee in a medium cup size (12 oz)")
        print("3: Enter 3 to buy coffee in a large cup size (15 oz)")
        print("9: Enter 9 to exit.")
        pick_option = int(input())
        if pick_option == 9:
            break
        num_cups = int(input("Enter the number of cups: "))
        if pick_option == 1:
            small_count += num_cups
            overall_cost += num_cups * SMLCUP_CHARGE
            overall_coffee += num_cups * SMLCUP_SIZE
        elif pick_option == 2:
            medium_count += num_cups
            overall_cost += num_cups * MEDCUP_CHARGE
            overall_coffee += num_cups * MEDCUP_SIZE
        elif pick_option == 3:
            large_count += num_cups
            overall_cost += num_cups * LRGCUP_CHARGE
            overall_coffee += num_cups * LRGCUP_SIZE
    print(f"\nPlease pay $ {overall_cost:.2f}")
    total_money += overall_cost
    total_coffee += overall_coffee
    return small_count, medium_count, large_count, total_money, total_coffee

def sumOfMoney(total_money):
    print(f"\nTotal money made: $ {total_money:.2f}")

def calculateTotalCoffee(total_coffee):
    print(f"\nTotal amount of coffee sold: {total_coffee} oz")

def verifyCupSizes(small_count, medium_count, large_count):
    print(f"\nSmall cup count: {small_count}")
    print(f"Medium cup count: {medium_count}")
    print(f"Large cup count: {large_count}")

def dataPrint(small_count, medium_count, large_count, total_coffee, total_money):
    verifyCupSizes(small_count, medium_count, large_count)
    calculateTotalCoffee(total_coffee)
    sumOfMoney(total_money)

def main():
    small_count = 0
    medium_count = 0
    large_count = 0
    total_money = 0
    total_coffee = 0
    
    while True:
        MenuPrinter()
        user_selection = int(input())
        if user_selection == 1:
            small_count, medium_count, large_count, total_money, total_coffee = getCoffeeOrder(
                small_count, medium_count, large_count, total_money, total_coffee
            )
        elif user_selection == 2:
            sumOfMoney(total_money)
        elif user_selection == 3:
            calculateTotalCoffee(total_coffee)
        elif user_selection == 4:
            verifyCupSizes(small_count, medium_count, large_count)
        elif user_selection == 5:
            dataPrint(small_count, medium_count, large_count, total_coffee, total_money)
        elif user_selection == 9:
            break

main()
