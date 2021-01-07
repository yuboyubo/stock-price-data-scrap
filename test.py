import unittest
from app import *

class ScrapAppTest(unittest.TestCase):
    """
        Unit Test for ScrapApp class
    """

    def test_check_symbol(self):
        """
            Unit Test for check_symbol() function
        """
        # initialization
        app = ScrapApp()

        # test for good symbols
        good_symbols = ["ISRG", "ILMN", "VRTX", "MELI", "MA", "ALGN", "EW", "IDXX", "ANET"]
        for symbol in good_symbols:
            self.assertTrue(app.check_symbol(symbol))
        
        # test for bad symbols 
        bad_symbols = ["1/23/", "123213", "$$$$", "VAEer", "`12-`12`", "131adad123", "incorrect"]
        for symbol in bad_symbols:
            self.assertFalse(app.check_symbol(symbol))

    def test_check_date(self):
        """
            Unit Test for check_date() function
        """
        # initialization
        app = ScrapApp()

        # test for good date
        good_dates = ["01/01/2021", "02/24/2021", "12/20/2020", "12/19/2020", "01/11/1999"]
        for date in good_dates:
            self.assertTrue(app.check_date(date))

        # test for bad date
        bad_dates = ["13/01/2021", "01/32/2011", "1231231","13/123/12311", "1/1/12021"]
        for date in bad_dates:
            self.assertFalse(app.check_date(date))

    def test_check_quit(self):
        """
            Unit Test for check_quit() function
        """
        # initialization
        app = ScrapApp()

        # test for quit the app
        self.assertTrue(app.check_quit("Y"))
        self.assertTrue(app.check_quit("y"))

        # test for not qutting the app or wrong input
        self.assertFalse(app.check_quit("N"))
        self.assertFalse(app.check_quit("n"))
        self.assertFalse(app.check_quit("ADASDAD"))
        self.assertFalse(app.check_quit("q"))

    def test_get_stock_price_data(self):
        """
            Unit Test for get_stock_price_data() function
        """
        # initialization
        app = ScrapApp()

        # test for ISRG
        symbol1 = "ISRG"

        # test1
        date1 = "01/06/2021"
        data1 = ["795.28", "792.79", "800.00", "786.86"]
        self.assertEqual(app.get_stock_price_data(symbol1, date1), data1)

        # test2
        date2 = "01/05/2021"
        data2 = ["793.89", "805.05", "811.39", "789.39"]
        self.assertEqual(app.get_stock_price_data(symbol1, date2), data2)

        # test3
        date3 = "12/30/2020"
        data3 = ["819.99", "815.30", "822.15", "812.04"]
        self.assertEqual(app.get_stock_price_data(symbol1, date3), data3)

        # test4
        date4 = "01/01/2021"
        data4 = None
        self.assertEqual(app.get_stock_price_data(symbol1, date4), data4)

        # test for MA
        symbol2 = "MA"

        # test1
        date1 = "01/06/2021"
        data1 = ["350.42", "347.55", "354.03", "344.56"]
        self.assertEqual(app.get_stock_price_data(symbol2, date1), data1)

        # test2
        date2 = "01/04/2021"
        data2 = ["358.00", "351.49", "358.13", "347.36"]
        self.assertEqual(app.get_stock_price_data(symbol2, date2), data2)

        # test3
        date3 = "12/31/2020"
        data3 = ["355.03", "356.94", "359.41", "353.25"]
        self.assertEqual(app.get_stock_price_data(symbol2, date3), data3)

        # test4
        date4 = "01/02/2021"
        data4 = None
        self.assertEqual(app.get_stock_price_data(symbol2, date4), data4)

if __name__ == '__main__':
    unittest.main()
