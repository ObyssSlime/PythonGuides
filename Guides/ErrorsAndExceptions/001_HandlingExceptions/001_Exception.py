while True:
    try:
        x = int(input("Please Enter a Number: "))
        print("Ah, you did it bro")
        break

    except ValueError:
        print("Oops! that was no valid number, try again bro...")
