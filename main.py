from analyzer import Analyzer
from scraper import MediaMarktScraper


def main():
    while True:
        print("""
______________________________________________________________________________________________________

##          #   #########   ##           ##########     ###########   #####      #####   ###########
##          #   #           ##           ##             ##        #   ##   #    #    #   ##
##    #     #   ######      ##           ##             ##        #   ##    #  #     #   #######
##    #     #   #           ##           ##             ##        #   ##     ##      #   ##
##    #     #   #           ##           ##             ##        #   ##             #   ##
 ###########    #########   ##########   ###########    ###########   ##             #   ############

                                    IN 'SMART ESTIMATOR'
______________________________________________________________________________________________________

Now you can scrap data to get latest informations about products or use existing one.
Note that scraping process can take up to few hours.

---------------------------
What would you like to do?
1. Scrap data
2. Predict price

Type number of choice
        """)
        typed = int(input())

        if typed == 1:
            mediaMarktScraper = MediaMarktScraper()
            mediaMarktScraper.main()
        elif typed == 2:
            main_loop()
        else:
            pass


def main_loop():
    analyzer = Analyzer()
    while True:
        print("""
______________________________________________________
What would you like to do?

1. Get average price of all laptops
2. Get correlation diagram of price and all components
3. Predict price of laptop with particular components 
4. Exit

Type number of choice:
            """)

        typed = input()

        if int(typed) == 1:
            analyzer.get_statistics("Cena", "average")
        elif int(typed) == 2:
            analyzer.pearson_correlation()
        elif int(typed) == 3:
            print("[GET VALUE] Amount of COREs: ")
            cores = int(input())
            print("[GET VALUE] Amount of RAM: ")
            ram = int(input())

            print("[GET VALUE] Type of disc (SSD or HDD): ")
            disc_type = input()
            while disc_type.upper() != 'SSD' and disc_type.upper() != 'HDD':
                print("[GET VALUE] Type of disc (SSD or HDD): ")
                disc_type = input()

            if disc_type.upper() == 'SSD':
                disc_type = 1
            else:
                disc_type = 0

            print("[GET VALUE] Capacity of disc: ")
            capacity = int(input())
            print("[GET VALUE] Size of display: ")
            display = float(input())

            print("[GET VALUE] Operating system (Windows, macOS or Other): ")
            operating_system = input()
            while operating_system.upper() != 'WINDOWS' \
                    and operating_system.upper() != 'MACOS' \
                    and operating_system.upper() != 'OTHER':
                print("[GET VALUE] Operating system (Windows, macOS or Other): ")
                operating_system = input()

            if operating_system.upper() == 'WINDOWS':
                operating_system = 2
            elif operating_system.upper() == 'MACOS':
                operating_system = 1
            else:
                operating_system = 0

            print('[GET VALUE] Warranty: ')
            warranty = int(input())

            predicted_price, effectiveness = analyzer.linear_regression(
                [cores, ram, disc_type, capacity, display, operating_system, warranty])

            result = round(float(predicted_price),0)

            to_print = """

[RESULT] ESTIMATED PRICE OF THIS LAPTOP IS EQUAL
                    
           ------>   %s   <------
            (Effectiveness: %s)
                
                """ % (result, effectiveness)

            print(to_print)

        elif int(typed) == 4:
            break
        else:
            print("[info] Incorrect value passed")
            pass

    print("[info] You have already leaved program")


main()
