from bs4 import BeautifulSoup
import urllib.request as urllib2
import requests
from requests.exceptions import HTTPError


class ScrapApp:
    """
        ScarpApp class which is used to scap the stock's high, low, open 
        and close prices for a given date
        
    """

    def __init__(self):
        """
            Initializatation for ScrapApp class (We use yahoo website.)
        """
        self.link = 'https://finance.yahoo.com/quote/{0}/history?p={0}'
    
    def check_symbol(self, symbol):
        """
            Check whether the stock tick symbol is appropriate or not
        
        Parameter:
            symbol (str): the given stock tick symbol

        Returns:
            (bool): Returns True if the input stock tick symbol is appropriate, 
                    otherwise return False
        """
        try:
            # open the link
            url_link = self.link.format(symbol)
            page = urllib2.urlopen(url_link)
            soup = BeautifulSoup(page, 'html.parser')

            # find the table with the given stock tick symbol
            tables = soup.findAll('table', {'class':'W(100%) M(0)'})
        except Exception as e:
            print(e)
            return False
        
        # if no table is found, then no such stock tick symbol and return False, 
        # otherwise return True
        if len(tables) == 0:
            print("Stock Tick Symbol: Not Found")
            return False
        else:
            return True

    def check_date(self, date):
        """
            Check whether the date is appropriate or not

        Parameter:
            date (str): the given date

        Returns:
            (bool): Returns True if the input date is appropriate, otherwise return False
        """
        return True

    def check_quit(self):
        """
            Check whether quit the app or not
        
        Returns:
            (bool): Returns True if quit the app, False otherwise
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
        url_link = self.link.format(symbol)
        page = urllib2.urlopen(url_link)
        soup = BeautifulSoup(page, 'html.parser')
        tables = soup.findAll('table', {'class':'W(100%) M(0)'})
 
        for table in tables:
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')

            for row in rows:
                col_name = row.find_all('span')
                col_val = row.find_all('td')
                col_val = [cell.text.strip() for cell in col_val]
                print(col_val[0] + " " + col_val[1] + " " + col_val[2] + " " + col_val[3])

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
                print("\nNo such stock tick symobl, please enter again: ", end = "")
                symbol = input()
            
            # obtain the date to search
            print("\nEnter the date to look for (e.g. 01/01/2021): ", end = "")
            date = input()
            while self.check_date(date) == False:
                print("\nNo such date or incorrect date format, please enter again: ", end = "")
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
