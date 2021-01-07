import requests

class ScrapApp:
    """
        ScarpApp class which is used to scapping the stock's high, low, open 
        and close prices for a given date
        
    """
    def __init__(self):
        self.session = requests.Session()
        self.timeout = 2
        self.link = 'https://finance.yahoo.com/quote/{0}/history?p={0}'
    
    def check_symbol(self, symbol):
        response = self.session.get(self.link.format(symbol))
        response.raise_for_status()
        return True

    def check_date(self, date):
        return True

    def check_quit(self):
        """
            Check whether quit the app or not
        """
        print("Do you want to continue (Y/N): ", end = "")
        quit = input().upper()
        while quit != "Y" and quit != "N":
            print("Wrong input, please enter again: ", end = "")
            quit = input().upper()
        if quit == "N":
            return True
        return False


    def display_stock_price_data(self, symbol, date):
        print("Data 100\n")

    def run(self):
        """
            Run the ScrapApp to scrap the stock price data
        """

        # enter the app message
        print("Welcome to the ScrapApp...")

        # loop to obtain the stock price data
        while True:
            # obtain the stock tick symbol
            print("\nEnter the stock tick symbol (e.g. ISRG): ", end = "")
            symbol = input()
            while self.check_symbol(symbol) == False:
                print("No such stock tick symobl, please enter again: ", end = "")
                symbol = input()
            
            # obtain the date to search
            print("Enter the date to look for (e.g. 01/01/2021): ", end = "")
            date = input()
            while self.check_date(date) == False:
                print("No such date or incorrect date format, please enter again: ", end = "")
                date = input()
            
            # display the stock information
            self.display_stock_price_data(symbol, date)

            # end the app or not
            if self.check_quit() == True:
                break
        
        # quit the app message
        print("\nQuit the app!!")

def main():
    """
        main function
    """
    app = ScrapApp()
    app.run()

if __name__ == "__main__":
    main()
