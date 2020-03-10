from selenium import webdriver
import time

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def logIn(self):
        self.driver.get("https://tinder.com")
        time.sleep(5)
        closePopUp = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button')
        closePopUp.click()
        logInButton = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        logInButton.click()
        faceBookLogIn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        faceBookLogIn.click()

bot = TinderBot()
bot.logIn()
