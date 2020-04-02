def main():
    total = 0
    num = int(input("Enter the number of items: "))
    while num < 0:
        print("Please enter a valid number.")
        num = int(input("Enter the number of items: "))
    else:
        for i in range(num):
            price = float(input("Price of item: "))
            total += price
            if total > 100:
                total *= 0.9
    print("Total price for ", num, " item(s) is $", total, sep='')


if __name__ == '__main__':
    main()
