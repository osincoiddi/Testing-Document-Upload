import time

import pynput.keyboard
import pytest
from PageObject.UploadDoc import UploadDocPage
from utilities.customlog import LogGen


class TestUploadDocPage:
    url="https://the-internet.herokuapp.com/upload"
    # url=ReadConfig.getapplicationurl()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_Upload_doc(self,setup):
        self.driver=setup
        self.driver.get("https://the-internet.herokuapp.com/upload")
        # self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(10)


        self.udp=UploadDocPage(self.driver)
        self.udp.clickChooseFilebtn(file_path=r"C:\\Users\\O\\OneDrive\\Documents\\selenium\\example_file.png")
        self.udp.clickUploadbtn()

    def keyboard(self,key):
        self.keyboard=pynput.keyboard.Controller()
        self.keyboard.type(r"C:\\Users\\O\\OneDrive\\Documents\\selenium\\example_file.png")
        self.keyboard.press(key.enter)
        self.keyboard.release(key.enter)



