def main():
    name = input("Please Enter your name here: ")
    OUTPUT_FILE1 = "name.txt"
    OUTPUT_FILE2 = "numbers.txt"
    out_file1 = open(OUTPUT_FILE1, 'w')
    print(name, file=out_file1)
    out_file1.close()

    in_file1 = open("name.txt", "r")
    output_name = in_file1.read()
    print("Your name is", output_name)
    in_file1.close()

    out_file2 = open(OUTPUT_FILE2, 'w')
    print("17", file=out_file2)
    print("42", file=out_file2)
    print("400", file=out_file2)
    out_file2.close()

    in_file2 = open("numbers.txt", "r")
    num1 = int(in_file2.readline())
    num2 = int(in_file2.readline())
    result1 = num1 + num2
    print(result1)
    in_file2.close()

    in_file2 = open("numbers.txt", "r")
    num3 = int(in_file2.readline())
    num4 = int(in_file2.readline())
    num5 = int(in_file2.readline())
    result2 = num3 + num4 + num5
    print(result2)
    in_file2.close()


if __name__ == '__main__':
    main()
