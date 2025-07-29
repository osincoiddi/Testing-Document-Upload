import os.path
from selenium.webdriver.common.by import By


class UploadDocPage:
    #locators
    choose_file_xpath="//input[@id='file-upload']"
    upload_xpath="//input[@id='file-submit']"

    #constractors

    def __init__(self,driver):
        self.file_input = None
        self.driver=driver

       #action methods
    def clickChooseFilebtn(self,file_path):
        self.file_input=self.driver.find_element(By.XPATH,self.choose_file_xpath)
        self.file_path=os.path.abspath(r"C:\\Users\\O\\Documents\\selenium\\example_file.png")
        self.file_input.send_keys(file_path)

    def clickUploadbtn(self):
        self.driver.find_element(By.XPATH,self.upload_xpath).click()



