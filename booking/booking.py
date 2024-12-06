import booking.constants as const 
import os
from selenium.webdriver.common.by import By
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Users\adars\Desktop\subjects\django\new1\pre1\ven\Lib\site-packages\django\test\selenium.py", teardown=False):
        self.driver_path=driver_path
        self.teardown=teardown
        os.environ['PATH']+=self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_curreny(self,currency=None):
        currency_element=self.find_element(By.CSS_SELECTOR,'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
