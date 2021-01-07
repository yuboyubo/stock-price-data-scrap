# Scrapping Stock Price Data Application

## About
A python application that can scrap stock price data from a [yahoo finance](https://finance.yahoo.com/quote/ISRG/history?p=ISRG) so that when given a stock tick symbol (e.g. "ISRG") as the input, the application returns the stock's high. low, open and close prices today.

## Install requirements:
This work is fully tested with Python 3.6.9 under Ubuntu 18.04.5 LTS. 

Install requirements in terminal, please run: ```pip3 install -Ur requirements.txt```

## How to test the application:
Run the test script: ```python3 -m unittest -v test.py  -b```

Example output:

```
test_check_date (test.ScrapAppTest) ... ok
test_check_quit (test.ScrapAppTest) ... ok
test_check_symbol (test.ScrapAppTest) ... ok
test_get_stock_price_data (test.ScrapAppTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 9.721s

OK
```

## How to run the application:
Run the main application: ```python3 app.py```

Example output:

```
Welcome to the ScrapApp...

Enter the stock tick symbol (e.g. ISRG): ISRG

Enter the date to look for (e.g. 01/13/2021): 01/06/2021

Here is the price data for ISRG at 01/06/2021:
Open:   795.28
Close:  792.79
High:   800.00
Low:    786.86

Do you want to continue (Y/N): Y

Enter the stock tick symbol (e.g. ISRG): ISRG

Enter the date to look for (e.g. 01/13/2021): 01/05/2021

Here is the price data for ISRG at 01/05/2021:
Open:   793.89
Close:  805.05
High:   811.39
Low:    789.39

Do you want to continue (Y/N): Y

Enter the stock tick symbol (e.g. ISRG): ISRG

Enter the date to look for (e.g. 01/13/2021): 01/01/2021

There is no price information for ISRG at 01/01/2021

Do you want to continue (Y/N): Y

Enter the stock tick symbol (e.g. ISRG): ILMN

Enter the date to look for (e.g. 01/13/2021): 01/06/2021

Here is the price data for ILMN at 01/06/2021:
Open:   367.43
Close:  376.55
High:   380.57
Low:    365.00

Do you want to continue (Y/N): Y

Enter the stock tick symbol (e.g. ISRG): ILMN

Enter the date to look for (e.g. 01/13/2021): 13/12/2021
Date String Format: Not Correct (e.g.: mm/dd/yyyy)

Incorrect date string format, please enter again or quit(q): 12/30/2020

Here is the price data for ILMN at 12/30/2020:
Open:   368.22
Close:  364.09
High:   370.34
Low:    360.76

Do you want to continue (Y/N): Y

Enter the stock tick symbol (e.g. ISRG): incorrect
Stock Tick Symbol: Not Found

No such stock tick symobl, please enter again or quit(q): q

Quit the app!!

```
