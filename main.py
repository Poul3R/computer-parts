import analyzer as an


def main():
    while True:
        print("""
        What would you like to do?
        
        1. Get average price of all laptops
        2. Get correlation diagram of price and all components
        3. Predict price of laptop with particular components 
        4. Exit
        
        Type number of choice:
        """)

        typed = input()

        if int(typed) == 1:
            an.get_statistics("Cena", "average")
        elif int(typed) == 2:
            an.pearson_correlation()
        elif int(typed) == 3:
            print("[GET VALUE] Amount of COREs: ")
            cores = int(input())
            print("[GET VALUE] Amount of RAM: ")
            ram = int(input())
            print("[GET VALUE] Capacity of disc: ")
            capacity = int(input())
            print("[GET VALUE] Size of display: ")
            display = float(input())
            print("[GET VALUE] Warranty: ")
            warranty = int(input())

            predicted_price = an.linear_regression([cores, ram, capacity, display, warranty])

            to_print = """
            
            [RESULT] ESTIMATED PRICE OF THIS LAPTOP IS EQUAL
            %s
            """ % (predicted_price,)

            print(to_print)

        elif int(typed) == 4:
            break
        else:
            print("[info] Incorrect value passed")
            pass

    print("[info] You have already leaved program")


main()
