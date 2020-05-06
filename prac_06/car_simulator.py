"""
Author: Han Su
Date: 01/05/2020
https://github.com/HanSu52/cp1404practicals
"""
from prac_06.car import Car


def main():
    print("Let's drive!")
    name = input("Enter you car name: ")
    car = Car(name, 100)

    print(car)
    menu_choice = display_menu()
    while True:
        if menu_choice == "d":
            distance = int(input("How many km do you wish to drive? "))
            while distance < 0:
                print("Distance must be >= 0")
                distance = int(input("How many km do you wish to drive? "))
            if car.fuel > distance:
                car.drive(distance)
                print("The car drove {}km.\n".format(distance))
            else:
                print("The car drove {}km and ran out of fuel.\n".format(car.fuel))
                car.drive(distance)

        elif menu_choice == "r":
            amount = int(input("How many units of fuel do you want to add to the car? "))
            while amount < 0:
                print("Fuel amount must be >= 0")
                amount = int(input("How many units of fuel do you want to add to the car? "))
            while amount >= 0:
                print("Added {} units of fuel.\n".format(amount))
                break
            car.add_fuel(amount)

        elif menu_choice == "q":
            print("\nGood bye {}'s driver.".format(name))
            break

        else:
            print("Invalid choice\n")
        print(car)
        menu_choice = display_menu()


def display_menu():
    menu_choice = input("Menu:\nd) drive\nr) refuel\nq) quit\nEnter your choice: ").lower()
    return menu_choice


if __name__ == '__main__':
    main()
