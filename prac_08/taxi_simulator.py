"""
Author: Han Su
Date: 18/05/2020
https://github.com/HanSu52/cp1404practicals
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """This is a program that stimulates driving taxis and returns the trip cost."""
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    current_car = None

    print("Let's drive!")
    menu_choice = display_menu()
    while True:
        if menu_choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_car = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(bill_to_date))
            menu_choice = display_menu()

        elif menu_choice == "d":
            current_car.start_fare()
            distance = int(input("Drive how far? "))
            current_car.drive(distance)
            trip_cost = current_car.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_car.name, trip_cost))
            bill_to_date += trip_cost
            print("Bill to date: ${:.2f}".format(bill_to_date))
            menu_choice = display_menu()

        elif menu_choice == "q":
            print("Total trip cost: ${:.2f}".format(bill_to_date))
            print("Taxis are now:")
            display_taxis(taxis)
            break

        else:
            print("Invalid menu choice.")
            menu_choice = display_menu()


def display_taxis(taxis):
    """Display all the taxis that are available."""
    for i, each in enumerate(taxis, start=0):
        print("{} - {}".format(i, each))


def display_menu():
    """Display the menu for users to chose."""
    menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    return menu_choice


if __name__ == '__main__':
    main()
