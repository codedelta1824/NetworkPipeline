from pipeline import Engine

class Menu():
    def run():
        while True:
            try:
                print("\n1) Check App Status")
                print("2) Exit")

                user_input = int(input("Enter a num: "))

                if user_input == 1:
                    Engine.message()
                elif user_input == 2:
                    print("Exiting Application")
                    exit()

            except ValueError as e:
                    print("Invalid Input!!!")