from bs4 import BeautifulSoup
import urllib.request
import datetime

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
        self.date_format = "%m/%d/%Y"
        self.link_date_format = "%b %d, %Y"
    
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
            page = urllib.request.urlopen(url_link)
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
        try:
            datetime.datetime.strptime(date, self.date_format)
        except ValueError:
            print("Date String Format: Not Correct (e.g.: mm/dd/yyyy)")
            return False
        return True

    def check_quit(self):
        """
            Check whether quit the app or not
        
        Returns:
            (bool): Returns True if quit the app, False otherwise
        """
        print("\nDo you want to continue (Y/N): ", end = "")
        quit = input().upper()
        while quit != "Y" and quit != "N":
            print("Wrong input, please enter again: ", end = "")
            quit = input().upper()
        if quit == "N":
            return True
        return False

    def get_stock_price_data(self, symbol, date):
        """
            Get the stock price data for the given stock tick symbol and the date

        Parameters:
            symbol (str): the given stock tick symbol
            date (str): the given date

        Return:
            (List): If date is found, then return [Open, Close, High, Low] price data,
                    otherwise, return None
        """
        # open the link and get the table
        url_link = self.link.format(symbol)
        page = urllib.request.urlopen(url_link)
        soup = BeautifulSoup(page, 'html.parser')
        tables = soup.findAll('table', {'class':'W(100%) M(0)'})
        
        # change the date into new format
        date = datetime.datetime.strftime(datetime.datetime.strptime(date, self.date_format), self.link_date_format)

        # go through all the found tables
        for table in tables:

            # obtain the row information in each table
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')

            for row in rows:
                # get each col information
                col_val = row.find_all('td')
                col_val = [cell.text.strip() for cell in col_val]
                
                # check the date and if found, return [Open, Close, High, Low] price data.
                if col_val[0] == date:
                   return [col_val[1], col_val[4], col_val[2], col_val[3]]
        
        # if no date is found, return None
        return None

    def display_price_data(self, data, symbol, date):
        """
            Display the price data information for the given stock tick symbol and the date

        Parameters:
            data (List): input price data or None
            symbol (str): input stock tick symbol
            date (str): input date
        """
        if data == None:
            print("\nThere is no price information for {0} at {1}".format(symbol, date)) 
        else:
            print("\nHere is the price data for {0} at {1}:".format(symbol, date))
            print("Open:  ", data[0])
            print("Close: ", data[1])
            print("High:  ", data[2])
            print("Low:   ", data[3])
                    

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
            while symbol.lower() != 'q' and self.check_symbol(symbol) == False:
                print("\nNo such stock tick symobl, please enter again or quit(q): ", end = "")
                symbol = input()
            
            # if input is q, then quit the app
            if symbol.lower() == 'q':
                break
            
            # obtain the date to search
            print("\nEnter the date to look for (e.g. 01/13/2021): ", end = "")
            date = input()
            while date.lower() != 'q' and self.check_date(date) == False:
                print("\nIncorrect date string format, please enter again or quit(q): ", end = "")
                date = input()
            
            # if input is q, then quit the app
            if date.lower() == 'q':
                break

            # display the stock information if date is found, otherwise display the alert message
            price_data = self.get_stock_price_data(symbol, date)
            self.display_price_data(price_data, symbol, date)

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
